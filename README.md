#### # To run this POC
1.  docker-compose -f docker-compose-CeleryExecutor.yml up
2.  Navigate to http://localhost:8080/
3.  Create variables
	a.  Navigate to : Admin -> Variables
	b.  Key = settings
	c.  Val = { "login": "my_login", "password": "my_password", "config": { "role": "admin" } }
4.  To Run a DAG
	a.  Navigate to : DAGs
	b.  Toggle the desired DAG to On
	c.  Click on the DAG
	d.  Trigger DAG
	e.  Go to Graph View
	f.  Click on the task and View Log
