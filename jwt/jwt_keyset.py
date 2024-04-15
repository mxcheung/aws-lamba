import requests
import jwt

def decode_jwt_with_jwk_uri(jwt_token, jwk_uri):
    # Fetch the JWK set
    jwk_set = requests.get(jwk_uri).json()

    # Extract the key from the JWK set
    key = None
    for key_data in jwk_set['keys']:
        if key_data['kid'] == jwt.decode(jwt_token, verify=False)['kid']:
            key = jwt.algorithms.RSAAlgorithm.from_jwk(key_data)
            break

    if key is None:
        raise ValueError("Key not found in JWK set")

    # Decode the JWT token using the extracted key
    decoded_token = jwt.decode(jwt_token, key=key, algorithms=['RS256'])

    return decoded_token

# Example usage
jwt_token = "YOUR_JWT_TOKEN_HERE"
jwk_uri = "YOUR_JWK_URI_HERE"

decoded_token = decode_jwt_with_jwk_uri(jwt_token, jwk_uri)
print(decoded_token)
