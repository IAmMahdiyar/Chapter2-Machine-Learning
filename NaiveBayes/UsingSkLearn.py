from sklearn.naive_bayes import BernoulliNB
import numpy as np

X_train = np.array([
[0, 1, 1],
[0, 0, 1],
[0, 0, 0],
[1, 1, 0]])

Y_train = ['Y', 'N', 'Y', 'Y']

X_test = np.array([[1, 1, 0]])

nb = BernoulliNB(alpha=1.0, fit_prior=True)

nb.fit(X_train, Y_train)

print(nb.predict_proba(X_test))