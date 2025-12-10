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

## gRPC Functionalities to implement

- add different types of authentication
- cancel RPC from client side (with server knowing and reacting) and from server side
- add compression logic with CRIME and BEAST attacks prevention.
- add timeout to protect client from waiting forever.
- attach channelz for debugging purposes and retrieve debug info.
- create rich error details and unpack them on client side.
    - use good status codes
- limit bandwidth on server and client sides.
- add health check service to a server, and react to it on the client side.
- send metadata at the start of request or response, or at the end of sending response and read metadata on the other side.
- add keepalive for improving performance and reliability.
- use interceptors to create logic that is not specific to a single RPC method.
- add reflection to make API specs publicly available
- add observability using OpenTelemetry plugin
- add retry policy
- stop server gracefully
- make client wait for server
- use uds
- use multiprocessing
- use xds
- run project in two separate Docker instances

## Learninglog

- [2025/12/10](../learninglog/log_20251210.md)
- [2025/12/09](../learninglog/log_20251209.md)
- [2025/12/08](../learninglog/log_20251208.md)
