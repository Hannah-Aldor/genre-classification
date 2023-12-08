from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

app = Flask(__name__)
CORS(app)

# Load the models
knn = joblib.load('./models/best_knn.pkl')
rbf_svm = joblib.load('./models/best_rbf_svm.pkl')
linear_svm = joblib.load('./models/best_linear_svm.pkl')


@app.route('/get-prediction', methods=['POST'])
def get_prediction():
    try:
        # Get the CSV data from the request
        file = request.files['file']
        filename = file.filename

        # Extract test set number
        i = filename.split('X_test_')[1]
        
        user_data = pd.read_csv(file)
        y_test = pd.read_csv(f'./test_datasets/y_test_{i}')

        # Get model predictions
        rbf_pred = rbf_svm.predict(user_data)
        knn_pred = knn.predict(user_data)
        linear_pred = linear_svm.predict(user_data)

        # Evaluate the models
        rbf_report = classification_report(y_test, rbf_pred, output_dict=True)
        knn_report = classification_report(y_test, knn_pred, output_dict=True)
        linear_report = classification_report(y_test, linear_pred, output_dict=True)

        # Prepare the response
        response = {
            'rbf_report': rbf_report,
            'knn_report': knn_report, 
            'linear_report': linear_report,
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000, threaded=True)
