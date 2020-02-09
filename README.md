## Django Channels: Chatroom App
####  A Websocket implementation for a realtime chat app

##### Websockets: what is it?

Websockets (`ws://`) is a newer internet protocol designed for real-time
 communication. It is extremely performant through use of persistent, open
 , bidirectional communication between the client-server.

##### What problem do websockets solve?

Previous internet protocols were centered around HTTP (`http://`) and were never
designed to accommodate real-time applications.  Hacks like long long-polling
http, and server side events(SSE) were either low performance(slow), high
 overhead(computationally expensive) or highly complex to implement(hard to
  develop, maintain, debug).

##### Why would I not want to use websockets?
TODO:


System Requirements:

- Ubuntu 18.0.x+(tested on 19.10)
- Python 3.8.x
    - Poetry
    - Django 3.0.x
        - Django Channels
- Docker


### Setup and running:

```
# clone the repo
git clone repo && cd repo

# create a python virtualenv and activate it
virtualenv -p python3.8 venv && source venv/bin/activate

# install the dependencies from pyproject.toml with poetry
poetry install

# start a redis instance from docker
docker run -p 6379:6379 redis:2.8

# start the server
python manage.py runserver

# navigate to http://127.0.0.1:8000/chat/lobby/ in your web browser
```
