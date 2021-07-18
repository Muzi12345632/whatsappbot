import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        self.new_block(previous_hash="The Times 10/jul/2021 chancellor on brink of seco for banks.", proof=100)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamps': time(),
            'transaction': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),

        }
        self.pending_transactions = []
        self.chain.append(block)

        return block

    @property
    def last_block(self):

        return self.chain[-1]


    def  new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        }

        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

    def hash(selfself,block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash

blockchain = Blockchain()
t1 = blockchain.new_transaction("Satoshi", "muzi", '2BTC')
t2 = blockchain.new_transaction("mike", "satoshi", '22BTC')
t3 = blockchain.new_transaction("maya", "qala", '21BTC')
blockchain.new_block(12345)

t4 = blockchain.new_transaction("mela", "papa", '22BTC')
t5 = blockchain.new_transaction("kulo", "juju", '11BTC')
t6 = blockchain.new_transaction("wawa", "sasa", '33BTC')
blockchain.new_block(6789)

print("Blockchain: ", blockchain.chain)
