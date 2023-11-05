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


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <Fields/>
      </header>
    </div>
  );
}

export default App;
