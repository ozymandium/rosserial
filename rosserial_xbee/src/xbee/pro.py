"""
pro.py

by Robert Cofield, 2013

This module provides an XBee Pro (specifically XBee-PRO XSC & XBee-PRO 900HP)
API library.
"""
import struct
from xbee.base import XBeeBase


class XBeePro(XBeeBase):
  """
  Provides an implementation of the XBee API for Proprietary protocol modules

  This was developed with an XBee-PRO XSC S3B
  
  Commands may be sent to a device by instansiating this class with
  a serial port object (see PySerial) and then calling the send
  method with the proper information specified by the API. Data may
  be read from a device syncronously by calling wait_read_frame. For
  asynchronous reads, see the definition of XBeeBase.
  """
  # Packets which can be sent to an XBee
  # Format: 
  #        {name of command:
  #           [{name:field name, len:field length, default: default value sent}
  #            ...
  #            ]
  #         ...
  #         }
  api_commands = {
    "tx": [
      {'name':'id',              'len':1,        'default':'\x01'},
      {'name':'frame_id',        'len':1,        'default':'\x00'},
      {'name':'dest_addr',       'len':2,        'default':None},
      {'name':'options',         'len':1,        'default':'\x00'},
      {'name':'data',            'len':None,     'default':None}
    ],
  }
  
  # Packets which can be received from an XBee
  # Format: 
  #        {id byte received from XBee:
  #           {name: name of response
  #            structure:
  #                [ {'name': name of field, 'len':length of field}
  #                  ...
  #                  ]
  #            parse_as_io_samples:name of field to parse as io
  #           }
  #           ...
  #        }
  #
  api_responses = {
    "\x01": {
      'name':'rx',
      'structure': [
        # {'name':'id',              'len':1,        'default':'\x01'},
        {'name':'frame_id',        'len':1,        'default':'\x00'},
        {'name':'dest_addr',       'len':2,        'default':None},
        {'name':'options',         'len':1,        'default':'\x00'},
        {'name':'data',            'len':None,     'default':None}
      ],
    },
  }
  
  def __init__(self, *args, **kwargs):
      # Call the super class constructor to save the serial port
      super(XBeePro, self).__init__(*args, **kwargs)
