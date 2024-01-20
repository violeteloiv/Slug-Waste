import React from 'react';
import logo from './logo.svg';
import './Login.css';

function Login() {
  return (
    <div className="Login">
      <p id="login_title">Slug Waste Log-In</p>
      
      <form id="login_form" action="localhost:5000" method="POST">
        <p> username </p>
        <input type="username"/>
        <p> password </p>
        <input type="password"/>
        <input type="submit"/>
      </form>
    </div>
  );
}

export default Login;
