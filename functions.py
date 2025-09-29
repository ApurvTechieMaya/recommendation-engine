import pandas as pd
from openai import OpenAI
from collections import Counter

client = OpenAI(api_key="API Key")

def sentiment_mapping(val):
#Converting aspect labels to numeric score for averaging
    mapping = {"positive": 1, "neutral": 0, "negative": -1}
    return mapping.get(val, 0)

def aggregate_user(user_df):
    user_df = user_df.sort_values("timestamp")
    
    avg_sentiment = user_df["overall_sentiment"].mean()
    avg_intent = user_df["intent_score"].mean()
    avg_engagement = user_df["engagement"].mean()
    last_aspects = user_df.iloc[-1]["aspects"]
    last_intent = user_df.iloc[-1]["intent"]
    
    # Aspect-Level Sentiment
    aspect_sums = {}
    aspect_counts = {}
    for row in user_df.itertuples():
        for aspect, sentiment in row.aspects.items():
            aspect_sums[aspect] = aspect_sums.get(aspect, 0) + sentiment_mapping(sentiment)
            aspect_counts[aspect] = aspect_counts.get(aspect, 0) + 1
    avg_aspect_sentiment = {k: aspect_sums[k]/aspect_counts[k] for k in aspect_sums}
    
    # Intent Evolution
    first_intent = user_df.iloc[0]["intent"]
    intent_trend = (last_intent, first_intent)
    
    # Emotion analysis: average per emotion type
    emotion_sums = {}
    emotion_counts = {}
    for row in user_df.itertuples():
        for emo, val in row.emotion.items():
            emotion_sums[emo] = emotion_sums.get(emo, 0) + val
            emotion_counts[emo] = emotion_counts.get(emo, 0) + 1
    avg_emotion = {k: emotion_sums[k]/emotion_counts[k] for k in emotion_sums}
    
    return pd.Series({
        "avg_sentiment": avg_sentiment,
        "avg_intent": avg_intent,
        "avg_engagement": avg_engagement,
        "last_aspects": last_aspects,
        "last_intent": last_intent,
        "avg_aspect_sentiment": avg_aspect_sentiment,
        "intent_trend": intent_trend,
        "avg_emotion": avg_emotion
    })

def compute_composite(row, max_eng):
    intent_weight = 1.0 if row["last_intent"] == "purchase" else 0.7 if row["last_intent"] == "research" else 0.5
    score = (
        0.35 * row["avg_sentiment"] +
        0.35 * row["avg_intent"] * intent_weight +
        0.2 * (row["avg_engagement"] / max_eng)
    )
    return min(max(score, 0), 1)

def categorize_lead(row):
    score = row["composite_score"]
    if score > 0.7 and row["last_intent"] == "purchase":
        return "Hot"
    elif 0.4 <= score <= 0.7:
        return "Neutral"
    else:
        return "Cold"

# Keyword recommendation
def aggregate_keywords(user_df):
    total_keywords = Counter()
    for kw_dict in user_df["keyword_count"]:
        total_keywords.update(kw_dict)
    return dict(total_keywords)

def top_keywords(keyword_dict, top_n=3):
    if not keyword_dict:
        return []
    # Sorting the keywords by frequency
    sorted_keywords = sorted(keyword_dict.items(), key=lambda x: x[1], reverse=True)
    return [k for k, v in sorted_keywords[:top_n]]

def generate_recommendation_ai(row):
    
    aspect_sentiment_str = ", ".join([f"{k}: {v:.2f}" for k, v in row['avg_aspect_sentiment'].items()])
    emotion_str = ", ".join([f"{k}: {v:.2f}" for k, v in row['avg_emotion'].items()])
    intent_trend_str = f"{row['intent_trend'][1]} → {row['intent_trend'][0]}"
    keywords = ", ".join(row['top_keywords']) if row['top_keywords'] else "key topics"
    
    prompt = f"""
    You are an assistant helping sales teams.
    Here’s the user data:
    - Lead category: {row['lead_category']}
    - Composite score: {row['composite_score']:.2f}
    - Average sentiment: {row['avg_sentiment']:.2f}
    - Intent: {row['last_intent']}
    - Intent trend: {intent_trend_str}
    - Positive aspects: {[k for k,v in row['last_aspects'].items() if v=='positive']}
    - Negative aspects: {[k for k,v in row['last_aspects'].items() if v=='negative']}
    - Avg aspect sentiment: {aspect_sentiment_str}
    - Avg emotions: {emotion_str}
    - Top keywords: {keywords}

    Write a clear sales recommendation (1–2 sentences). 
    Emphasize positive aspects, suggest improvements for negatives, 
    mention how to use top keywords in messaging, and consider sentiment trends and user emotions.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()
