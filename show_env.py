import os

print("Greeting:", os.environ.get("GREETING"))
secret = os.environ.get("MY_SECRET", "")
print("The value of Secret is:",secret)
print("Secret is set:", bool(secret))
print("Secret length:", len(secret))
