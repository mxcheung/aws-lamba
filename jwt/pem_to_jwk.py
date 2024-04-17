from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
import json

def pem_to_jwk(pem_data):
    private_key = serialization.load_pem_private_key(pem_data, password=None, backend=default_backend())
    public_key = private_key.public_key()

    jwk = {
        "kty": "RSA",
        "n": public_key.public_numbers().n,
        "e": public_key.public_numbers().e,
    }

    return jwk

# Read PEM file
with open("private_key.pem", "rb") as pem_file:
    pem_data = pem_file.read()

# Convert PEM to JWK
jwk = pem_to_jwk(pem_data)

# Print JWK
print(json.dumps(jwk, indent=4))

