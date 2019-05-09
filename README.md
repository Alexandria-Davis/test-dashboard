# Test Automation Dashboard
Prerequisites via docker-compose:
- Download MySQL database: https://www.mysql.com/downloads/
- Install Docker-compose on your device: ‘https://docs.docker.com/install/’
- Download should be Docker Desktop download

Prerequisites via manual:
- Node JS
- Other dependencies can be found at ‘https://angular.io/guide/quickstart’

Setting up MySQL (needs to be set up manually) :
- Create a MySQL Database. (The dashboard will set up the tables).
- The user will need read and write access into the particular schema, but may safely be rejected access to parts of the database.
-  Enter MySQL database connection information into python/flaskFiles/config.py
    - The config file requires a database schema name, database schema host, user, and password.
    - Due to how Docker handles routing, if the MySQL server is on the same server as the flask server, then the full hostname of the machine should still be used.

Configuring Angular:
- Set the URL of the flask server in test-dashboard/src/app/tests.service.ts
Clients will be attempting to reach the flask server at this URL, so do not set it to “localhost”!

Running both Angular and Flask Servers:
- If this is the first time the code has been run, or if there have been any changes, Run:
```  
Docker-compose build; docker-compose up;
```
on root project folder.

- If this gives no errors then skip ‘Running Flask file’ and ‘Running Angular web service’
- If this is not the first time running the dashboard, you can run docker-compose up on its own to save time.

Running Flask File:
- Make sure to be in the directory test-dashboard/python/flaskFiles
    -
    ```
    pip install -r requirements.txt
    ```
    - Run
    ```
    flask run
     ```
    - URL to view flask information : http://127.0.0.1:5000/

Parsing XML File:
- To tell the Flask server to parse files, upload them on the main page of the flask server. (This is served on port 5000)
- The flask server can accept multiple files at once, and will return a Json object when it has completed.

Running Angular web service:
- Make sure you are in the directory <test-dashboard/test-dashboard>
    - Make sure you have angular dependencies downloaded:
        - Node js
        - Other dependencies can be found at ‘https://angular.io/guide/quickstart’
    - Write command
    ```
     ng -o serve
     ```
    - This shall open up the web service for you
