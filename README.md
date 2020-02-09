## Django Channels: Chatroom App
####  A Websocket implementation for a realtime chat app

##### Websockets: what is it?

Websockets (`ws://`) is a newer internet protocol designed for real-time
 communication. It is extremely performant by using persistent, open
 , bidirectional communication between the client-server.

##### What problem do websockets solve?

Previous internet protocols were centered around HTTP (`http://`) and were never
designed to accommodate real-time applications.  Hacks like long long-polling
http, and server side events(SSE) were plagued by low performance(slow), high
 overhead(computationally expensive) or high technical debt(hard to
  develop, maintain, debug).

##### Why would I not want to use websockets?
If your app/component/api doesn't require realtime bi-directional communication then HTTP(Ideally HTTP2) is still probably your best choice.  HTTP is very well supported across all programming languages and end-user clients. Websockets is still newer and may not be supported by legacy browers/clients and many languages outside javascript may have a hard time making use of it.


System Requirements:

- Ubuntu 18.0.x+(tested on 19.10)
- Python 3.8.x
    - Virtualenv
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

# navigate to http://127.0.0.1:8000/chat/lobby/ in your web browser; do the same in a second tab/window
# type a message
# see it in both chats in real time.
```
