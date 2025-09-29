import json
import pandas as pd
from functions import (
    aggregate_user,
    compute_composite,
    categorize_lead,
    aggregate_keywords,
    top_keywords,
    generate_recommendation_ai
)

with open("data.json") as f:
    data = json.load(f)

df = pd.DataFrame(data)
df["timestamp"] = pd.to_datetime(df["timestamp"])

agg_df = df.groupby("user_id").apply(aggregate_user).reset_index()
max_eng = df.groupby("user_id")["engagement"].mean().max()

agg_df["composite_score"] = agg_df.apply(lambda row: compute_composite(row, max_eng), axis=1)
agg_df["lead_category"] = agg_df.apply(categorize_lead, axis=1)

agg_df["keywords"] = df.groupby("user_id").apply(aggregate_keywords).values
agg_df["top_keywords"] = agg_df["keywords"].apply(top_keywords)

agg_df["recommendation"] = agg_df.apply(generate_recommendation_ai, axis=1)

pd.set_option('display.max_colwidth', None)
print(agg_df[["user_id", "composite_score", "lead_category", "recommendation"]])
