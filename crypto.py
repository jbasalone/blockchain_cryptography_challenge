'''
cryptoclass
find a hash value that starts with two consevutive zeros b'00'
'''

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import base64 # to produce human readable encoding of the bytes
import random
import string

def random_string(length):
    pool = string.hexdigits
    return ''.join(random.choice(pool) for i in xrange(length))

n_tries = 0


while True: 
        
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(random_string(128))
    msg_digest = digest.finalize()
    encoded_msg_digest = base64.b64encode(msg_digest)
    
    n_tries += 1
    
    if encoded_msg_digest.startswith(b'00'):
        print n_tries, encoded_msg_digest
        break

