import json
from openai import OpenAI

client = OpenAI(api_key="API KEY")

with open("user_data.json") as f:
    user_data = json.load(f)

def generate_recommendation(user):
    aspect_sentiments = ", ".join(
        [f"{k} ({v['sentiment']}): {v['score']}" for k, v in user["aspect_based_sentiment"].items()]
    )
    
    emotions = ", ".join([f"{e}: {s}" for e, s in user["intent_emotion"]["emotion_scores"].items()])
    
    key_concerns = ", ".join(user["key_concerns"]) if user["key_concerns"] else "None"
    positive_aspects = ", ".join(user["positive_aspects"]) if user["positive_aspects"] else "None"
    
    prompt = f"""
You are a sales assistant. Here’s the user data:
- User ID: {user['user_id']}
- Overall category: {user['overall_category']}
- Overall sentiment score: {user['overall_sentiment_score']}
- Aspect-based sentiment: {aspect_sentiments}
- Intent: {user['intent_emotion']['intent']} (confidence: {user['intent_emotion']['intent_confidence']})
- Emotions: {emotions}
- Sentiment trend: {user['sentiment_trend']}
- Key concerns: {key_concerns}
- Positive aspects: {positive_aspects}

Write a concise 1–2 sentence recommendation for the sales team:
- Emphasize positives
- Address key concerns
- Suggest next steps to turn the interaction into a sale
- Consider sentiment, emotions, and intent confidence
"""
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

all_recommendations = []
for user in user_data:
    rec = generate_recommendation(user)
    all_recommendations.append({"user_id": user["user_id"], "recommendation": rec})

for r in all_recommendations:
    print(f"User {r['user_id']} -> Recommendation: {r['recommendation']}\n")
    