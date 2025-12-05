# gRPC python key knowledge

This project showcases knowledge from gRPC documentation given at https://grpc.io/docs/languages/python/.

## Running project

### Create virtual environment

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Start server

`python -m device_controller.server.entrypoint`

### Run client

`python -m device_controller.client.entrypoint`

## Update after proto edit

`python -m grpc_tools.protoc -Idevice_controller/grpc_python=device_controller/protos --python_out=. --grpc_python_out=. --pyi_out=. device_controller/protos/device_controller.proto`

## Changelog

- [2025/12/05](./changelog/log_20251205.md)
- [2025/12/04](./changelog/log_20251204.md)

## Learninglog

- [2025/12/05](../learninglog/log_20251205.md)
- [2025/12/04](../learninglog/log_20251204.md)
- [2025/12/03](../learninglog/log_20251203.md)
