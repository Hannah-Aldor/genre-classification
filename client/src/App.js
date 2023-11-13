import { useState } from "react";

import logo from './logo.svg';
import './App.css';


function ModelPrediction({model}) {
  return (
    <details>
      <summary>Model {model}</summary>
      <span>*Prediction Report for model {model}*</span>
  </details>
  )
}

function handleUpload(event) {
  const file = event.target.files[0];
  console.log(file.name);
}

function Column({column_id}) {
  return <div className="column">
    <h2>Name {column_id}</h2>
    <p>...</p>
    <p>data</p>
    <p>...</p>
  </div>
}


function ResponseModal({data}) {
  return <div className="response-modal">
    <h1>Model predictions</h1>
    <div>
      <Column column_id={0}/>
      <Column column_id={1}/>
      <Column column_id={2}/>
      <Column column_id={3}/>
      <Column column_id={4}/>
    </div>
  </div>
}


function App() {
  const [modalOpen, setModalOpen] = useState(false);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Genre Classification API</h1>
        <form>
            <span className="upload-label">Upload Input Data</span>
            <input type="file" onChange={handleUpload}/>
      </form>
      </header>

      <div className="body-div">
        <div className="intruction-div floater">
          This API interfaces with 3 classification models that predict genre based on
          popularity, acousticness, danceability, duration_ms, energy, instrumentalness,
          liveness, loudness, mode, speechiness, and valence.

          Upload a CSV containing columns for the features to interact with the API.
        </div>

        <div className="predictions floater">
          <ModelPrediction model="1"/>
          <ModelPrediction model="2"/>
          <ModelPrediction model="3"/>
        </div>

      </div>


      <ResponseModal/>



    </div>
  );
}

export default App;
