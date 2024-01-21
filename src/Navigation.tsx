import React from 'react';
import logo from './logo.svg';

import "./Navigation.css"

function Navigation() {
  return (
    <div>
		<nav className="navbar">
			<h1 id="title">SlugWaste</h1>
			<ul id="nav-links">	
				<div className="menu">
					<li><a href="/submission">Submission</a></li>
					<li><a href="/data">Data</a></li>
					<li><a href="/analyze">Analyze</a></li>
				</div>
			</ul>
		</nav>
	</div>
  );
}

export default Navigation;
