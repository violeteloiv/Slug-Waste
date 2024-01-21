import React from 'react';
import logo from './logo.svg';
import './Login.css';

function Login() {
  return (
    <div className="login">
      <form id="login_form" action="/login" method="POST">
        <h1>Login</h1>
        <input type="text" placeholder="Username" id="username" name="username"/>
        <input type="password" placeholder="Password" id="password" name="password"/>
        <input type="submit" id="submit"/>
      </form>
    </div>
  );
}

export default Login;
