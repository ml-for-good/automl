# Authentication server
This is the authentication server which use keycloak as the server implementation

## How to run
https://www.keycloak.org/getting-started/getting-started-docker

`docker run -p 8080:8080 -e KEYCLOAK_ADMIN=admin -e KEYCLOAK_ADMIN_PASSWORD=admin quay.io/keycloak/keycloak:17.0.1 start-dev`

## How to setup the keycloak server using Api-call (Client credential grant type)
1. create a realme setting called: automl_dev
    - <img src="./imgs/1.png" width="60%"/>
2. import the `realm-export.json`
3. try: `GET http://localhost:8080/realms/automl_dev/.well-known/openid-configuration`
    - ```json
      {
          ...,
          "token_endpoint": "http://localhost:8080/realms/automl_dev/protocol/  openid-connect/token",
          ...
      }
      ```
4. try: `POST http://localhost:8080/realms/automl_dev/protocol/openid-connect/token`
    - with:  
        <img src="./imgs/2.png" width="60%"/>  
        where you can get client_id with the same name client, client_secret by  
        <img src="./imgs/3.png" width="60%"/> 
    - response:
        ```json
        {
            "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJMcEZLZE5lcGVsYk9RVlNqSTk4NnlFUHZpS2RWZ2FaNWY3V2tib2FGUFpzIn0.eyJleHAiOjE2NDg1NDMzNDUsImlhdCI6MTY0ODU0MzA0NSwianRpIjoiZTE4YjBiYjAtMjkxMy00MmZlLTk2MTYtZjIxZTE5MzE0MTg5IiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL3JlYWxtcy9hdXRvbWxfZGV2IiwiYXVkIjoiYWNjb3VudCIsInN1YiI6ImU1MTllMGUyLTIyOGItNDU3Ni05NWIyLWNjMTlhODQ3MmVhNiIsInR5cCI6IkJlYXJlciIsImF6cCI6ImF1dG9tbF9hcGkiLCJhY3IiOiIxIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIm9mZmxpbmVfYWNjZXNzIiwiZGVmYXVsdC1yb2xlcy1hdXRvbWxfZGV2IiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJjbGllbnRJZCI6ImF1dG9tbF9hcGkiLCJjbGllbnRIb3N0IjoiMTcyLjE3LjAuMSIsInByZWZlcnJlZF91c2VybmFtZSI6InNlcnZpY2UtYWNjb3VudC1hdXRvbWxfYXBpIiwiY2xpZW50QWRkcmVzcyI6IjE3Mi4xNy4wLjEifQ.GYeWctV0f3oI_iHxfs_SBUMWQJXYX3B0fjBPstQAe2hWBxjvJhQxDgF_hozDg0ljc2U-a_SUSkdyvAxvRbT30UJoaRkC6GNUG564vDStARq7sdxtZM_G3tIOldTqvIDB8CE2cfyYRxr9PqteG6CRMoKWOzBwNB9F_8e9CVQRvgUECcQHjf8_cGgaHb_55pzJuFUMKan7Vx4K9-FHBsFLAn0tapWGWq5ApZ0Ct92seWrxkYIAbYsIKU_Yut6yC62bgU49IcnWz2svbN0ON1-5q4CMkICFu7eeHWuQksd0KnBVEHH-MxoYNMQIXbsTmK5yYpJLFNmmRXFzN_OiqsD9OQ",
            "expires_in": 300,
            "refresh_expires_in": 0,
            "token_type": "Bearer",
            "id_token": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJMcEZLZE5lcGVsYk9RVlNqSTk4NnlFUHZpS2RWZ2FaNWY3V2tib2FGUFpzIn0.eyJleHAiOjE2NDg1NDMzNDUsImlhdCI6MTY0ODU0MzA0NSwiYXV0aF90aW1lIjowLCJqdGkiOiI4NmI2NmIwNC05Y2M2LTQzMjQtYTVhNS1iNGQ3NTdhYWM5NzIiLCJpc3MiOiJodHRwOi8vbG9jYWxob3N0OjgwODAvcmVhbG1zL2F1dG9tbF9kZXYiLCJhdWQiOiJhdXRvbWxfYXBpIiwic3ViIjoiZTUxOWUwZTItMjI4Yi00NTc2LTk1YjItY2MxOWE4NDcyZWE2IiwidHlwIjoiSUQiLCJhenAiOiJhdXRvbWxfYXBpIiwiYXRfaGFzaCI6IlNacng5NmZLZ3B6M3hpSVdOVWQ4S2ciLCJhY3IiOiIxIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJjbGllbnRJZCI6ImF1dG9tbF9hcGkiLCJjbGllbnRIb3N0IjoiMTcyLjE3LjAuMSIsInByZWZlcnJlZF91c2VybmFtZSI6InNlcnZpY2UtYWNjb3VudC1hdXRvbWxfYXBpIiwiY2xpZW50QWRkcmVzcyI6IjE3Mi4xNy4wLjEifQ.rwjGVYayI8pzLY1LQ4UJthiX_uJKMHG3jkVMJ8Mcmiruij9AYSY52RKgSFJh7xZJPFrxyTQvwzQVuxIBQFbTeMsSn8wZcNsXsoBcHMvERl6e8XgVOVIOGewhUpK3k5H64JBu2rXy6HHQ6lBr2h1Sxc7wNwtuGHrs6CmW11oiHcBsVSlKrtt3HjDywvek9Y1mrunVgAE9XGTEvKM8_OEFwlQPNvDncFmu16M-M80UuhqR4v9ql_8UGWgURKpeaCdgXIFWHip5Ji5OD8h7G3OHn2geo7zicHKkKtGThR8DdxcCgQ0PP8TwD7U9vwIMC5c4kkHLiaNwWXAeKusUDvyGKQ",
            "not-before-policy": 0,
            "scope": "openid profile email"
        }
        ```
