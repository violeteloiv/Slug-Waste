import React from 'react';
import logo from './logo.svg';
import './Login.css';

function Login() {
  return (
    <div className="Login">
      <p id="login_title">Slug Waste Log-In</p>
      
      <form id="login_form" action="/login" method="POST">
        <p> username </p>
        <input type="username" name="username"/>
        <p> password </p>
        <input type="password" name="password"/>
		<br/>
        <input type="submit"/>
      </form>
    </div>
  );
}

export default Login;
