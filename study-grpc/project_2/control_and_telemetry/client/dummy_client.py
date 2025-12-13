import os
import grpc
from control_and_telemetry.grpc_python.dummy_pb2_grpc import DummyServiceStub
from control_and_telemetry.grpc_python.dummy_pb2 import Empty 

def run():
    default_path = "http://localhost:50051"
    backend_url = os.getenv('BACKEND_URL', default_path)
    with grpc.insecure_channel(backend_url) as channel:
        stub = DummyServiceStub(channel)
        print(stub.GetResponse(Empty()))

if __name__ == "__main__":
    run()