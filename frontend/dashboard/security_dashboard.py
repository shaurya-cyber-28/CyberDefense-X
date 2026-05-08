import tkinter as tk
from tkinter import scrolledtext


def launch_dashboard():

    window = tk.Tk()
    window.title("CyberDefense-X Security Dashboard")
    window.geometry("700x500")

    title = tk.Label(
        window,
        text="CyberDefense-X Security Monitor",
        font=("Arial", 16, "bold")
    )
    title.pack(pady=10)

    status = tk.Label(
        window,
        text="System Status: Running",
        fg="green",
        font=("Arial", 12)
    )
    status.pack(pady=5)

    alert_label = tk.Label(
        window,
        text="Security Alerts",
        font=("Arial", 12, "bold")
    )
    alert_label.pack(pady=5)

    log_box = scrolledtext.ScrolledText(
        window,
        width=80,
        height=20
    )
    log_box.pack(pady=10)

    log_box.insert(tk.END, "CyberDefense-X Initialized\n")
    log_box.insert(tk.END, "Monitoring network traffic...\n")

    window.mainloop()
