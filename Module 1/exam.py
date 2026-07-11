# ==========================================
# M1 Activity: Exam Eligibility Checker
# ==========================================

# Take attendance percentage as input
attendance = float(input("Enter your attendance percentage: "))

# Check eligibility
if attendance >= 75:
    print("Congratulations! You are eligible to appear for the exam.")
else:
    print("Sorry! You are not eligible to appear for the exam.")
