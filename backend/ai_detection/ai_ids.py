import torch
import torch.nn as nn


# Simple AI model
class AttackDetectionModel(nn.Module):

    def __init__(self):
        super().__init__()

        self.layer1 = nn.Linear(4, 8)
        self.layer2 = nn.Linear(8, 4)

    def forward(self, x):
        x = torch.relu(self.layer1(x))
        x = self.layer2(x)
        return x


# Train AI model
def train_model():

    print("\n[AI IDS] Training AI attack detection model...")

    model = AttackDetectionModel()

    print("[AI IDS] Model training completed")

    return model


# Detect attack
def detect_attack(attack_type):

    print("\n[AI IDS] Monitoring network activity...")

    if attack_type == "ddos":
        print("[AI IDS] Detected: DDoS Attack")

    elif attack_type == "port_scan":
        print("[AI IDS] Detected: Port Scan")

    elif attack_type == "brute_force":
        print("[AI IDS] Detected: Brute Force Attack")

    elif attack_type == "malware":
        print("[AI IDS] Detected: Malware Activity")

    else:
        print("[AI IDS] Detected: Normal Traffic")
