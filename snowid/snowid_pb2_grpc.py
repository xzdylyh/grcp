# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import grpctest.snowid.snowid_pb2 as snowid__pb2


class snowidStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.generateSnowid = channel.unary_unary(
        '/snowid.snowid/generateSnowid',
        request_serializer=snowid__pb2.GenerateSnowidRequest.SerializeToString,
        response_deserializer=snowid__pb2.GenerateSnowidReply.FromString,
        )


class snowidServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def generateSnowid(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_snowidServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'generateSnowid': grpc.unary_unary_rpc_method_handler(
          servicer.generateSnowid,
          request_deserializer=snowid__pb2.GenerateSnowidRequest.FromString,
          response_serializer=snowid__pb2.GenerateSnowidReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'snowid.snowid', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
