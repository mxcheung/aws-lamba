jwk_uri = "your_jwk_uri"
issuer = "your_issuer"
authorizer = JWTAuthorizer(jwk_uri, issuer)

# Assuming token is obtained from the client
token = "your_jwt_token_string"

authorized, decoded_token = authorizer.authorize(token)
if authorized:
    print("Token is valid")
    # Do something with the decoded token
    print(decoded_token)
else:
    print("Token is not valid:", decoded_token)
