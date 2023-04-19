# Introduction

This project runs a full API REST connected to a MySQL using Docker-compose.

- [Models](#models)
- [API endpoints](#api-endpoints)
- [Dependencies](#dependencies)
- [Run Project](#run-project)
    - [Successful](#successful)
    - [Create table](#create-table)
- [Credentials](#credentials)


# Models

**Games model**
| #id   | #name | #description | #price |
| :---: | :---: | :---: | :---: |
| integer   | varchar  | varchar   | decimal   |


# API endpoints

The allowed methods are:
 - GET -> `/games` or `games/<game_id>`
 ```json
 [GET] /games
 Response
 {
    "games": [
        [
            1,
            "Counter Strike",
            "Shooter",
            "64.99"
        ],
        [
            2,
            "Assassins Creed I",
            "Altair history",
            "32.99"
        ]
    ]
}
 ```
 - POST -> `/save_game`
 ```json
 [POST] /save_game/
 Body
 {
        "name": "Rubik",
        "description": "Magic cube",
        "price": "7.99"
 }
 ```
 - PUT -> `/update_game/<id>`
 ```json
 [PUT] /update_game/2
 Body
 {
        "name": "Assassins Creed I",
        "description": "Altair history",
        "price": "40.99"
 }
 ```
 - DELETE -> `/delete_game/<id>`
 ```json
 [DELETE] /delete_game/2
 ```

# Dependencies

For this project the tools needed are Docker

Follow this [guide to install Docker on Mac](https://docs.docker.com/desktop/install/mac-install/)

Also it is required to install docker-compose.
```
pip install docker-compose
```


# Run project

You can build and run containers all at once with this command.
```
docker-compose up --build
```

To check if the containers are running run this command in a separete tab/window
```
docker ps
```

You should see 3 process running
```bash
CONTAINER ID   IMAGE                   COMMAND                  CREATED        STATUS         PORTS                                                  NAMES
3d178931d951   phpmyadmin/phpmyadmin   "/docker-entrypoint.…"   19 hours ago   Up 5 seconds   0.0.0.0:8080->80/tcp, :::8080->80/tcp                  flask_db_admin_1
0267919a7478   flask_app               "python app.py"          19 hours ago   Up 6 seconds   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp              flask_app_1
9817ba23ec46   mysql                   "docker-entrypoint.s…"   19 hours ago   Up 6 seconds   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   flask_db_1
```

## Successful
1. Go to http://localhost:5000/
2. You should see `Hello World!`


## Create table

Once the containers are running it necessary to create the `games` table in the MySQL.
There is an admin panel running in the 8080 PORT.

1. Go there using http://localhost:8080/
2. Select `test-db` on the left pannel
3. Select the `SQL` tab
4. Paste and run the following sentence
```SQL
CREATE TABLE games(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    price DECIMAL(9,2) NOT NULL
);
```
5. (Optional) in case you want to add initial data execute this sentence
```SQL
INSERT INTO games(name, description, price)
VALUES 
    ("Counter Strike", "Shooter", 64.99),
    ("Assassins Creed I", "Altair history", 32.99);
```


# Credentials
By default the credentials are located in `export_credentials.sh` script

To export credentials to the current shell run
*_Note: Replace this credentials for security._*
```
source bin/export_credentials.sh
```

In case the script is not executable run
```
chmod +x bin/export_credentials.sh
```
