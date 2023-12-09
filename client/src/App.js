import { useState } from 'react';
import Modal from 'react-modal';
import axios from 'axios';

import './App.css';


function ModelPrediction({data, model, modalOpen, setModalOpen}) {
  console.log(`Data for model ${model}:`, data); // Debugging line

  return (
    <div>
      <ResponseModal data={data} model={model} modalOpen={modalOpen} setModalOpen={setModalOpen}/>
      <details>
      <summary>Model {model}</summary>
      <span>*Prediction Report for model {model}*</span>
    </details>
    <button onClick={setModalOpen}>Show Report</button>
    </div>
  )
}

function Column({column_id}) {
  return <div className="column">
    <h2>Name {column_id}</h2>
    <p>...</p>
    <p>data</p>
    <p>...</p>
  </div>
}

function ResponseModal({ data, modalOpen, setModalOpen }) {
  const renderOtherKeys = (data) => {
    const otherKeys = ['accuracy', 'macro avg', 'weighted avg'];
    return (
      <ul>
        {otherKeys.map(key => (
          <li key={key}>
            <strong>{key.replace(' avg', ' Average').replace('_', ' ').toUpperCase()}:</strong> {typeof data[key] === 'object' ? JSON.stringify(data[key], null, 2) : data[key]}
          </li>
        ))}
      </ul>
    );
  };

  const int_to_genre = {
    0: 'Electronic',
    1: 'Anime',
    2: 'Jazz',
    3: 'Alternative',
    4: 'Country',
    5: 'Rap',
    6: 'Blues',
    7: 'Rock',
    8: 'Classical',
    9: 'Hip-Hop'
  }

  return (
    <Modal
      isOpen={modalOpen}
      onRequestClose={() => setModalOpen(false)}
      className="response-modal"
    >
      <h1>Model predictions</h1>
      {data ? (
        <div className="modal-inner-container">
          {/* Table for the data */}
          <table>
            <thead>
              <tr>
                <th>Label</th>
                <th>F1-Score</th>
                <th>Precision</th>
                <th>Recall</th>
              </tr>
            </thead>
            <tbody>
              {Object.entries(data).filter(([key]) => !isNaN(key)).map(([key, values]) => (
                <tr key={int_to_genre[key]}>
                  <td>{int_to_genre[key]}</td>
                  <td>{values['f1-score']}</td>
                  <td>{values.precision}</td>
                  <td>{values.recall}</td>
                </tr>
              ))}
            </tbody>
          </table>

          {/* List for other keys */}
          <>
            {renderOtherKeys(data)}
          </>
        </div>
      ) : (
        <p>No data available</p>
      )}
      <button onClick={() => setModalOpen(false)}>Close Modal</button>
    </Modal>
  );
}





function App() {
  // const [modalOpen, setModalOpen] = useState(false);
  const [rbfModalOpen, setRBFModalOpen] = useState(false);
  const [linearModalOpen, setLinearModalOpen] = useState(false);
  const [knnModalOpen, setKNNModalOpen] = useState(false);

  const [modelNo, setModelNo] = useState(0);
  const [uploadedFile, setUploadedFile] = useState(null);
  const [predictionData, setPredictionData] = useState(null);

  async function handleSubmit(e) {
    e.preventDefault();
    
    const fileInput = document.getElementById('fileInput');
    if (!fileInput || !fileInput.files || fileInput.files.length === 0) {
      alert('Please upload a file before submitting!');
      return;
    }
  
    const file = fileInput.files[0];

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('http://localhost:5000/get-prediction', {
          method: 'POST',
          body: formData, // Send the FormData object
          // Don't set Content-Type header, let the browser set it
      });

      if (response.ok) {
          const responseData = await response.json();
          setPredictionData((old) => responseData);
          console.log(responseData);

      } else {
          console.error('Upload failed:', response.statusText);
      }
    }
    catch (error) {
      console.error('Error during file upload:', error);
    }
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>Genre Classification API</h1>
        <form onSubmit={handleSubmit}>
          <span className="upload-label">Upload Input Data:</span>
          <input type="file" id="fileInput"/>
          <button type="submit">Submit</button>
        </form>
      </header>

      <div className="body-div">
        <div className="instruction-div floater">
          • This API interfaces with 3 classification models that predict music genre based on
          popularity, acousticness, danceability, duration (ms), energy, instrumentalness,
          liveness, loudness, speechiness, and valence.

          <br></br>
          <br></br>
          • To interact with the API, upload one of the X_test_i.csv files in the `test_datasets` folder within
          the project root folder. Click `Submit`, and view the classification report for any of the three models
          with `Show Report`.
        </div>
        
        <div className="predictions floater">
          <ModelPrediction data={predictionData?.linear_report} model="Linear SVM" modalOpen={linearModalOpen} setModalOpen={setLinearModalOpen}/>
          <ModelPrediction data={predictionData?.rbf_report} model="RBF Kernel SVM" modalOpen={rbfModalOpen} setModalOpen={setRBFModalOpen}/>
          <ModelPrediction data={predictionData?.knn_report} model="K Nearest Neighbors" modalOpen={knnModalOpen} setModalOpen={setKNNModalOpen}/>
        </div>

      </div>
      <ResponseModal data={predictionData} model={modelNo}/>
    </div>
  );
}

export default App;
