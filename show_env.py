import os

print("Greeting:", os.environ.get("GREETING"))
secret = os.environ.get("MY_SECRET", "")
print("Secret is set:", bool(secret))
print("Secret length:", len(secret))
