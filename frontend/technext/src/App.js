import logo from './logo.svg';
import './App.css';
import React, { useContext, useEffect, useState } from 'react';
import { getPatentResults } from "./PatentSearch"; 

function App() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);


  function handleInput(e) {
    setQuery(e.target.value);
  }

  const fetchResults = () => {
    getPatentResults(query).then((data) => {
      setResults(data.results);
    });

  } 

  return (
    <div>
      <header>
        <label>
            Patent Search:
            <input value={query} onChange={handleInput}/>
        </label>
        <button onClick={fetchResults}>Submit</button>
      </header>
      <div>
      <ul>
        {results.map(data => (
          <li key={data.patent_id}> {data.patent_id}</li>
        ))}
      </ul>
        
      </div>
    </div>
  );
}

export default App;
