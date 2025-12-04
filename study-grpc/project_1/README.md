This project based on examples given in gRPC documentation.

I'm updating it while reading docs.

## Setup

### Create virtual environment

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Start server

`python python/device_management_server.py`

### Run client

`python python/device_management_client.py`

### Update after proto edit

from project_1 folder run:

`python -m grpc_tools.protoc -I=./protos --python_out=./python/ --pyi_out=./python/ --grpc_python_out=./python/ ./protos/device_management.proto`

### Changelog

[2025/12/04](./changelog/log_20251204.md)