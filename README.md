# ECS 171 Group 29 Final Project

## Getting Started
1. Install the required project dependencies:
    - This project runs on Node `v20.9.0`, NPM `v10.1.0`, and Python `3.10.9`. Be sure `node -v`, `npm -v`, and `python --version` return the correct version numbers before moving on.   
    - In the project root directory, `$ npm install`.
    - In the `/client` directory, `$ npm install`.
2. Run the web app locally:
    - You must set the `FLASK_APP` and `FLASK_ENV` environment variables to `app.py` and `development` respectively. An example of doing this in Linux is `$ export FLASK_APP=app.py` and `$ export FLASK_ENV=development`.
    - In the project root directory, `$ npm start`. This starts up both the development client and server at the same time. Wait for the server to become available; the way you can tell is if you see the following output: `* Running on http://127.0.0.1:5000`.
    

## Interact With the Web App
1. Use any of the testing datasets in `/test_datasets` to pass to our models.
2. Click the 'Submit' button.
3. View the Classification Report for the three models on the web app.
