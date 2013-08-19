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