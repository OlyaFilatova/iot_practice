from concurrent import futures

import grpc

from control_and_telemetry.grpc_python.dummy_pb2_grpc import DummyServiceServicer, add_DummyServiceServicer_to_server
from control_and_telemetry.grpc_python.dummy_pb2 import Empty, Dummy

class DummyService(DummyServiceServicer):
    def GetResponse(self, request, context):
        return Dummy(response="Called server successfully")

def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_DummyServiceServicer_to_server(DummyService(), server)

    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
