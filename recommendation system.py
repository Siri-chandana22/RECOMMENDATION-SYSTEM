import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
df = pd.read_csv('large_ratings.csv')  
print("Original Ratings Data:")
print(df.head())
user_item_matrix = df.pivot(index='user_id', columns='item_id', values='rating').fillna(0)
print("\n User-Item Matrix:")
print(user_item_matrix.head())
user_similarity = pd.DataFrame(
    cosine_similarity(user_item_matrix),
    index=user_item_matrix.index,
    columns=user_item_matrix.index
)
print("\n User Similarity Matrix:")
print(user_similarity.round(6).head())
def recommend_best_item(user_id, user_item_matrix, user_similarity):
    sim_scores = user_similarity[user_id]
    user_ratings = user_item_matrix.loc[user_id]
    unrated_items = user_ratings[user_ratings == 0].index
    scores = {}
    for item in unrated_items:
        item_ratings = user_item_matrix[item]
        mask = item_ratings > 0
        relevant_sims = sim_scores[mask]
        relevant_ratings = item_ratings[mask]
        if relevant_sims.sum() > 0:
            scores[item] = np.dot(relevant_sims, relevant_ratings) / relevant_sims.sum()
    if scores:
        top_item = max(scores, key=scores.get)
        print(f"\n Top Recommendation for User {user_id}:")
        print(f" item_id\n{top_item}    {scores[top_item]:.5f}")
    else:
        print(f"\n No recommendations available for User {user_id}.")
recommend_best_item(user_id=2, user_item_matrix=user_item_matrix, user_similarity=user_similarity)
