import React from 'react';
import logo from '../tarot.jpeg'; // Tell webpack this JS file uses this image
import './TarotImage.css'

function TarotImage() {
  // Import result is the URL of your image
  return <img src={logo} alt="Logo" />;
}

export default TarotImage;