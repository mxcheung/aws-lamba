import jwt
import requests
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

class JWTAuthorizer:
    def __init__(self, jwk_uri, issuer):
        self.jwk_uri = jwk_uri
        self.issuer = issuer
        self.rsa_public_key = self.fetch_rsa_public_key()

    def fetch_rsa_public_key(self):
        # Fetch JWK from the provided URI
        response = requests.get(self.jwk_uri)
        jwk_data = response.json()

        # Extract the RSA public key from JWK
        rsa_public_key = None
        for key in jwk_data['keys']:
            if key['kty'] == 'RSA':
                rsa_key_components = {
                    'e': key['e'],
                    'n': key['n']
                }
                rsa_public_key = serialization.load_der_public_key(
                    jwt.algorithms.RSAAlgorithm.jwk_to_der(rsa_key_components),
                    backend=default_backend()
                )
                break

        if rsa_public_key is None:
            raise ValueError("No RSA public key found in JWK")

        return rsa_public_key

    def authorize(self, token):
        try:
            decoded_token = jwt.decode(token, self.rsa_public_key, algorithms=['RS256'], issuer=self.issuer)
            # Optionally, you can perform additional checks on the decoded token here
            # such as verifying user roles, expiration time, etc.
            return True, decoded_token
        except jwt.ExpiredSignatureError:
            return False, "Token expired"
        except jwt.InvalidIssuerError:
            return False, "Invalid token issuer"
        except jwt.InvalidTokenError:
            return False, "Invalid token"
