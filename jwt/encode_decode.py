import jwt

# Define a secret key
SECRET_KEY = 'your_secret_key'

# Payload data
payload = {'user_id': 123}

# Encode JWT
encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
print("Encoded JWT:", encoded_jwt)

# Decode JWT
decoded_jwt = jwt.decode(encoded_jwt, SECRET_KEY, algorithms=['HS256'])
print("Decoded JWT:", decoded_jwt)
