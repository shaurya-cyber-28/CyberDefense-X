import datetime

from backend.network_sim.network_topology import create_default_topology
from backend.attack_engine.attack_simulator import launch_random_attack
from backend.attack_engine.packet_simulator import PacketSimulator
from backend.ai_detection.ai_ids import train_model, detect_attack
from frontend.visualization_3d.network_visualizer import visualize_network
from frontend.dashboard.security_dashboard import launch_dashboard


print("===================================")
print("   CyberDefense-X Security System  ")
print("===================================")


# Create log entry
def start_log():

    time = datetime.datetime.now()
    log_entry = f"System started at {time}\n"

    with open("logs/system_log.txt", "a") as log:
        log.write(log_entry)

    print("[+] Log system initialized")


# Initialize backend modules
def start_backend():

    print("[+] Starting Attack Simulation Engine...")
    print("[+] Starting AI Detection System...")
    print("[+] Starting Network Simulator...")


# Initialize frontend modules
def start_frontend():

    print("[+] Loading 3D Visualization...")
    print("[+] Launching Security Dashboard...")


def main():

    start_log()
    start_backend()
    start_frontend()

    # Create virtual network
    topology = create_default_topology()
    topology.display_topology()

    attack_path = [
    ("Attacker", "Router"),
    ("Router", "Server")
    ]

    visualize_network(attack_path)

    # Launch simulated cyber attack
    attack_type = launch_random_attack("Server")

    # Simulate packets
    packet_sim = PacketSimulator()
    packet_sim.simulate_ping("127.0.0.1")
    packet_sim.simulate_port_probe("127.0.0.1", 80)
    packet_sim.simulate_traffic("127.0.0.1")

    # Train AI detection system
    train_model()

    # Detect attack
    detect_attack(attack_type)

    launch_dashboard()


    print("\nCyberDefense-X is now running.")


if __name__ == "__main__":
    main()

