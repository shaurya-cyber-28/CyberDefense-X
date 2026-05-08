# CyberDefense-X Packet Simulation Engine
# Uses Scapy to simulate packets in a safe environment

from scapy.all import IP, TCP, ICMP, send
import time


class PacketSimulator:

    def simulate_ping(self, target="127.0.0.1"):
        print("\n[PACKET SIM] Sending ICMP ping packets")

        for i in range(3):
            packet = IP(dst=target)/ICMP()
            send(packet, verbose=False)
            print(f"ICMP packet {i+1} sent to {target}")
            time.sleep(0.5)

        print("[RESULT] Ping simulation completed\n")


    def simulate_port_probe(self, target="127.0.0.1", port=80):
        print(f"\n[PACKET SIM] Simulating TCP SYN packet to port {port}")

        packet = IP(dst=target)/TCP(dport=port, flags="S")

        send(packet, verbose=False)

        print(f"TCP SYN packet sent to {target}:{port}")
        print("[RESULT] Port probe simulation completed\n")


    def simulate_traffic(self, target="127.0.0.1"):
        print("\n[PACKET SIM] Simulating network traffic")

        for i in range(5):
            packet = IP(dst=target)/TCP(dport=443)
            send(packet, verbose=False)
            print(f"Traffic packet {i+1} sent")
            time.sleep(0.3)

        print("[RESULT] Traffic simulation finished\n")
