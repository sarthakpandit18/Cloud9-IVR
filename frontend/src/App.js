import logo from './logo.svg';
import './App.css';
import Signup from './components/Signup';
import Login from './components/Login';
import { Account, AccountContext } from './components/Account';

import Dashboard from './components/Dashboard';
import Status from './components/Status';
import { Route, Routes, BrowserRouter } from "react-router-dom";
import ResponsiveAppBar from './components/ResponsiveAppBar';
import { useContext, useState } from 'react';


function App() {
  
  return (
    // <Login/>
    
    <div className="App">
      <Account>

      
      <BrowserRouter>
      
    <ResponsiveAppBar/>
    <Routes>
    <Route exact path="/" element={<div/>} />
      <Route exact path="/login" element={<Login/>} />
      <Route exact path="/signup" element={<Account><Signup/></Account>} />
      <Route exact path="/dashboard" element={<Dashboard/>} />
    </Routes>
  </BrowserRouter>
  </Account>
      {/* <Account>
        <Status/>
      <Signup/>
      <Login/>
      </Account> */}
    </div>
  );
}

export default App;
