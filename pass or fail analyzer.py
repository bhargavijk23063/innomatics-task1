# ===============================
# 2. PASS / FAIL ANALYZER
# ===============================

marks = [45, 78, 90, 33, 60]

pass_count = 0
fail_count = 0

# Loop through each mark
for mark in marks:
    if mark >= 50:
        pass_count += 1
    else:
        fail_count += 1

# Print final results
print("Total Students:", len(marks))
print("Total Passed Students:", pass_count)
print("Total Failed Students:", fail_count)
