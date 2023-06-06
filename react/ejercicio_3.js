//Conversor de temperatura
import React, { useState } from 'react';

const TemperatureConverter = () => {
  const [celsius, setCelsius] = useState('');
  const [fahrenheit, setFahrenheit] = useState('');

  const handleCelsiusChange = (event) => {
    const value = event.target.value;
    setCelsius(value);
    setFahrenheit(value !== '' ? (parseFloat(value) * 9) / 5 + 32 : '');
  };

  const handleFahrenheitChange = (event) => {
    const value = event.target.value;
    setFahrenheit(value);
    setCelsius(value !== '' ? ((parseFloat(value) - 32) * 5) / 9 : '');
  };

  return (
    <div>
      <h2>Conversor de Temperatura</h2>
      <div>
        <label>Temperatura en Celsius:</label>
        <input type="number" value={celsius} onChange={handleCelsiusChange} />
      </div>
      <div>
        <label>Temperatura en Fahrenheit:</label>
        <input type="number" value={fahrenheit} onChange={handleFahrenheitChange} />
      </div>
    </div>
  );
};

export default TemperatureConverter;
