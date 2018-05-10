import time
import os
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import PublicFormat
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.hazmat.primitives import serialization

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

def hash_pub_key(private_key):
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(private_key.public_key().public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo))
        return base64.b16encode(digest.finalize())

def sign_tx(tx, private_key):
    return private_key.sign(tx, ec.ECDSA(hashes.SHA256()))

def serialize_pubkey(publickey):
    serialized_public = publickey.public_bytes(
    encoding=Encoding.PEM,
    format=PublicFormat.SubjectPublicKeyInfo)
    
    return serialized_public

def parse_serialized_pubkey(serialized_pubkey):
    loaded_public_key = serialization.load_pem_public_key(serialized_pubkey, backend=default_backend())
    return loaded_public_key
