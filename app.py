from flask import Flask, request, jsonify
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

app = Flask(__name__)

# Load the preprocessed data from CSV
df = pd.read_csv('preprocessed_data (2).csv')

X = df.drop('music_genre', axis=1)  # Drop the target column to isolate features
y = df['music_genre']  # Target column with genres encoded from 0 to 9

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create an SVM classifier
svm_model = svm.SVC(decision_function_shape='ovr')

# Train the model
svm_model.fit(X_train, y_train)

# Create an RBF Kernel SVM classifier
rbf_svc = svm.SVC(kernel='rbf')
rbf_svc.fit(X_train, y_train)

# Create a Polynomial Kernel SVM classifier
# poly_svc = svm.SVC(kernel='poly', degree=3)
# poly_svc.fit(X_train, y_train)

@app.route('/get-prediction', methods=['POST'])
def get_prediction():
    try:
        # Get the CSV data from the request
        file = request.files['file']
        user_data = pd.read_csv(file)
        user_data = user_data.drop('music_genre', axis=1)

        # Make predictions using the loaded models
        svm_pred = svm_model.predict(user_data)
        rbf_pred = rbf_svc.predict(user_data)
        # poly_pred = poly_svc.predict(user_data)

        # Evaluate the models
        svm_report = classification_report(y_test, svm_model.predict(X_test), output_dict=True)
        rbf_report = classification_report(y_test, rbf_svc.predict(X_test), output_dict=True)
        # poly_report = classification_report(y_test, poly_svc.predict(X_test), output_dict=True)

        # Prepare the response
        response = {
            'svm_prediction': svm_pred.tolist(),
            'rbf_prediction': rbf_pred.tolist(),
            # 'poly_prediction': poly_pred.tolist(),
            'svm_report': svm_report,
            'rbf_report': rbf_report,
            # 'poly_report': poly_report,
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
