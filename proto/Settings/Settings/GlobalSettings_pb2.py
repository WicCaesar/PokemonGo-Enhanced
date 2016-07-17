# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Settings/GlobalSettings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Settings import Fort_pb2 as Settings_dot_Fort__pb2
from Settings import Map_pb2 as Settings_dot_Map__pb2
from Settings import Level_pb2 as Settings_dot_Level__pb2
from Settings import Inventory_pb2 as Settings_dot_Inventory__pb2

from Settings.Fort_pb2 import *
from Settings.Map_pb2 import *
from Settings.Level_pb2 import *
from Settings.Inventory_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='Settings/GlobalSettings.proto',
  package='POGOProtos.Settings',
  syntax='proto3',
  serialized_pb=_b('\n\x1dSettings/GlobalSettings.proto\x12\x13POGOProtos.Settings\x1a\x13Settings/Fort.proto\x1a\x12Settings/Map.proto\x1a\x14Settings/Level.proto\x1a\x18Settings/Inventory.proto\"\xde\x01\n\x0eGlobalSettings\x12\'\n\x04\x66ort\x18\x02 \x01(\x0b\x32\x19.POGOProtos.Settings.Fort\x12%\n\x03map\x18\x03 \x01(\x0b\x32\x18.POGOProtos.Settings.Map\x12)\n\x05level\x18\x04 \x01(\x0b\x32\x1a.POGOProtos.Settings.Level\x12\x31\n\tinventory\x18\x05 \x01(\x0b\x32\x1e.POGOProtos.Settings.Inventory\x12\x1e\n\x16minimum_client_version\x18\x06 \x01(\tP\x00P\x01P\x02P\x03\x62\x06proto3')
  ,
  dependencies=[Settings_dot_Fort__pb2.DESCRIPTOR,Settings_dot_Map__pb2.DESCRIPTOR,Settings_dot_Level__pb2.DESCRIPTOR,Settings_dot_Inventory__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GLOBALSETTINGS = _descriptor.Descriptor(
  name='GlobalSettings',
  full_name='POGOProtos.Settings.GlobalSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fort', full_name='POGOProtos.Settings.GlobalSettings.fort', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='map', full_name='POGOProtos.Settings.GlobalSettings.map', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='POGOProtos.Settings.GlobalSettings.level', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inventory', full_name='POGOProtos.Settings.GlobalSettings.inventory', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minimum_client_version', full_name='POGOProtos.Settings.GlobalSettings.minimum_client_version', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=144,
  serialized_end=366,
)

_GLOBALSETTINGS.fields_by_name['fort'].message_type = Settings_dot_Fort__pb2._FORT
_GLOBALSETTINGS.fields_by_name['map'].message_type = Settings_dot_Map__pb2._MAP
_GLOBALSETTINGS.fields_by_name['level'].message_type = Settings_dot_Level__pb2._LEVEL
_GLOBALSETTINGS.fields_by_name['inventory'].message_type = Settings_dot_Inventory__pb2._INVENTORY
DESCRIPTOR.message_types_by_name['GlobalSettings'] = _GLOBALSETTINGS

GlobalSettings = _reflection.GeneratedProtocolMessageType('GlobalSettings', (_message.Message,), dict(
  DESCRIPTOR = _GLOBALSETTINGS,
  __module__ = 'Settings.GlobalSettings_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Settings.GlobalSettings)
  ))
_sym_db.RegisterMessage(GlobalSettings)


# @@protoc_insertion_point(module_scope)