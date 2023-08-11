from Blockchain import *
from Crypto.Hash import SHA256
from datetime import datetime


# k = SHA256.new()
# msg = input("Enter message: ")
# k.update(msg.encode())
# print(k.hexdigest())

# blockchain = Blockchain()
# block = Block("0", 0, datetime.now().timestamp(), "Genesis Block", 0)
# blockchain.addBlock(block)
# print(blockchain.chain[0].timestamp)


# import ecdsa
# from ecdsa import SigningKey, VerifyingKey
# from cryptography.hazmat.primitives import serialization

# # Generate a private key using ecdsa
# private_key = SigningKey.generate(curve=ecdsa.SECP256k1)
# print("Private key: ", private_key.to_string().hex())

# # Generate a public key using ecdsa
# public_key = private_key.get_verifying_key()
# print("Public key: ", public_key.to_string().hex())


from ellipticcurve.ecdsa import Ecdsa
from ellipticcurve.privateKey import PrivateKey
import json

# Generate new Keys
privateKey = PrivateKey()
publicKey = privateKey.publicKey()
print("Private key: ", privateKey.toString())
print("Public key: ", publicKey.toString())

# finding address from public key
print(publicKey.toCompressed())



message = json.dumps({
    "sender": "Alice",
    "receiver": "Bob",
    "amount": 50
})

# Generate Signature
signature = Ecdsa.sign(message, privateKey) # sender's private key

# To verify if the signature is valid
print(Ecdsa.verify(message, signature, publicKey))