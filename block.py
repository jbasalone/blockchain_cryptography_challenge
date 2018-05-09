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
        
        
	def find_hash(self):
		#hash of hte block header + data
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(self.previous_hash)
        digest.update(str.encode(self.timestamp))
        digest.update(self.data)
        digest.update(self.nonce)
        self.hash = base64.b16encode(digest.finalize())

	def find_nonce(self, difficulty):
		prefix = b'0'*difficulty
	    while True:
			self.nonce = os.urandom(16)
			msg_digest = self.find_hash()
			if msg_digest.startswith(prefix):
				self.hash = msg_digest
				break
    
    def __repr__(self):
        return "PreviousHash: {0}\nTimestamp: {1}\nNonce: {2}\nHash: {3}".format(
            self.previous_hash, self.timestamp, base64.b16encode(self.nonce), self.hash)
