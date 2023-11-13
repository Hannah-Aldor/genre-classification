import logo from './logo.svg';
import './App.css';

const NUMBER_OF_INPUTS = 11;

function InputField() {
  return (
    <input className="inputField" />
  );
}

function Fields() {
  return (
    <div>
      <div className="SameLine">
        <FieldLabel text="Popularity"/>
        <FieldLabel text="acousticness"/>
        <FieldLabel text="danceability"/>
        <FieldLabel text="duration_ms"/>
        <FieldLabel text="energy"/>
        <FieldLabel text="instrumentalness"/>
        <FieldLabel text="liveness"/>
        <FieldLabel text="loudness"/>
        <FieldLabel text="mode"/>
        <FieldLabel text="speechiness"/>
        <FieldLabel text="valence"/>
      </div>
      
      <br/>

      <div className="SameLine">
        {Array(NUMBER_OF_INPUTS).fill(<InputField />)}
      </div>
    </div>
  )
}

function FieldLabel({text}) {
  return (
    <div className="LabelDiv SameLine">
      <label className="FieldLabel">{text}</label>
    </div>
  )
}




function ModelPrediction({model}) {
  return (
    <details>
      <summary>Model {model}</summary>
      <span>*Prediction Report for model {model}*</span>
  </details>
  )
}





function App() {
  return (
    <div className="App">
      <header className="App-header">
        Genre Classification API
        <form>
          <h1>Upload Input Data</h1>
          <input type="file" />
          <button type="submit">Upload</button>
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

    </div>
  );
}

export default App;
