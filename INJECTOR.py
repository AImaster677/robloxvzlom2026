import os
import sys
import time
import random
import ctypes

# ================== ЦВЕТА ==================
class C:
    HDR  = '\033[95m'
    BLU  = '\033[94m'
    CYN  = '\033[96m'
    GRN  = '\033[92m'
    YEL  = '\033[93m'
    RED  = '\033[91m'
    END  = '\033[0m'
    BOLD = '\033[1m'
    UND  = '\033[4m'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow(text, delay=0.015):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def bar(i, total, prefix='', length=42):
    percent = 100 * (i / float(total))
    filled = int(length * i // total)
    bar_str = '█' * filled + '░' * (length - filled)
    sys.stdout.write(f'\r{prefix} |{bar_str}| {percent:5.1f}%')
    sys.stdout.flush()
    if i == total:
        print()

def fake_stage(title, steps=28, base_delay=0.055):
    print(f"\n{C.CYN}{C.BOLD}[+] {title}{C.END}")
    for i in range(steps + 1):
        bar(i, steps, prefix='    ')
        time.sleep(base_delay + random.uniform(-0.015, 0.025))

# ================== СТАРТ ==================
clear()
print(f"""{C.HDR}{C.BOLD}
╔══════════════════════════════════════════════════════════╗
║           SHADOWCORE AI  —  INJECTOR v9.9.9              ║
║              Undetected Quantum Injection Engine         ║
╚══════════════════════════════════════════════════════════╝{C.END}
""")

slow(f"{C.YEL}[!] Please open your game window first.{C.END}", 0.02)
slow(f"{C.YEL}[!] Make sure the game is fully loaded and in the main menu / lobby.{C.END}", 0.02)
print()
slow(f"{C.GRN}When the game is ready, type {C.BOLD}1{C.END}{C.GRN} and press Enter to begin injection...{C.END}", 0.02)
print()

while True:
    user = input(f"{C.CYN}>>> {C.END}").strip()
    if user == "1":
        break
    print(f"{C.RED}[!] Invalid input. Type only 1{C.END}")

# ================== ФЕЙКОВАЯ ЗАГРУЗКА ==================
clear()
print(f"{C.HDR}{C.BOLD}SHADOWCORE AI — INJECTION SEQUENCE STARTED{C.END}\n")

stages = [
    ("Initializing quantum core...", 22),
    ("Scanning for anti-cheat modules...", 26),
    ("Bypassing kernel callbacks...", 24),
    ("Caching game signatures...", 30),
    ("Building local AI neural map...", 28),
    ("Allocating protected memory regions...", 20),
    ("Hooking rendering pipeline...", 25),
    ("Calibrating head-detection model...", 27),
    ("Encrypting payload in transit...", 23),
    ("Finalizing stealth injection...", 32),
]

for title, steps in stages:
    fake_stage(title, steps)
    time.sleep(0.3)

print(f"\n{C.GRN}{C.BOLD}[✓] Injection completed successfully!{C.END}")
time.sleep(1.2)

# ================== КРАСИВОЕ ОКНО ==================
MessageBox = ctypes.windll.user32.MessageBoxW

MessageBox(
    None,
    "Thank you for installing and using ShadowCore AI!\n\n"
    "Everything was done successfully.\n\n"
    "Now please run RecorderX.exe to activate the cheat inside your game.\n\n"
    "Have fun and stay undetected.",
    "ShadowCore AI — Installation Complete",
    0x40 | 0x0  # MB_ICONINFORMATION | MB_OK
)

print(f"\n{C.CYN}You can now close this window.{C.END}")
input()