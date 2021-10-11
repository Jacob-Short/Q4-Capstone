import './App.css';
import Navigation from "./components/Navigation";
import Index from "./views/HomePage";
import React from 'react';


function App() {
  return (
    <div className="App">
      <div>
        <Navigation />
        <Index />
      </div>
    </div>
  );
}

export default App;
