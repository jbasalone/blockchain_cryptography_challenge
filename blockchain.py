OLUTION

# SOLUTION


genesis_block = Block('Pycon 2018 Genesis BLock', '0000000000000000000000000000000000000000000000000000000000000000',b"FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")

class Blockchain():
    def __init__(self):
        self.blocks = []
    
    def __repr__(self):
        _blocks = []
        for _block in self.blocks:
            _blocks.append(str(_block))
        return "\n\n".join(_blocks)
    
    def add_block(self, block):
        self.blocks.append(block)
    
    def blockchain_valid(self):   
        # check if the genesis block is correct
        if self.blocks[0] != genesis_block:
            return False
        
        prv_block = self.blocks[0]
        
        for block in self.blocks[1:]:
            # check if the prv_hash of the block points to the prv block
            if prv_block.hash != block.prv_hash:
                return False
            
            # Check Hash(current+prv) = current hash
            digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
            digest.update(block.prv_hash)
            digest.update(str.encode(block.timestamp))
            digest.update(block.nonce)
            digest.update(block.data)
            hash_digest = base64.b16encode(digest.finalize())
            
            if hash_digest != block.hash:
                return False
            
            prv_block = block
	def mine_blocks(test_blockchain):
    s_time = int(time.time())
    duration = 10
    
    _prv_block = genesis_block
    
    while True:
        _block = block(_prv_block.hash, os.urandom(4))
        _block.find_nonce(3)
        test_blockchain.add_block(_block)
        _prv_block = _block
        print(".", end='')
        if int(time.time()) > duration + s_time:
            break

        
        return True
