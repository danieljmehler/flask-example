# flask-example
Example of a python flask REST webapp.

## Run

```shell
export FLASK_APP=src.app.app
flask run
```

## Test

### Pytest

```shell
python -m pytest
```

### Manual Test
```shell
$ curl -v --data '{ "characters": [ { "name": "Severus Snape" } ] }' -H "Content-type: application/json" "http://localhost:5000/characters"
*   Trying 127.0.0.1:5000...
* Connected to localhost (127.0.0.1) port 5000 (#0)
> POST /characters HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.83.0
> Accept: */*
> Content-type: application/json
> Content-Length: 49
9:10 GMT
< Content-Type: text/html; charset=utf-8
< Content-Length: 0
< Connection: close
<
* Closing connection 0
```

Go to `http://localhost:5000/characters` to see the list of characters.
