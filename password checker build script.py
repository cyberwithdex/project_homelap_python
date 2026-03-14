import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password is too short. Use at least 8 characters.")

    # Check for uppercase
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one uppercase letter (A-Z).")

    # Check for lowercase
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one lowercase letter (a-z).")

    # Check for numbers
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 2
    else:
        feedback.append("❌ Add at least one special character (!, @, #, $, etc.)")

    # Check for common passwords
    common_passwords = ['password', '123456', 'qwerty', 'abc123', 'letmein', 'welcome']
    if password.lower() in common_passwords:
        score = 0
        feedback.append("❌ This is a very common password. Please choose something unique.")

    # Determine strength
    if score >= 6:
        strength = "🟢 Strong"
    elif score >= 3:
        strength = "🟡 Medium"
    else:
        strength = "🔴 Weak"

    return strength, score, feedback

def main():
    print("=" * 40)
    print("   🔐 Password Strength Checker")
    print("=" * 40)

    password = input("\nEnter your password: ")
    strength, score, feedback = check_password_strength(password)

    print(f"\nStrength: {strength}")
    print(f"Score: {score}/7")

    if feedback:
        print("\n💡 Tips to improve your password:")
        for tip in feedback:
            print(f"  {tip}")
    else:
        print("\n✅ Great password! No improvements needed.")

if __name__ == "__main__":
    main()