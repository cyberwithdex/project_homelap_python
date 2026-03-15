def encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, shift):
    return encrypt(ciphertext, -shift)

def brute_force(ciphertext):
    print("\n🔍 Brute Force — All Possible Shifts:")
    print("-" * 40)
    for shift in range(1, 26):
        attempt = encrypt(ciphertext, -shift)
        print(f"  Shift {shift:2}: {attempt}")

def main():
    print("=" * 45)
    print("   🔐 Caesar Cipher Encryption Tool")
    print("=" * 45)

    print("\nWhat would you like to do?")
    print("  [1] Encrypt a message")
    print("  [2] Decrypt a message")
    print("  [3] Brute force decrypt (try all shifts)")

    choice = input("\nEnter your choice (1/2/3): ").strip()

    if choice in ['1', '2']:
        message = input("Enter your message: ")
        shift = int(input("Enter shift key (1-25): "))
        if choice == '1':
            result = encrypt(message, shift)
            print(f"\n✅ Encrypted Message: {result}")
        else:
            result = decrypt(message, shift)
            print(f"\n✅ Decrypted Message: {result}")
    elif choice == '3':
        message = input("Enter the ciphertext to brute force: ")
        brute_force(message)
    else:
        print("❌ Invalid choice. Please run the program again.")

if __name__ == "__main__":
    main()