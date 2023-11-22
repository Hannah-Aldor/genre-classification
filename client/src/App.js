import { useState } from "react";
import Modal from "react-modal";

import './App.css';


function ModelPrediction({model, modalOpen, setModalOpen}) {
  return (
    <div>

    <ResponseModal data="1" modalOpen={modalOpen} setModalOpen={setModalOpen}>
    </ResponseModal>

    <details>
      <summary>Model {model}</summary>
      <span>*Prediction Report for model {model}*</span>
    </details>
    <button onClick={setModalOpen}>Show Report</button>
    </div>
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


function ResponseModal({data, modalOpen, setModalOpen}) {
  return <Modal
  isOpen={modalOpen}
  onRequestClose={() => setModalOpen(false)}
  className="response-modal"
  >
    <h1>Model predictions</h1>
    <div>
      <Column column_id={0}/>
      <Column column_id={1}/>
      <Column column_id={2}/>
      <Column column_id={3}/>
      <Column column_id={4}/>
    </div>
    <button onClick={() => setModalOpen(false)}>Close Modal</button>
  </Modal>
}


function App() {
  const [modalOpen, setModalOpen] = useState(false);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Genre Classification API</h1>
        <form>
          <span className="upload-label">Upload Input Data:</span>
          <input type="file" onChange={handleUpload}/>
        </form>
      </header>

      <div className="body-div">
        <div className="instruction-div floater">
          • This API interfaces with 3 classification models that predict genre based on
          popularity, acousticness, danceability, duration_ms, energy, instrumentalness,
          liveness, loudness, mode, speechiness, and valence.
          <br></br>
          <br></br>
          • Upload a CSV file containing columns for the features to interact with the API.
        </div>
        <div className="predictions floater">
          <ModelPrediction model="1" modalOpen={modalOpen} setModalOpen={setModalOpen}/>

        </div>

      </div>
      <ResponseModal />
      <div id="left"></div>
      <div id="right"></div>
      <div id="top"></div>
      <div id="bottom"></div>
    </div>
  );
}

export default App;
