# SOLUTION

import time
import os
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes 

class Block():
    def __init__(self, data, previous_hash, nonce=None):
        self.data = data
        
        #block header
        self.timestamp = str(int(time.time()))
        self.previous_hash = previous_hash
        if nonce:
            self.nonce= nonce
        else:
            self.nonce = base64.b16encode(os.urandom(16))
        
        #hash of hte block header + data
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(self.previous_hash)
        digest.update(str.encode(self.timestamp))
        digest.update(self.data)
        digest.update(self.nonce)
        self.hash = base64.b16encode(digest.finalize())
    
    def __repr__(self):
        return "PreviousHash: {0}\nTimestamp: {1}\nNonce: {2}\nHash: {3}".format(
            self.previous_hash, self.timestamp, self.nonce, self.hash)
