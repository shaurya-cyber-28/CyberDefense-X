import random
import time


def ddos_attack(target):

    print(f"\n[ATTACK] Launching DDoS attack on {target}")

    for i in range(5):
        print(f"Sending flood packet {i+1}")
        time.sleep(0.3)

    print("[RESULT] DDoS attack simulation completed\n")
    return "ddos"


def port_scan(target):

    print(f"\n[ATTACK] Scanning ports on {target}")

    for i in range(5):
        port = random.randint(20, 1024)
        print(f"Port {port} is OPEN")
        time.sleep(0.2)

    print("[RESULT] Port scan completed\n")
    return "port_scan"


def brute_force(target):

    print(f"\n[ATTACK] Attempting brute force login on {target}")

    attempts = ["admin", "root", "password123", "123456", "letmein"]

    for password in attempts:
        print(f"Trying password: {password}")
        time.sleep(0.3)

    print("[RESULT] Brute force simulation finished\n")
    return "brute_force"


def malware_attack(target):

    print(f"\n[ATTACK] Deploying malware to {target}")

    stages = [
        "Payload delivery",
        "Execution",
        "Privilege escalation",
        "Persistence",
        "Data exfiltration"
    ]

    for stage in stages:
        print(f"Malware stage: {stage}")
        time.sleep(0.3)

    print("[RESULT] Malware spread completed\n")
    return "malware"


def launch_random_attack(target):

    attacks = [
        ddos_attack,
        port_scan,
        brute_force,
        malware_attack
    ]

    attack = random.choice(attacks)

    return attack(target)
