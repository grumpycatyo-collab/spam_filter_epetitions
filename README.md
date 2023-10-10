# Description
Spam Filter is a microservice made specifically for the E-petitions Project made in Go. Due to special needs (NLP + AI), we decided to stop on Python and implement a Web Socket type connection with the frontend.

## Contents
- [Conventions](#conventions)
- [Run Project](#runproject)
- [Usages](#usages)
  
## Conventions
Spam Filter is developed to use the Web Sockets, thus to try it, just connect to Postman and initialize the web-socket route

## Run Project
- Navigate to `app.py`
- Run the file
- Open Postman and choose web-socket connection
- Type in: `ws://localhost:8567`
- Push 'Connect' and good to go.

## Usages
There are two main functionalities that can be found in `src`. First one is censoring (finding the uncesored words) and
second one is grammar correction.

```python
from src.censore.censore_main import check_censoring

seq = "I don't know why but I am filling shitty today"
print(check_censoring(seq))
```
```
['shitty']
```
