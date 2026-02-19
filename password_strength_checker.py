import string

print("🔐 Password Strength Checker\n")

password = input("Enter your password: ")

score = 0

# Length check
if len(password) >= 8:
    score += 1

# Uppercase check
if any(char.isupper() for char in password):
    score += 1

# Lowercase check
if any(char.islower() for char in password):
    score += 1

# Digit check
if any(char.isdigit() for char in password):
    score += 1

# Special character check
if any(char in string.punctuation for char in password):
    score += 1

print("\n📊 Password Strength Result")

if score <= 2:
    print("❌ Weak Password")
elif score <= 4:
    print("⚠️ Medium Password")
else:
    print("✅ Strong Password")
