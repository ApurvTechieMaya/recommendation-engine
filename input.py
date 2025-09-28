user_data = [
    {
        "user_id": "1",
        "overall_category": "Hot",
        "overall_sentiment_score": 0.85,
        "aspect_based_sentiment": {
            "price": {"sentiment": "negative", "score": -0.6},
            "location": {"sentiment": "positive", "score": 0.8},
            "amenities": {"sentiment": "neutral", "score": 0.1},
            "mortgage_rates": {"sentiment": "negative", "score": -0.4}
        },
        "intent_emotion": {
            "intent": "Purchase",
            "intent_confidence": 0.9,
            "emotions": ["Excitement", "Anxiety"],
            "emotion_scores": {"Excitement": 0.8, "Anxiety": 0.3}
        },
        "sentiment_trend": "increasing",
        "key_concerns": ["price", "mortgage_rates"],
        "positive_aspects": ["location"]
    },
    {
        "user_id": "2",
        "overall_category": "Neutral",
        "overall_sentiment_score": 0.6,
        "aspect_based_sentiment": {
            "price": {"sentiment": "neutral", "score": 0.0},
            "location": {"sentiment": "positive", "score": 0.7},
            "amenities": {"sentiment": "neutral", "score": 0.1}
        },
        "intent_emotion": {
            "intent": "Research",
            "intent_confidence": 0.6,
            "emotions": ["Curiosity"],
            "emotion_scores": {"Curiosity": 0.7}
        },
        "sentiment_trend": "stable",
        "key_concerns": ["price"],
        "positive_aspects": ["location"]
    },
    {
        "user_id": "3",
        "overall_category": "Cold",
        "overall_sentiment_score": 0.35,
        "aspect_based_sentiment": {
            "price": {"sentiment": "negative", "score": -0.7},
            "location": {"sentiment": "neutral", "score": 0.0},
            "amenities": {"sentiment": "negative", "score": -0.5}
        },
        "intent_emotion": {
            "intent": "Hesitant",
            "intent_confidence": 0.4,
            "emotions": ["Anxiety"],
            "emotion_scores": {"Anxiety": 0.8}
        },
        "sentiment_trend": "decreasing",
        "key_concerns": ["price", "amenities"],
        "positive_aspects": []
    },
    {
        "user_id": "4",
        "overall_category": "Hot",
        "overall_sentiment_score": 0.9,
        "aspect_based_sentiment": {
            "price": {"sentiment": "positive", "score": 0.8},
            "location": {"sentiment": "positive", "score": 0.9},
            "service": {"sentiment": "positive", "score": 0.95}
        },
        "intent_emotion": {
            "intent": "Purchase",
            "intent_confidence": 0.95,
            "emotions": ["Excitement", "Curiosity"],
            "emotion_scores": {"Excitement": 0.9, "Curiosity": 0.7}
        },
        "sentiment_trend": "increasing",
        "key_concerns": [],
        "positive_aspects": ["price", "location", "service"]
    },
    {
        "user_id": "5",
        "overall_category": "Neutral",
        "overall_sentiment_score": 0.55,
        "aspect_based_sentiment": {
            "price": {"sentiment": "neutral", "score": 0.0},
            "location": {"sentiment": "neutral", "score": 0.1},
            "service": {"sentiment": "neutral", "score": 0.0}
        },
        "intent_emotion": {
            "intent": "Research",
            "intent_confidence": 0.5,
            "emotions": ["Curiosity", "Anxiety"],
            "emotion_scores": {"Curiosity": 0.6, "Anxiety": 0.4}
        },
        "sentiment_trend": "stable",
        "key_concerns": ["price"],
        "positive_aspects": []
    },
    {
        "user_id": "6",
        "overall_category": "Hot",
        "overall_sentiment_score": 0.78,
        "aspect_based_sentiment": {
            "location": {"sentiment": "positive", "score": 0.8},
            "service": {"sentiment": "positive", "score": 0.75},
            "amenities": {"sentiment": "neutral", "score": 0.2}
        },
        "intent_emotion": {
            "intent": "Purchase",
            "intent_confidence": 0.85,
            "emotions": ["Excitement"],
            "emotion_scores": {"Excitement": 0.75}
        },
        "sentiment_trend": "increasing",
        "key_concerns": [],
        "positive_aspects": ["location", "service"]
    },
    {
        "user_id": "7",
        "overall_category": "Cold",
        "overall_sentiment_score": 0.3,
        "aspect_based_sentiment": {
            "price": {"sentiment": "negative", "score": -0.6},
            "location": {"sentiment": "neutral", "score": 0.0},
            "amenities": {"sentiment": "negative", "score": -0.5}
        },
        "intent_emotion": {
            "intent": "Hesitant",
            "intent_confidence": 0.4,
            "emotions": ["Anxiety", "Curiosity"],
            "emotion_scores": {"Anxiety": 0.8, "Curiosity": 0.3}
        },
        "sentiment_trend": "decreasing",
        "key_concerns": ["price", "amenities"],
        "positive_aspects": []
    },
    {
        "user_id": "8",
        "overall_category": "Hot",
        "overall_sentiment_score": 0.88,
        "aspect_based_sentiment": {
            "price": {"sentiment": "positive", "score": 0.8},
            "location": {"sentiment": "positive", "score": 0.9},
            "service": {"sentiment": "positive", "score": 0.85}
        },
        "intent_emotion": {
            "intent": "Purchase",
            "intent_confidence": 0.9,
            "emotions": ["Excitement"],
            "emotion_scores": {"Excitement": 0.9}
        },
        "sentiment_trend": "increasing",
        "key_concerns": [],
        "positive_aspects": ["price", "location", "service"]
    },
    {
        "user_id": "9",
        "overall_category": "Neutral",
        "overall_sentiment_score": 0.5,
        "aspect_based_sentiment": {
            "price": {"sentiment": "neutral", "score": 0.0},
            "location": {"sentiment": "neutral", "score": 0.1},
            "amenities": {"sentiment": "neutral", "score": 0.0}
        },
        "intent_emotion": {
            "intent": "Research",
            "intent_confidence": 0.55,
            "emotions": ["Curiosity"],
            "emotion_scores": {"Curiosity": 0.5}
        },
        "sentiment_trend": "stable",
        "key_concerns": ["price"],
        "positive_aspects": []
    },
    {
        "user_id": "10",
        "overall_category": "Hot",
        "overall_sentiment_score": 0.92,
        "aspect_based_sentiment": {
            "price": {"sentiment": "positive", "score": 0.85},
            "location": {"sentiment": "positive", "score": 0.9},
            "amenities": {"sentiment": "positive", "score": 0.8}
        },
        "intent_emotion": {
            "intent": "Purchase",
            "intent_confidence": 0.95,
            "emotions": ["Excitement"],
            "emotion_scores": {"Excitement": 0.95}
        },
        "sentiment_trend": "increasing",
        "key_concerns": [],
        "positive_aspects": ["price", "location", "amenities"]
    }
]