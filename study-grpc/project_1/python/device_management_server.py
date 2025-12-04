from concurrent import futures
import logging

import grpc
import device_management_pb2_grpc
import device_management_pb2

class CustomException(Exception):
    """Custom exception to test gRPC behavior"""
    custom_param = "Some custom param"

class Register(device_management_pb2_grpc.DeviceManagerServicer):
    def RegisterDevice(self, request, context):
        # raise Exception('Whoops! something weng wrong!')
        # # Client receives grpc._channel._InactiveRpcError with
        # # status = StatusCode.UNKNOWN
        # # details = "Exception calling application: Whoops! something weng wrong!"
        # # debug_error_string = "UNKNOWN:Error received from peer  {grpc_status:2, grpc_message:"Exception calling application: Whoops! something weng wrong!"}"

        # # Serves sees following error and is still usable:
        # # ERROR:grpc._server:Exception calling application: Whoops! something weng wrong!
        # # Traceback (most recent call last):
        # # ...
        # # File ".../iot_practice/study-grpc/project_1/from_docs/helloworld/greeter_server.py", line 26, in SayHello
        # # raise Exception('Whoops! something weng wrong!')
        # # Exception: Whoops! something weng wrong!

        # raise CustomException('Other error!.', 43)
        # # Client sees:
        # # grpc._channel._InactiveRpcError: <_InactiveRpcError of RPC that terminated with:
        # # status = StatusCode.UNKNOWN
        # # details = "Exception calling application: ('Other error!.', 43)"
        # # debug_error_string = "UNKNOWN:Error received from peer  {grpc_message:"Exception calling application: (\'Other error!.\', 43)", grpc_status:2}"
        # # >

        # # # Server sees:
        # # ERROR:grpc._server:Exception calling application: ('Other error!.', 43)
        # # Traceback (most recent call last):
        # # ...
        # # File ".../iot_practice/study-grpc/project_1/from_docs/helloworld/greeter_server.py", line 43, in SayHello
        # # CustomException: ('Other error!.', 43)
        return device_management_pb2.DeviceResponse(success=True, message=f"Device {request.name} has been successfully registered.")


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    device_management_pb2_grpc.add_DeviceManagerServicer_to_server(Register(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()