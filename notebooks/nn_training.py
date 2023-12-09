import numpy as np
import pandas as pd

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report

df = pd.read_csv("../old_preprocessed_data.csv", header = 0)


X = df.drop(columns=["music_genre"])
y = df["music_genre"]

X_train, X_test = train_test_split(X, test_size=0.2, random_state=21)
y_train, y_test = train_test_split(y, test_size=0.2, random_state=21)

Optimal_Hyper_parameters =  {'activation': 'logistic', 'batch_size': 100, 'hidden_layer_sizes': (35, 35), 'learning_rate_init': 0.025, 'max_iter': 1000, 'solver': 'sgd'}
#Optimal Accuracy :  0.5882

def param_search():
    parameters =  {
        'activation': 'logistic',
        'batch_size': 50,
        'hidden_layer_sizes': (200, 100, 50, 35),
        'learning_rate_init': 0.005,
        'max_iter': 10000,
        'solver': 'sgd'
    }


    max_iterations = [4000]
    hidden_layer_siz = [(100, 100, 100, 10)]
    learning_rates = 0.005 * np.arange(5, 6)
    activations = ["logistic"]
    batch_sizes = [100]
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


mlp = MLPClassifier(**Optimal_Hyper_parameters)

mlp.fit(X_train, y_train)

Y_hat = mlp.predict(X_test)

report = classification_report(y_test, Y_hat, digits=4)
print(report)

#output
'''
              precision    recall  f1-score   support

           0     0.5919    0.6524    0.6207      1027
           1     0.7807    0.7448    0.7623       956
           2     0.5376    0.4952    0.5155      1040
           3     0.5241    0.3401    0.4125       991
           4     0.5227    0.6228    0.5684       981
           5     0.4722    0.3778    0.4198       990
           6     0.6193    0.4957    0.5506      1037
           7     0.5209    0.6846    0.5916       948
           8     0.8450    0.8309    0.8379      1017
           9     0.4628    0.6022    0.5234      1013

    accuracy                         0.5837     10000
   macro avg     0.5877    0.5846    0.5803     10000
weighted avg     0.5877    0.5837    0.5798     10000
'''
