# ===============================
# 4. MESSAGE LENGTH ANALYZER
# ===============================

messages = ["Hi", "Welcome to the platform", "OK"]

for message in messages:
    length = len(message)
    print("Message:", message)
    print("Length:", length)
    
    # Check if message is longer than 10 characters
    if length > 10:
        print("⚠️ This message is longer than 10 characters")
    
    print("---------------------------")
