from __future__ import print_function

import logging

import grpc
import device_management_pb2
import device_management_pb2_grpc

server_path = "localhost:50051"

def run():
    print("Client `run` started")
    with grpc.insecure_channel(server_path) as channel:
        stub = device_management_pb2_grpc.DeviceManagerStub(channel)
        try:
            response = stub.RegisterDevice(device_management_pb2.DeviceInfo(name="Lamp"))
            print("Greeter client received: " + response.message)
        except grpc.RpcError as exc:
            # Exploring exception formatting
            # https://docs.ros.org/en/noetic/api/grpc/html/classgrpc_1_1__channel_1_1__InactiveRpcError.html
            print('error')
            print('args')
            state = exc.args[0] # python sees as tuple[Any, ...] but it returns (<grpc._channel._RPCState object at 0x105a70830>,)
            # https://docs.ros.org/en/noetic/api/grpc/html/classgrpc_1_1__channel_1_1__RPCState.html
            print("cancelled", state.cancelled) # not present in grpc.RpcError
            print("state code", exc.code)
            print("code", exc.code())
            print("code name", exc.code().name)
            print("code value", exc.code().value)
            print("state condition", state.condition)
            print("state debug_error_string", state.debug_error_string)
            print("debug_error_string", exc.debug_error_string()) # not present in grpc.RpcError
            print("state details", state.details)
            print("details", exc.details())
            print("state due", state.due)
            print("done", exc.done()) # not present in grpc.RpcError
            print("exception", exc.exception()) # not present in grpc.RpcError
            print("state fork_epoch", state.fork_epoch)
            print("state initial_metadata", state.initial_metadata)
            print("initial_metadata", exc.initial_metadata()) # not present in grpc.RpcError
            # print("result", exc.result()) # raises exception again
            print("state response", state.response)
            print("running", exc.running()) # not present in grpc.RpcError
            # print("traceback", exc.traceback()) #
            print("state trailing_metadata", state.trailing_metadata)
            print("trailing_metadata", exc.trailing_metadata())
            
            # Afterthought:
            # - Although I see error messsage I do not know how to parse it.
            # - Most of the methods are present in grpc._channel._InactiveRpcError but not grpc.RpcError


if __name__ == "__main__":
    logging.basicConfig()
    run()