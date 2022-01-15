import jwt

private_key = open("private.pem").read()
public_key = open("receiver.pem").read()
encoded = jwt.encode({"some": "payload"}, private_key, algorithm="RS256")
decoded = jwt.decode(encoded, public_key, algorithms=["RS256"])
