# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import grpctest.openCard.user_pb2 as user__pb2


class userStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.batchOpenActualCard = channel.unary_unary(
        '/user.user/batchOpenActualCard',
        request_serializer=user__pb2.BatchOpenActualCardRequest.SerializeToString,
        response_deserializer=user__pb2.BatchOpenActualCardReply.FromString,
        )


class userServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def batchOpenActualCard(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_userServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'batchOpenActualCard': grpc.unary_unary_rpc_method_handler(
          servicer.batchOpenActualCard,
          request_deserializer=user__pb2.BatchOpenActualCardRequest.FromString,
          response_serializer=user__pb2.BatchOpenActualCardReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'user.user', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
