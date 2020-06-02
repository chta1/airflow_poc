To run this POC
1.  docker-compose -f docker-compose-CeleryExecutor.yml up
2.  Navigate to http://localhost:8080/
3.  Upload variables file : http://localhost:8080 -> Admin -> Variables
    a.  Key = settings
    b.  Val = { "login": "my_login", "password": "my_password", "config": { "role": "admin" } }
