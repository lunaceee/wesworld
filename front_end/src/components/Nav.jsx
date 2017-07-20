import React, { Component } from 'react';
import logo from "../static/css/images/binocular.svg"

class Nav extends Component {
	render(){
		return(
			<div className="Nav">
					<img src={logo} className="App-logo" alt="logo"/>
					<div>
						<button>Register</button>
						<button>Log in</button>
					</div>
			</div>
		);
	}
}

export default Nav;