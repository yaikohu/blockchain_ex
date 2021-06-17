from typing import List
import time
import json
from hashlib import sha256


class Block:
    def __init__(self, index: int, 
                 transactions: List, 
                 timestamp: time.time, 
                 previous_hash: str):
        """ Constructor for the `Block` class.
        
        Args:
            index: Unique ID of the block.
            transactions: List of transactions.
            timestamp: Time of generation of the block.
            previous_hash: Hash of the previous block in the chain which this block is part of.                                        
        
        Returns:
            An instance of the `Block` class. A block object.
        """
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash # Adding the previous hash field
 
    def compute_hash(self):
        """
        Returns the hash of the block instance.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True) # The string equivalent also considers the previous_hash field now
        return sha256(block_string.encode()).hexdigest()