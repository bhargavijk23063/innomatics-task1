# ===============================
# 1. USER LOGIN CHECK
# ===============================

# Stored credentials (like database values)
stored_username = "admin"
stored_password = "1234"

# Input credentials (user entered values)
username = "admin"
password = "1234"

# Check if both username and password match
if username == stored_username and password == stored_password:
    print("Login Successful")
else:
    print("Invalid Credentials")
