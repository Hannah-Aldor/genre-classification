from sklearn import svm, datasets
import sklearn.model_selection as model_selection
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

import pandas as pd

#iris = datasets.load_iris()
#X = iris.data[:, :2]
#y = iris.target

#X_train, X_test, y_train, y_test = model_selection.train_test_split(
#    X, y,
#    train_size=0.80,
#    test_size=0.20,
#    random_state=101
#)

df_pre = pd.read_csv("preprocessed_data.csv", header = 0)

df = df_pre[pd.to_numeric(df_pre["tempo"], errors="coerce").notnull()]
#df = df_pre[df_pre["tempo"].str.contains("?") == False]

train, test = train_test_split(df, test_size=0.2, random_state=21)
X_train, y_train = train.drop(columns=["instance_id", "artist_name", "track_name", "key", "obtained_date", "music_genre"]), train["music_genre"]
X_test, y_test = test.drop(columns=["instance_id", "artist_name", "track_name", "key", "obtained_date", "music_genre"]), test["music_genre"]

print(len(y_train))

print("starting training")

rbf = svm.SVC(kernel="rbf", gamma=0.5, C=0.1).fit(X_train, y_train)
print("training part 1 done")
poly = svm.SVC(kernel="poly", degree=3, C=1).fit(X_train, y_train)
print("training done")

poly_pred = poly.predict(X_test)
print("prediction part 1 done")
rbf_pred = rbf.predict(X_test)
print("prediction done")

poly_accuracy = accuracy_score(y_test, poly_pred)
print("accuracy done\n\n")

poly_f1 = f1_score(y_test, poly_pred, average="weighted")
print("Accuracy (Polynomial Kernel): ", "%.2f" % (poly_accuracy*100))
print("F1 (Polynomial Kernel): ", "%.2f" % (poly_f1*100))

rbf_accuracy = accuracy_score(y_test, rbf_pred)
rbf_f1 = f1_score(y_test, rbf_pred, average="weighted")
print("Accuracy (RBF Kernel): ", "%.2f" % (rbf_accuracy*100))
print("F1 (RBF Kernel): ", "%.2f" % (rbf_f1*100))


#print(type(iris))

