# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nchat.proto\"4\n\x0fUserCredentials\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\x1a\n\tUserQuery\x12\r\n\x05query\x18\x01 \x01(\t\"\x17\n\x04User\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"S\n\x07Message\x12\x14\n\x0c\x66rom_user_id\x18\x01 \x01(\t\x12\x12\n\nto_user_id\x18\x02 \x01(\t\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\"\x1f\n\x0cMessageQuery\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"?\n\x13SendMessageResponse\x12\x11\n\tdelivered\x18\x01 \x01(\x08\x12\x15\n\rerror_message\x18\x02 \x01(\t\"?\n\x15\x44\x65leteAccountResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x15\n\rerror_message\x18\x02 \x01(\t\"8\n\x0eSignInResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x15\n\rerror_message\x18\x02 \x01(\t\"8\n\x0eSignUpResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x15\n\rerror_message\x18\x02 \x01(\t\"9\n\x0fSignOutResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x15\n\rerror_message\x18\x02 \x01(\t\"\x07\n\x05\x45mpty2\xdd\x02\n\x0b\x43hatService\x12-\n\x06SignUp\x12\x10.UserCredentials\x1a\x0f.SignUpResponse\"\x00\x12-\n\x06SignIn\x12\x10.UserCredentials\x1a\x0f.SignInResponse\"\x00\x12\"\n\tListUsers\x12\n.UserQuery\x1a\x05.User\"\x00\x30\x01\x12/\n\x07SignOut\x12\x10.UserCredentials\x1a\x10.SignOutResponse\"\x00\x12/\n\x0bSendMessage\x12\x08.Message\x1a\x14.SendMessageResponse\"\x00\x12-\n\x0eReceiveMessage\x12\r.MessageQuery\x1a\x08.Message\"\x00\x30\x01\x12;\n\rDeleteAccount\x12\x10.UserCredentials\x1a\x16.DeleteAccountResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chat_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _USERCREDENTIALS._serialized_start=14
  _USERCREDENTIALS._serialized_end=66
  _USERQUERY._serialized_start=68
  _USERQUERY._serialized_end=94
  _USER._serialized_start=96
  _USER._serialized_end=119
  _MESSAGE._serialized_start=121
  _MESSAGE._serialized_end=204
  _MESSAGEQUERY._serialized_start=206
  _MESSAGEQUERY._serialized_end=237
  _SENDMESSAGERESPONSE._serialized_start=239
  _SENDMESSAGERESPONSE._serialized_end=302
  _DELETEACCOUNTRESPONSE._serialized_start=304
  _DELETEACCOUNTRESPONSE._serialized_end=367
  _SIGNINRESPONSE._serialized_start=369
  _SIGNINRESPONSE._serialized_end=425
  _SIGNUPRESPONSE._serialized_start=427
  _SIGNUPRESPONSE._serialized_end=483
  _SIGNOUTRESPONSE._serialized_start=485
  _SIGNOUTRESPONSE._serialized_end=542
  _EMPTY._serialized_start=544
  _EMPTY._serialized_end=551
  _CHATSERVICE._serialized_start=554
  _CHATSERVICE._serialized_end=903
# @@protoc_insertion_point(module_scope)