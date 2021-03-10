# Fast API for Learn consume API

### Setting Up a Project

Install :
```
pip install redis sqlalchemy pymysql pandas fastapi uvicorn python-dotenv pymongo sockets requests
```

Import database :

using ```db.sql``` in this project
Setting your ```database``` connection in ```.env``` file

### Deploy up a Project on Docker
```docker build -t <IMAGE-NAME> <PATH-PROJECT>```

make sure ```.env``` or ```ENV Dockerfile``` is correct and connected to the same network as the database 