from vpython import *
import time

def visualize_network(attack_path=None):

    scene.title = "CyberDefense-X 3D Attack Simulation"
    scene.background = color.black
    scene.width = 1200
    scene.height = 700

    # Node positions in 3D
    attacker_pos = vector(-8,0,0)
    router_pos = vector(-3,1,0)
    server_pos = vector(0,3,0)
    firewall_pos = vector(3,-1,0)
    database_pos = vector(7,0,0)

    # Create nodes
    attacker = sphere(pos=attacker_pos, radius=0.6, color=color.red, emissive=True)
    router = sphere(pos=router_pos, radius=0.6, color=color.cyan, emissive=True)
    server = sphere(pos=server_pos, radius=0.6, color=color.green, emissive=True)
    firewall = sphere(pos=firewall_pos, radius=0.6, color=color.orange, emissive=True)
    database = sphere(pos=database_pos, radius=0.6, color=color.blue, emissive=True)

    label(pos=attacker.pos, text="Attacker", xoffset=20, height=12)
    label(pos=router.pos, text="Router", xoffset=20, height=12)
    label(pos=server.pos, text="Server", xoffset=20, height=12)
    label(pos=firewall.pos, text="Firewall", xoffset=20, height=12)
    label(pos=database.pos, text="Database", xoffset=20, height=12)

    # Network links
    curve(pos=[attacker_pos, router_pos], radius=0.05, color=color.white)
    curve(pos=[router_pos, server_pos], radius=0.05, color=color.white)
    curve(pos=[server_pos, firewall_pos], radius=0.05, color=color.white)
    curve(pos=[firewall_pos, database_pos], radius=0.05, color=color.white)

    # Packet
    packet = sphere(pos=attacker_pos, radius=0.25, color=color.yellow, make_trail=True)

    path = [
        attacker_pos,
        router_pos,
        server_pos,
        firewall_pos,
        database_pos
    ]

    # Animation
    for i in range(len(path)-1):

        start = path[i]
        end = path[i+1]

        for step in range(100):

            rate(120)

            packet.pos = start + (end-start)*(step/100)

            # Camera follows packet (POV feel)
            scene.camera.pos = packet.pos + vector(-1,0.5,1)
            scene.camera.axis = packet.pos - scene.camera.pos

    # Attack reached database
    explosion = sphere(pos=database_pos, radius=0.5, color=color.red, opacity=0.6)
    for i in range(20):
        rate(60)
        explosion.radius += 0.2
        explosion.opacity -= 0.03
