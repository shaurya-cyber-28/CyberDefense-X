import random
import time

class TrafficSimulator:

    def __init__(self, network):
        self.network = network

    def generate_normal_traffic(self):

        nodes = list(self.network.nodes())

        source = random.choice(nodes)
        destination = random.choice(nodes)

        while source == destination:
            destination = random.choice(nodes)

        packet = {
            "type": "NORMAL",
            "source": source,
            "destination": destination
        }

        return packet

    def generate_attack_traffic(self):

        packet = {
            "type": "ATTACK",
            "source": "Attacker",
            "destination": "WebServer"
        }

        return packet
