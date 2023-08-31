First of all make sure project is set up and running on your local machine:
   1. Follow setup instructions in readme.md file

   2. Run project via command `python manage.py runserver`. By default, Django starts at host 127.0.0.1 and port 8000, but you can specify your own host and port by adding command-line argument, for example: `python manage.py runserver 0.0.0.0:8080`

Once project is running you have several options to create inventory (default host and port are used in the instructions below).
   1. Using built in browsable API. Go to http://127.0.0.1:8000/inventory/. You should see human-friendly HTML output with form to create inventory item. Please use data structure described below to send metadata.
   
   2. Using [curl](https://curl.se) command-line tool. Send the following data structure to inventory API url:
   
```
{
  "name": "string",
  "type": {
    "name": "string"
  },
  "language": {
    "name": "string"
  },
  "tags": [
    {
      "name": "string",
      "is_active": "boolean"
    }
  ],
  "metadata": {
    "year": "integer",
    "actors": ["string", ],
    "imdb_rating": "decimal",
    "rotten_tomatoes_rating": "integer",
  }
}
```
   Please note that all attributes in data structure above are mandatory.

   Example of creating inventory item: 
   
```
curl -X 'POST' \
  'http://127.0.0.1:8000/inventory/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "test_1",
  "type": {
    "name": "test_1"
  },
  "language": {
    "name": "test_1"
  },
  "tags": [
    {
      "name": "test_1",
      "is_active": true
    }
  ],
  "metadata": {
    "year": 2000,
    "actors": ["test_1"],
    "imdb_rating": 2.22,
    "rotten_tomatoes_rating": 5
  }
}'
```

If you have any questions regarding instructions described above please fill free to contact: