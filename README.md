# RECOMMENDATION-SYSTEM

COMPANY: CODTECH IT SOLUTIONS

NAME: YARLAGADDA SIRI CHANDANA

INTERN ID: CT06DL1154

DOMAIN: MACHNE LEARNING

DURATION: 6 WEEKS

MENTOR: NEELA SANTOSH

DESCRIPTION:

This implements a user-based collaborative filtering recommendation system that predicts user preferences by leveraging similarities between users’ past ratings. The main goal is to recommend new items that a user might like based on the tastes of similar users.

Importing Libraries and Loading Data:

The code starts by importing essential Python libraries:
pandas for data manipulation,
numpy for numerical computations,
cosine_similarity from scikit-learn for calculating similarity between users,
Next, it loads the ratings data from a CSV file named large_ratings.csv. This file contains records of user ratings for different items with three columns: user_id, item_id, and rating. Each row represents a single rating given by a user to an item.

Creating the User-Item Matrix:

Once the data is loaded, the script pivots the data frame to create a User-Item matrix. In this matrix:
Rows represent individual users,
Columns represent items,
The values are ratings that users gave to items.
If a user hasn’t rated an item, the value is set to zero (indicating missing rating). This matrix is crucial because it provides a structured format that allows easy comparison between users based on their rating patterns.

Calculating User Similarity Using Cosine Similarity:

To recommend items effectively, the system must understand which users have similar tastes. This is done by calculating the cosine similarity between each pair of users’ rating vectors.
Cosine similarity measures how closely aligned two rating vectors are by calculating the cosine of the angle between them.
Similar users will have similarity scores close to 1, indicating highly correlated tastes.
This step produces a User Similarity matrix, which is a square matrix where each entry shows how similar two users are.

Defining the Recommendation Function:

The core of the recommendation system is a function called recommend_best_item. This function:
Takes a specific user ID as input,
Identifies which items the user hasn’t rated yet (items with a rating of zero),
For each unrated item, it predicts a score that estimates how much the user might like that item.
To predict this score, the function:
Looks at other users’ ratings for the item,
Weights these ratings by how similar those users are to the target user,
Computes a weighted average rating as the predicted score.
This method uses the intuition that similar users’ opinions are more valuable when estimating preferences.

Selecting and Printing the Best Recommendation:

After calculating predicted scores for all unrated items, the function:
Finds the item with the highest predicted score,
Prints that item as the top recommendation for the given user.
If no recommendations can be made (e.g., the user has rated all items or there is insufficient data), it gracefully notifies that no recommendation is available.

Running the Recommendation:

This ends by calling this recommendation function for a specific user ID (e.g., user_id=2). It outputs the item ID and predicted rating score of the best item recommended for that user.

Conclusion

This implements a basic user-based collaborative filtering recommendation system using Python. By calculating user similarities with cosine similarity, it provides personalized item recommendations based on past ratings. This simple yet effective approach can be further expanded for larger datasets and improved accuracy, making it a great starting point for recommendation system development.

OUTPUT:

![Image](https://github.com/user-attachments/assets/6261c849-d7d5-44b8-a4f7-04e6b5e51d1f)
