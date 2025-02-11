Sample CURL Request 

curl -X POST http://127.0.0.1:8000/api/token/ \
     -H "Content-Type: application/json" \
     -d '{"username": "your_username", "password": "your_password"}'


curl -X GET http://127.0.0.1:8000/tasks/ \
     -H "Authorization: Token <ur Token>"



curl -X POST http://127.0.0.1:8000/tasks/ \
     -H "Authorization: Token <ur Token>" \
     -H "Content-Type: application/json" \
     -d '{"title": "New Task", "description": "Complete this task", "assigned_to": 2,"assigned_by": 3 }'
