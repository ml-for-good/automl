import React from 'react';
import { useKeycloak } from '@react-keycloak/web'

function AuthButton() {
  const { keycloak } = useKeycloak();

  const handleLogInOut = () => {
    console.log(keycloak);
    console.log(keycloak.authenticated);

    if (keycloak.authenticated) {
      keycloak.logout();
    } else {
      keycloak.login();
    }
  }

  const handleButtonCaption = () => {
    if (!keycloak.authenticated) {
        return "Login";
    } else {
        return "Logout " + keycloak.tokenParsed.preferred_username;
    }
  }

  return(
    <div>
      <button
        onClick={() => handleLogInOut()}
      >
      {handleButtonCaption()}
      </button>
    </div>
  );
}

export default AuthButton;
