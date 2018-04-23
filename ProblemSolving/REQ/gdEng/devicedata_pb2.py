# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: devicedata.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='devicedata.proto',
  package='gdEng',
  serialized_pb=_b('\n\x10\x64\x65vicedata.proto\x12\x05gdEng\"\x88\x01\n\x06\x44\x65vice\x12\x13\n\x0btemperature\x18\x01 \x02(\x05\x12\x19\n\x11\x61mpereConsumption\x18\x02 \x02(\x05\x12\x0f\n\x07\x62\x61ttery\x18\x03 \x02(\x05\x12\x0e\n\x06option\x18\x04 \x02(\x03\x12\r\n\x05power\x18\x05 \x02(\x08\x12\x1e\n\ninsertTime\x18\x06 \x01(\t:\nUNINSERTED\"+\n\nDeviceData\x12\x1d\n\x06\x64\x65vice\x18\x01 \x03(\x0b\x32\r.gdEng.Device')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DEVICE = _descriptor.Descriptor(
  name='Device',
  full_name='gdEng.Device',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='temperature', full_name='gdEng.Device.temperature', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ampereConsumption', full_name='gdEng.Device.ampereConsumption', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battery', full_name='gdEng.Device.battery', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='option', full_name='gdEng.Device.option', index=3,
      number=4, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='power', full_name='gdEng.Device.power', index=4,
      number=5, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='insertTime', full_name='gdEng.Device.insertTime', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("UNINSERTED").decode('utf-8'),
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=164,
)


_DEVICEDATA = _descriptor.Descriptor(
  name='DeviceData',
  full_name='gdEng.DeviceData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device', full_name='gdEng.DeviceData.device', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=166,
  serialized_end=209,
)

_DEVICEDATA.fields_by_name['device'].message_type = _DEVICE
DESCRIPTOR.message_types_by_name['Device'] = _DEVICE
DESCRIPTOR.message_types_by_name['DeviceData'] = _DEVICEDATA

Device = _reflection.GeneratedProtocolMessageType('Device', (_message.Message,), dict(
  DESCRIPTOR = _DEVICE,
  __module__ = 'devicedata_pb2'
  # @@protoc_insertion_point(class_scope:gdEng.Device)
  ))
_sym_db.RegisterMessage(Device)

DeviceData = _reflection.GeneratedProtocolMessageType('DeviceData', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEDATA,
  __module__ = 'devicedata_pb2'
  # @@protoc_insertion_point(class_scope:gdEng.DeviceData)
  ))
_sym_db.RegisterMessage(DeviceData)


# @@protoc_insertion_point(module_scope)
