# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: orderer/ab.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common import common_pb2 as common_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='orderer/ab.proto',
  package='orderer',
  syntax='proto3',
  serialized_pb=_b('\n\x10orderer/ab.proto\x12\x07orderer\x1a\x13\x63ommon/common.proto\"3\n\x11\x42roadcastResponse\x12\x1e\n\x06Status\x18\x01 \x01(\x0e\x32\x0e.common.Status\"\xa8\x01\n\x08SeekInfo\x12*\n\x05Start\x18\x01 \x01(\x0e\x32\x1b.orderer.SeekInfo.StartType\x12\x17\n\x0fSpecifiedNumber\x18\x02 \x01(\x04\x12\x12\n\nWindowSize\x18\x03 \x01(\x04\x12\x0f\n\x07\x43hainID\x18\x04 \x01(\x0c\"2\n\tStartType\x12\n\n\x06NEWEST\x10\x00\x12\n\n\x06OLDEST\x10\x01\x12\r\n\tSPECIFIED\x10\x02\"!\n\x0f\x41\x63knowledgement\x12\x0e\n\x06Number\x18\x01 \x01(\x04\"o\n\rDeliverUpdate\x12\x33\n\x0f\x41\x63knowledgement\x18\x01 \x01(\x0b\x32\x18.orderer.AcknowledgementH\x00\x12!\n\x04Seek\x18\x02 \x01(\x0b\x32\x11.orderer.SeekInfoH\x00\x42\x06\n\x04Type\"Z\n\x0f\x44\x65liverResponse\x12\x1f\n\x05\x45rror\x18\x01 \x01(\x0e\x32\x0e.common.StatusH\x00\x12\x1e\n\x05\x42lock\x18\x02 \x01(\x0b\x32\r.common.BlockH\x00\x42\x06\n\x04Type2\x95\x01\n\x0f\x41tomicBroadcast\x12?\n\tBroadcast\x12\x10.common.Envelope\x1a\x1a.orderer.BroadcastResponse\"\x00(\x01\x30\x01\x12\x41\n\x07\x44\x65liver\x12\x16.orderer.DeliverUpdate\x1a\x18.orderer.DeliverResponse\"\x00(\x01\x30\x01\x42.Z,github.com/hyperledger/fabric/protos/ordererb\x06proto3')
  ,
  dependencies=[common_dot_common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_SEEKINFO_STARTTYPE = _descriptor.EnumDescriptor(
  name='StartType',
  full_name='orderer.SeekInfo.StartType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NEWEST', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OLDEST', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPECIFIED', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=222,
  serialized_end=272,
)
_sym_db.RegisterEnumDescriptor(_SEEKINFO_STARTTYPE)


_BROADCASTRESPONSE = _descriptor.Descriptor(
  name='BroadcastResponse',
  full_name='orderer.BroadcastResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Status', full_name='orderer.BroadcastResponse.Status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=101,
)


_SEEKINFO = _descriptor.Descriptor(
  name='SeekInfo',
  full_name='orderer.SeekInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Start', full_name='orderer.SeekInfo.Start', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SpecifiedNumber', full_name='orderer.SeekInfo.SpecifiedNumber', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='WindowSize', full_name='orderer.SeekInfo.WindowSize', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ChainID', full_name='orderer.SeekInfo.ChainID', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SEEKINFO_STARTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=104,
  serialized_end=272,
)


_ACKNOWLEDGEMENT = _descriptor.Descriptor(
  name='Acknowledgement',
  full_name='orderer.Acknowledgement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Number', full_name='orderer.Acknowledgement.Number', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=274,
  serialized_end=307,
)


_DELIVERUPDATE = _descriptor.Descriptor(
  name='DeliverUpdate',
  full_name='orderer.DeliverUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Acknowledgement', full_name='orderer.DeliverUpdate.Acknowledgement', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Seek', full_name='orderer.DeliverUpdate.Seek', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Type', full_name='orderer.DeliverUpdate.Type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=309,
  serialized_end=420,
)


_DELIVERRESPONSE = _descriptor.Descriptor(
  name='DeliverResponse',
  full_name='orderer.DeliverResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Error', full_name='orderer.DeliverResponse.Error', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Block', full_name='orderer.DeliverResponse.Block', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Type', full_name='orderer.DeliverResponse.Type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=422,
  serialized_end=512,
)

_BROADCASTRESPONSE.fields_by_name['Status'].enum_type = common_dot_common__pb2._STATUS
_SEEKINFO.fields_by_name['Start'].enum_type = _SEEKINFO_STARTTYPE
_SEEKINFO_STARTTYPE.containing_type = _SEEKINFO
_DELIVERUPDATE.fields_by_name['Acknowledgement'].message_type = _ACKNOWLEDGEMENT
_DELIVERUPDATE.fields_by_name['Seek'].message_type = _SEEKINFO
_DELIVERUPDATE.oneofs_by_name['Type'].fields.append(
  _DELIVERUPDATE.fields_by_name['Acknowledgement'])
_DELIVERUPDATE.fields_by_name['Acknowledgement'].containing_oneof = _DELIVERUPDATE.oneofs_by_name['Type']
_DELIVERUPDATE.oneofs_by_name['Type'].fields.append(
  _DELIVERUPDATE.fields_by_name['Seek'])
_DELIVERUPDATE.fields_by_name['Seek'].containing_oneof = _DELIVERUPDATE.oneofs_by_name['Type']
_DELIVERRESPONSE.fields_by_name['Error'].enum_type = common_dot_common__pb2._STATUS
_DELIVERRESPONSE.fields_by_name['Block'].message_type = common_dot_common__pb2._BLOCK
_DELIVERRESPONSE.oneofs_by_name['Type'].fields.append(
  _DELIVERRESPONSE.fields_by_name['Error'])
_DELIVERRESPONSE.fields_by_name['Error'].containing_oneof = _DELIVERRESPONSE.oneofs_by_name['Type']
_DELIVERRESPONSE.oneofs_by_name['Type'].fields.append(
  _DELIVERRESPONSE.fields_by_name['Block'])
_DELIVERRESPONSE.fields_by_name['Block'].containing_oneof = _DELIVERRESPONSE.oneofs_by_name['Type']
DESCRIPTOR.message_types_by_name['BroadcastResponse'] = _BROADCASTRESPONSE
DESCRIPTOR.message_types_by_name['SeekInfo'] = _SEEKINFO
DESCRIPTOR.message_types_by_name['Acknowledgement'] = _ACKNOWLEDGEMENT
DESCRIPTOR.message_types_by_name['DeliverUpdate'] = _DELIVERUPDATE
DESCRIPTOR.message_types_by_name['DeliverResponse'] = _DELIVERRESPONSE

BroadcastResponse = _reflection.GeneratedProtocolMessageType('BroadcastResponse', (_message.Message,), dict(
  DESCRIPTOR = _BROADCASTRESPONSE,
  __module__ = 'orderer.ab_pb2'
  # @@protoc_insertion_point(class_scope:orderer.BroadcastResponse)
  ))
_sym_db.RegisterMessage(BroadcastResponse)

SeekInfo = _reflection.GeneratedProtocolMessageType('SeekInfo', (_message.Message,), dict(
  DESCRIPTOR = _SEEKINFO,
  __module__ = 'orderer.ab_pb2'
  # @@protoc_insertion_point(class_scope:orderer.SeekInfo)
  ))
_sym_db.RegisterMessage(SeekInfo)

Acknowledgement = _reflection.GeneratedProtocolMessageType('Acknowledgement', (_message.Message,), dict(
  DESCRIPTOR = _ACKNOWLEDGEMENT,
  __module__ = 'orderer.ab_pb2'
  # @@protoc_insertion_point(class_scope:orderer.Acknowledgement)
  ))
_sym_db.RegisterMessage(Acknowledgement)

DeliverUpdate = _reflection.GeneratedProtocolMessageType('DeliverUpdate', (_message.Message,), dict(
  DESCRIPTOR = _DELIVERUPDATE,
  __module__ = 'orderer.ab_pb2'
  # @@protoc_insertion_point(class_scope:orderer.DeliverUpdate)
  ))
_sym_db.RegisterMessage(DeliverUpdate)

DeliverResponse = _reflection.GeneratedProtocolMessageType('DeliverResponse', (_message.Message,), dict(
  DESCRIPTOR = _DELIVERRESPONSE,
  __module__ = 'orderer.ab_pb2'
  # @@protoc_insertion_point(class_scope:orderer.DeliverResponse)
  ))
_sym_db.RegisterMessage(DeliverResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z,github.com/hyperledger/fabric/protos/orderer'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class AtomicBroadcastStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Broadcast = channel.stream_stream(
        '/orderer.AtomicBroadcast/Broadcast',
        request_serializer=common_dot_common__pb2.Envelope.SerializeToString,
        response_deserializer=BroadcastResponse.FromString,
        )
    self.Deliver = channel.stream_stream(
        '/orderer.AtomicBroadcast/Deliver',
        request_serializer=DeliverUpdate.SerializeToString,
        response_deserializer=DeliverResponse.FromString,
        )


class AtomicBroadcastServicer(object):

  def Broadcast(self, request_iterator, context):
    """broadcast receives a reply of Acknowledgement for each common.Envelope in order, indicating success or type of failure
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Deliver(self, request_iterator, context):
    """deliver first requires an update containing a seek message, then a stream of block replies is received.
    The receiver may choose to send an Acknowledgement for any block number it receives, however Acknowledgements must never be more than WindowSize apart
    To avoid latency, clients will likely acknowledge before the WindowSize has been exhausted, preventing the server from stopping and waiting for an Acknowledgement
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AtomicBroadcastServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Broadcast': grpc.stream_stream_rpc_method_handler(
          servicer.Broadcast,
          request_deserializer=common_dot_common__pb2.Envelope.FromString,
          response_serializer=BroadcastResponse.SerializeToString,
      ),
      'Deliver': grpc.stream_stream_rpc_method_handler(
          servicer.Deliver,
          request_deserializer=DeliverUpdate.FromString,
          response_serializer=DeliverResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'orderer.AtomicBroadcast', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaAtomicBroadcastServicer(object):
  def Broadcast(self, request_iterator, context):
    """broadcast receives a reply of Acknowledgement for each common.Envelope in order, indicating success or type of failure
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def Deliver(self, request_iterator, context):
    """deliver first requires an update containing a seek message, then a stream of block replies is received.
    The receiver may choose to send an Acknowledgement for any block number it receives, however Acknowledgements must never be more than WindowSize apart
    To avoid latency, clients will likely acknowledge before the WindowSize has been exhausted, preventing the server from stopping and waiting for an Acknowledgement
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaAtomicBroadcastStub(object):
  def Broadcast(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
    """broadcast receives a reply of Acknowledgement for each common.Envelope in order, indicating success or type of failure
    """
    raise NotImplementedError()
  def Deliver(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
    """deliver first requires an update containing a seek message, then a stream of block replies is received.
    The receiver may choose to send an Acknowledgement for any block number it receives, however Acknowledgements must never be more than WindowSize apart
    To avoid latency, clients will likely acknowledge before the WindowSize has been exhausted, preventing the server from stopping and waiting for an Acknowledgement
    """
    raise NotImplementedError()


def beta_create_AtomicBroadcast_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('orderer.AtomicBroadcast', 'Broadcast'): common_dot_common__pb2.Envelope.FromString,
    ('orderer.AtomicBroadcast', 'Deliver'): DeliverUpdate.FromString,
  }
  response_serializers = {
    ('orderer.AtomicBroadcast', 'Broadcast'): BroadcastResponse.SerializeToString,
    ('orderer.AtomicBroadcast', 'Deliver'): DeliverResponse.SerializeToString,
  }
  method_implementations = {
    ('orderer.AtomicBroadcast', 'Broadcast'): face_utilities.stream_stream_inline(servicer.Broadcast),
    ('orderer.AtomicBroadcast', 'Deliver'): face_utilities.stream_stream_inline(servicer.Deliver),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_AtomicBroadcast_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('orderer.AtomicBroadcast', 'Broadcast'): common_dot_common__pb2.Envelope.SerializeToString,
    ('orderer.AtomicBroadcast', 'Deliver'): DeliverUpdate.SerializeToString,
  }
  response_deserializers = {
    ('orderer.AtomicBroadcast', 'Broadcast'): BroadcastResponse.FromString,
    ('orderer.AtomicBroadcast', 'Deliver'): DeliverResponse.FromString,
  }
  cardinalities = {
    'Broadcast': cardinality.Cardinality.STREAM_STREAM,
    'Deliver': cardinality.Cardinality.STREAM_STREAM,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'orderer.AtomicBroadcast', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)