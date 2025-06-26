import os
import random

# Color setup
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
RESET = '\033[0m'

# Generate unique key
key = "RDG-" + str(random.randint(10000, 99999))

# Clear screen
os.system("clear")

# Banner
print(f"{R}██████╗ ██████╗  ██████╗      ██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗{RESET}")
print(f"{R}██╔══██╗██╔══██╗██╔═══██╗    ██╔════╝ ██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║{RESET}")
print(f"{R}██████╔╝██████╔╝██║   ██║    ██║  ███╗██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║{RESET}")
print(f"{R}██╔═══╝ ██╔══██╗██║   ██║    ██║   ██║██╔═══╝ ██╔══██║██║   ██║██║   ██║██║╚██╗██║{RESET}")
print(f"{R}██║     ██║  ██║╚██████╔╝    ╚██████╔╝██║     ██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║{RESET}")
print(f"{R}╚═╝     ╚═╝  ╚═╝ ╚═════╝      ╚═════╝ ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝{RESET}")

print(f"\n{C}Author      : Malik Habib")
print(f"Whatsapp     : +923434571018{RESET}")
print(f"{G}======================================================{RESET}\n")

# Load approved and blocked keys
approved_path = "keys/approved.txt"
blocked_path = "keys/blocked.txt"

approved_keys = []
if os.path.exists(approved_path):
    with open(approved_path, "r") as f:
        approved_keys = [line.strip() for line in f if line.strip()]

blocked_keys = []
if os.path.exists(blocked_path):
    with open(blocked_path, "r") as f:
        blocked_keys = [line.strip() for line in f if line.strip()]

# Approval check
if key in blocked_keys:
    print(f"{R}Your key is BLOCKED: {key}{RESET}")
    exit()
elif key in approved_keys:
    print(f"{G}Your key is APPROVED: {key}{RESET}\n")
else:
    print(f"{Y}Your key is NOT APPROVED: {key}{RESET}")
    print(f"Key: {C}{key}{RESET}")
    input(f"\n{Y}Press Enter to request approval via WhatsApp...{RESET}")
    os.system(f"xdg-open 'https://wa.me/923434571018?text=Please%20approve%20my%20key:%20{key}'")
    exit()

# Main options menu
print(f"{C}1. Poll Voting")
print(f"2. Post Like / Reacts")
print(f"3. Comment Voting")
print(f"4. Page Like / Follow")
print(f"5. Group Joining")
print(f"6. Reply to Comments")
print(f"7. Comment React")
print(f"8. Auto Page Creation")
print(f"9. Auto ID Creation{RESET}")
