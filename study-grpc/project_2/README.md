# gRPC guides key knowledge

This project showcases knowledge from gRPC documentation given at https://grpc.io/docs/guides/.

Its development is currently in progress.

## Running project

### Create virtual environment

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Changelog

- 

## Functionalities to implement

- based on knowledge acquired from guides so far
    - can add different types of authentication
    - can cancel RPC from client side (with server knowing and reacting) and from server side
    - can add compression logic with CRIME and BEAST attacks prevention.
    - can add timeout to protect client from waiting forever.
    - can attach channelz for debugging purposes and retrieve debug info.
    - can create rich error details and unpack them on client side.
    - can limit bandwidth on server and client sides.
    - can add health check service to a server, and react to it on the client side.

## Learninglog

- [2025/12/09](../learninglog/log_20251209.md)
- [2025/12/08](../learninglog/log_20251208.md)
