from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

class User:
    def __init__(self, name):
        self.name = name
        self.private_key = rsa.generate_private_key(public_exponent=65537,key_size=2048)
        self.public_key = self.private_key.public_key()
    