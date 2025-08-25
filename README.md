Overview
This Python-based project simulates keylogger activity and demonstrates firewall defense mechanisms in a safe, controlled environment. It provides hands-on experience with red-team vs blue-team scenarios, including capturing keystrokes, monitoring network traffic, and detecting suspicious processes.

Features
-Red Team Simulation: Keylogger captures keystrokes and attempts to send data to a simulated attacker.
-Firewall Simulator: Checks outgoing traffic against predefined rules, allowing safe traffic and blocking suspicious destinations.
-Keylogger Detection: Identifies potentially malicious processes running on the system.
-Optional Keylogging: Logs keystrokes locally for educational purposes without transmitting real data.

Technologies Used
-Python 3
-pynput – Keyboard input capture
-psutil – Process monitoring
-logging – File-based logging of keystrokes

Features:
-Observe normal traffic, simulated keylogger attempts, and firewall decisions.
-(Optional) Uncomment run_keylogger() to log keystrokes locally for learning purposes.

Safety & Disclaimer
-This project is for educational purposes only.
-Do not run this on systems without explicit permission.
-No real data is transmitted; all exfiltration is simulated.

Learning Outcomes
-Understanding keylogger mechanics and data capture.
-Implementing firewall rules to monitor and block traffic.
-Detecting malicious processes and simulating endpoint security.
-Practical experience with Python programming in cybersecurity contexts.
