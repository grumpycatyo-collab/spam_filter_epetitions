# Description
Spam Filter is a microservice made specifically for the E-petitions Project made in Go. Due to special needs (NLP + AI), we decided to stop on Python and implement a Web Socket type connection with the frontend.

## Contents
- [Conventions](#conventions)
- [RPC Methods](#rpc-methods)
- [Login](#login)
- [RefreshSession](#refreshsession)
- [ValidateToken](#validatetoken)
- [SendOTP](#sendotp)
- [ValidateOTP](#validateotp)

## Conventions
Spam Filter is developed to use the Web Sockets, thus to try it, just connect to Postman and initialize the web-socket route
