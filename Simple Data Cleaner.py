# ===============================
# 3. SIMPLE DATA CLEANER
# ===============================

names = [" Alice ", "bob", " CHARLIE "]

cleaned_names = []

for name in names:
    cleaned_name = name.strip().lower()   # Remove spaces + convert to lowercase
    cleaned_names.append(cleaned_name)

print("Cleaned Names List:", cleaned_names)
