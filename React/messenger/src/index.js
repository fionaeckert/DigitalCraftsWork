import React from 'react';
import ReactDOM from 'react-dom/client';
import './Messenger.css';
import reportWebVitals from './reportWebVitals';
import Messengers from './Messengers';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Messengers />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
