from collections import OrderedDict

import binascii

import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

import hashlib
import json
from time import time
from urllib.parse import urlparse
from uuid import uuid4

import pdb

MINING_DIFFICULTY = 1

class MerkleChain:

    def __init__(self):
        self.transactions = []

    def proof_of_work(self, inputState, nonce=None):
        """
        Proof of work algorithm
        """
        last_hash = inputState

        # change to a random number so that different miners have different energy costs
        if nonce is None:
            nonce = int(str(uuid4()).replace('-', ''),16)
        initialNonce = nonce

        energyMeter = 1
        chainState = 1

        while self.valid_proof(self.transactions, last_hash, nonce) is False:
            energyMeter += 1
            nonce = hashlib.sha256(str(nonce).encode()).hexdigest()
            #Attempt to calculate the PoW
            chainState = hashlib.sha256(
                str(self.transactions).encode() + 
                str(last_hash).encode() +
                str(nonce).encode() +
                str(energyMeter).encode() +
                str(chainState).encode()).hexdigest()

        print("Iteration count: {}".format(energyMeter))
        result = Result(nonce, energyMeter, initialNonce, chainState, inputState)

        return result

    def valid_proof(self, transactions, last_hash, nonce, difficulty=MINING_DIFFICULTY):
        """
        Check if a hash value satisfies the mining conditions. This function is used within the proof_of_work function.
        """
        guess = (str(transactions)+str(last_hash)+str(nonce)).encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        print("Hashing with nonce: {}".format(guess_hash))
        return guess_hash[:difficulty] == '0'*difficulty

    def test_pow(self, inputData):
        """
        Test Proof of work
        """

        #Miner calculates the merkle proof
        result = self.proof_of_work(inputData)
        initialNonce = result.initialNonce

        #Recalculate merkle proof from same nonce
        secondResult = self.proof_of_work(inputData, initialNonce)

        #Validate input data
        assert result.inputState == secondResult.inputState,"Different input data"
        #Validate initial nonce
        assert result.initialNonce == secondResult.initialNonce,"Different initial nonce"
        #Validate iteration count
        assert result.energyMeter == secondResult.energyMeter,"Different number of iterations"
        #Validate ending nonce
        assert result.nonce == secondResult.nonce,"Different ending nonce"
        #Validate merkle proof
        assert result.chainState == secondResult.chainState,"Different merkle proof"

        print('\nProof validated!')

    def select_validator_pool(self, nodeWeights, last_hash):

        #Sort by weight, drop node if weight == 0
        sortedNodes = OrderedDict(sorted(nodeWeights.items()))
        nodes = dict([ (k,v) for k,v in sortedNodes.items() if v > 0])
        hashCodes = dict()

        for id, v in nodes.items():
            if id is not None and v > 0:
                count = 0
                while count < v:
                    last_hash = hashlib.sha256(str(last_hash).encode()).hexdigest()
                    hashCodes[last_hash] = id
                    count +=1
        
        validatorPool = []
        sortedHashCodes = OrderedDict(sorted(hashCodes.items()))
        for k, v in sortedHashCodes.items():
            #print("k,v", (k,v))
            if v not in validatorPool:
                validatorPool.append(v)
            if len(validatorPool) == 3:
                break
        return validatorPool

class Result:
    def __init__(self, nonce, energyMeter, initialNonce, chainState, inputState):
        self.nonce = nonce
        self.energyMeter = energyMeter
        self.initialNonce = initialNonce
        self.chainState = chainState
        self.inputState = inputState       

m = MerkleChain()

miners = {'A':1, 'B':3, 'C':8, 'D':3, 'E':2, 'F':0, 'G':5, 'H':10, 'I':2}
lastHash = '2ffdb1929943256e954b85e79a09863df33b3706c7404de477640d4e2be495ac'

validators = m.select_validator_pool(miners, lastHash)
print(str(validators))

minerResults = {}
#Each miner calculates the proof
for miner in miners:
    result = m.proof_of_work(lastHash)
    minerResults[miner] = result

#sort on keys
#alpha node validates shortest
#other validators validate alpha's choice

m.test_pow(lastHash)

