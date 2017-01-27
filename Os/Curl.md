GET:
curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://hostname/resource

Create:
curl -XPOST -H "Content-type: application/json" -d '{"project_name":"My Project", "project_description":"The original description"}' http://localhost:8000/projects/

Update:
curl -XPATCH -H "Content-type: application/json" -d '{"project_name":"A new name"}' http://localhost:8000/project/1/

OR
PUT
curl -XPUT -H "Content-type:application/json" -d '{"project_name":"A new name", "project_description":"The original description"}' http://localhost:8000/project/1/

Delete:
curl -XDELETE http://localhost:8000/project/1/
