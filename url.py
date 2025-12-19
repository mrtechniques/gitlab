import time
import webbrowser
import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_glitch(text, min_delay=0.002, max_delay=0.01):
    """Hacker-style glitchy typing."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(random.uniform(min_delay, max_delay))
    print()

def loading_bar(task="Processing", length=30, speed=0.03):
    print(f"\n{task}:")
    for i in range(length + 1):
        bar = "[" + "#" * i + "-" * (length - i) + "]"
        print(bar, end="\r", flush=True)
        time.sleep(speed)
    print()

def matrix_rain(lines=10, speed=0.02):
    chars = "01"
    for _ in range(lines):
        line = "".join(random.choice(chars) for _ in range(60))
        print(line)
        time.sleep(speed)

def countdown(seconds=3):
    for i in range(seconds, 0, -1):
        print(f"\n>> System Launch in {i} <<", end="\r", flush=True)
        time.sleep(1)
    print("\n")

def fake_ip():
    return ".".join(str(random.randint(1, 255)) for _ in range(4))

# -------------------------
#       ASCII LOGO
# -------------------------
ascii_logo = r"""
   ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ 
   ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
   ███████║███████║██║     █████╔╝ █████╗  ██████╔╝
   ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
"""

# -------------------------
#       MAIN PROGRAM
# -------------------------

clear_screen()
print(ascii_logo)
time.sleep(1)

# MATRIX RAIN INTRO
matrix_rain(lines=12, speed=0.03)
time.sleep(0.5)
clear_screen()

# SYSTEM BOOT SEQUENCE
type_glitch("[BOOT] Initializing core modules...")
loading_bar("Loading Kernel")
time.sleep(0.3)

type_glitch("[OK] Kernel loaded.")
time.sleep(0.2)

type_glitch("[BOOT] Activating encrypted subsystems...")
loading_bar("Decrypting Systems", speed=0.02)
type_glitch("[OK] Subsystems online.")
time.sleep(0.3)

clear_screen()

# -------------------------
#   FAKE IP TRACE SEQUENCE
# -------------------------

type_glitch("[SCAN] Initiating IP Trace Protocol...")
time.sleep(0.5)

for i in range(5):
    fake_target = fake_ip()
    type_glitch(f"[TRACE] Scanning target node: {fake_target} ...")
    time.sleep(random.uniform(0.2, 0.5))

type_glitch("[TRACE] Establishing connection to remote host...")
loading_bar("Routing Node Access", speed=0.02)

type_glitch("[OK] Trace Completed.")
time.sleep(0.4)

clear_screen()

# FINAL HACKER MESSAGE
type_glitch("ACCESS LEVEL: ROOT", 0.01, 0.03)
time.sleep(0.3)
type_glitch("AUTHORIZATION: GRANTED", 0.01, 0.03)
time.sleep(0.3)
type_glitch("\nPreparing to launch payload...", 0.01, 0.03)

for i in range(3):
    type_glitch(".", 0.08, 0.15)
    time.sleep(0.2)

countdown(3)

# -------------------------
#   OPEN THE URL HERE
# -------------------------
#url = "https://www.dropbox.com/scl/fi/2qrc5h9dze8lqcuqekn0g/download.jpg?rlkey=a21ir0ic0f7mp6mvmlesr6i4y&st=hsqistdn&dl=0"
url="https://www.dropbox.com/scl/fi/2qrc5h9dze8lqcuqekn0g/download.jpg?rlkey=a21ir0ic0f7mp6mvmlesr6i4y&st=eh3ceta1&dl=0"
webbrowser.open(url)

type_glitch("\nPAYLOAD DEPLOYED SUCCESSFULLY. 🚀", 0.01, 0.03)
