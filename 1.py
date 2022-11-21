import base64
import uuid
import time
import threading
import sys

def StandardEncode(payload):
    
    if isinstance(payload, unicode):
       local_payload = payload.encode('utf-8')
    elif isinstance(payload, (bytes, bytearray)):
        local_payload = payload
    elif isinstance(payload, (int, float)):
        local_payload = str(payload).encode('ascii')
    elif payload is None:
        local_payload = b''
    
    return local_payload

xxx = 'fdsfsfdf'
StandardEncode(xxx)