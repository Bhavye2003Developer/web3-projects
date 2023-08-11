from ellipticcurve.ecdsa import Ecdsa
from ellipticcurve.privateKey import PrivateKey
import json

class Blockchain():
    def __init__(self) -> None:
        self.chain = []

    def addBlock(self, block):
        self.chain.append(block)

class Block():
    def __init__(self, prevHash, index, timestamp, data, nonce) -> None:
        self.prevHash = prevHash
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce


def CreatePrivateKey():
    privateKey = PrivateKey()
    return privateKey

def getSignature(message, privateKey):
    return Ecdsa.sign(message, privateKey)

def getMessage(sender, receiver, amount):
    return json.dumps({
        "sender": sender,
        "receiver": receiver,
        "amount": amount
    })

def verifyTransaction(message, signature, publicKey):
    return Ecdsa.verify(message, signature, publicKey)