5. Now, try `POST localhost:8081/dashboard` with `Authorzation = Bearer <jwt token (access_token) from the above api>`
    - <img src="imgs/4.png width="50%"/>

## How to setup the keycloak server using ui signin (Auth code grant type)
1. create a realme setting called: automl_dev
    - <img src="./imgs/1.png" width="60%"/>
2. import the `realm-export.json`
3. try: `GET http://localhost:8080/realms/automl_dev/.well-known/openid-configuration`
    - ```json
      {
          ...,
          "authorization_endpoint": "http://localhost:8080/realms/automl_dev/protocol/openid-connect/auth"
          ...
      }
      ```
4. try: `GET http://localhost:8080/realms/automl_dev/protocol/openid-connect/auth?...`
    - with  
    <img src="./imgs/5.png" width="80%"/>
    - Create a new user through KeyCloak admin console (`Users` on the left hand side)
        - After creation: visite `http://localhost:8080/realms/<realm-name>/account/` and try to signin with your user info
5. Copy the url in Postman
    - e.g.: `http://localhost:8080/realms/automl_dev/protocol/openid-connect/auth?client_id=automl_ui&response_type=code&scope=openid&redirect_uri=http://localhost:8081/hello&state=someRandomValue`
6. Type in your creaded user info (username + password)

## How to integrate Keycloak to frontend application (Auth code grant type with PKCE)
1. create a realme setting called: automl_dev
    - <img src="./imgs/1.png" width="60%"/>
2. import the `realm-export.json`
3. try: `GET http://localhost:8080/realms/automl_dev/.well-known/openid-configuration`
    - ```json
      {
          ...,
          "authorization_endpoint": "http://localhost:8080/realms/automl_dev/protocol/openid-connect/auth"
          ...
      }
      ```
4. try: `GET http://localhost:8080/realms/automl_dev/protocol/openid-connect/auth?...`
    - with  
    <img src="./imgs/5.png" width="80%"/>
    - Create a new user through KeyCloak admin console (`Users` on the left hand side)
        - After creation: visite `http://localhost:8080/realms/<realm-name>/account/` and try to signin with your user info
5. Give the user with USER role
    - <img src="./imgs/6.png" width="80%"/>
    - <img src="./imgs/7.png" width="80%"/>
6. ```bash
   cd my-auth-frontend
   npm install
   npm start
   ```
   Then you can sign in using your previously created user account through this ui to access some backend API as shown by the frontend application.
7. example screenshots:
    - initially:  
    <img src="./imgs/8.png" width="80%"/>
    - visite /hello  
    <img src="./imgs/9.png" width="80%"/>
    - signin:   
    <img src="./imgs/10.png" width="80%"/>
    - successful sigin and redirected to /dashboard  
    <img src="./imgs/11.png" width="80%"/>
    - visite /sample   
    <img src="./imgs/12.png" width="80%"/>

## trouble shooting
1. ["RESTEASY003210: Could not find resource for full path ..."](https://stackoverflow.com/a/71634718/18552929)

## helpful resource
- https://blog.logrocket.com/implement-keycloak-authentication-react/
- https://github.com/ivangfr/springboot-react-keycloak
