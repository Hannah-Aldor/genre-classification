import numpy as np
import pandas as pd

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report

df = pd.read_csv("preprocessed_data.csv", header = 0)


X = df.drop(columns=["music_genre"])
y = df["music_genre"]

X_train, X_test = train_test_split(X, test_size=0.2, random_state=21)
y_train, y_test = train_test_split(y, test_size=0.2, random_state=21)

Optimal_Hyper_parameters =  {'activation': 'logistic', 'batch_size': 100, 'hidden_layer_sizes': (35, 35), 'learning_rate_init': 0.025, 'max_iter': 1000, 'solver': 'sgd'}
#Optimal Accuracy :  0.5882

'''
max_iterations = [1000, 2000]
hidden_layer_siz = [(35, 37), (35, 35)]
learning_rates = 0.005 * np.arange(5, 6)
activations = ["logistic"]
batch_sizes = [100, 50]
solvers = ["sgd"] # "lbfgs"

param_grid = dict(
    learning_rate_init = learning_rates,
    hidden_layer_sizes = hidden_layer_siz,
    max_iter = max_iterations,
    activation = activations,
    batch_size = batch_sizes,
    solver = solvers
)
mlp = MLPClassifier(
    solver = 'sgd',
    random_state = 42,
    activation = 'logistic',
    learning_rate_init = 0.025,
    batch_size = 100,
    hidden_layer_sizes = (35, 35),
    max_iter = 400
)


print("Grid search")
grid = GridSearchCV(estimator = mlp, param_grid = param_grid)

grid.fit(X, y)

print("Optimal Hyper-parameters : ", grid.best_params_)
print("Optimal Accuracy : ", grid.best_score_)
'''

mlp = MLPClassifier(**Optimal_Hyper_parameters)

mlp.fit(X_train, y_train)

Y_hat = mlp.predict(X_test)

report = classification_report(y_test, Y_hat, digits=4)
print(report)


