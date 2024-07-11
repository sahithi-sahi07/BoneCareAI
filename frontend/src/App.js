import React from 'react';
import ImageUpload from './components/ImageUpload';
import PredictionResult from './components/PredictionResult';

function App() {
  const [result, setResult] = React.useState(null);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Bone Fracture Prediction</h1>
        <ImageUpload setResult={setResult} />
        {result && <PredictionResult result={result} />}
      </header>
    </div>
  );
}

export default App;
