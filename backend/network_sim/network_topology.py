class NetworkNode:

    def __init__(self, name, node_type):
        self.name = name
        self.node_type = node_type
        self.connections = []

    def connect(self, other_node):
        self.connections.append(other_node)


class NetworkTopology:

    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def display_topology(self):

        print("\n=== CyberDefense-X Network Topology ===")

        for node in self.nodes:
            connection_names = " ".join([c.name for c in node.connections])
            print(f"{node.name} ({node.node_type}) -> {connection_names}")


def create_default_topology():

    # Create nodes
    attacker = NetworkNode("Attacker", "Threat Actor")
    router = NetworkNode("Router", "Network Device")
    server = NetworkNode("Server", "Web Server")
    firewall = NetworkNode("Firewall", "Security Device")
    database = NetworkNode("Database", "Data Storage")

    # Create connections
    attacker.connect(router)
    router.connect(server)
    router.connect(firewall)
    firewall.connect(database)

    # Build topology
    topology = NetworkTopology()

    topology.add_node(attacker)
    topology.add_node(router)
    topology.add_node(server)
    topology.add_node(firewall)
    topology.add_node(database)

    return topology
