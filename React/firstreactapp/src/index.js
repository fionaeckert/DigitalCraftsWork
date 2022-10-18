import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import reportWebVitals from './reportWebVitals';
// import Counter from './Counter';
// import FunctionalCounter from './FunctionalCounter';
// import Status from './components/Status';
// import BrandExample from './components/navbar'; 
// import Minesweeper from './components/Minesweeper';
// import Jokes from './Jokes'
import App from './App'

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App/>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
