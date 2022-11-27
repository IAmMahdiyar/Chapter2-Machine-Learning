import sqlite3
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

n_users = 610
n_movies = 9724

def update_database(userId, movieId, doRecommend):
    con = sqlite3.connect("database.db")
    
    if doRecommend == 1.0:
        con.execute("INSERT INTO Predicts (MovieId, UserId, DoRecommend) VALUES (" + str(movieId) + "," + str(userId) +",TRUE)")
    
    elif doRecommend == 0.0:
        con.execute("INSERT INTO Predicts (MovieId, UserId, DoRecommend) VALUES(" + str(movieId) + "," + str(userId) + ",FALSE)")
    
    con.commit()

def get_all():
    con = sqlite3.connect("database.db")
    res = con.execute("SELECT * FROM Ratings")
    return res.fetchall()

def load_data():
    data = np.zeros([n_users, n_movies], dtype=np.float32)
    movie_id_mapping = {}

    for row in get_all():
        user_id = int(row[2]) - 1
        movie_id = int(row[1])
        rating = float(row[0])

        if movie_id not in movie_id_mapping:
            movie_id_mapping[movie_id] = len(movie_id_mapping)
        
        data[user_id, movie_id_mapping[movie_id]] = rating

    return data, movie_id_mapping


data, movie_id_mapping = load_data()

most_rated_movies = [318 ,296 ,593 ,2571 ,260 ,480 ,110 ,589 ,527 ,2959 ,1 ,1196 ,50 ,2858 ,47 ,780 ,150 ,1198 ,4993 ,1210]

for i in most_rated_movies:
    d = data
    X_raw = np.delete(d, movie_id_mapping[i], axis=1)
    Y_raw = d[:, movie_id_mapping[i]]
    
    X = X_raw[Y_raw > 0]
    Y = Y_raw[Y_raw > 0]

    recommend = 4
    Y[Y < recommend] = 0
    Y[Y >= recommend] = 1

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    nb = MultinomialNB(alpha=1.0, fit_prior=True)
    nb.fit(X_train, Y_train)

    predictaion = nb.predict(X_raw)

    print(i, len(predictaion))

    for j in range(1, len(predictaion)):
        update_database(userId=j, movieId=i, doRecommend=predictaion[j])