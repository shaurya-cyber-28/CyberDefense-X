import json
import time
import threading


class ReplayController:

    def __init__(self, scenario_file):
        self.scenario_file = scenario_file
        self.events = []
        self.current_index = 0
        self.is_paused = False
        self.is_stopped = False
        self.lock = threading.Lock()

    def load_scenario(self):
        with open(self.scenario_file, "r") as file:
            self.events = json.load(file)

    def reset(self):
        with self.lock:
            self.current_index = 0
            self.is_paused = False
            self.is_stopped = True

    def pause(self):
        with self.lock:
            self.is_paused = True

    def resume(self):
        with self.lock:
            self.is_paused = False


    def play(self, callback):
        start_time = time.time()

        while self.current_index < len(self.events):

            if self.is_stopped:
                return

            if self.is_paused:
                time.sleep(0.1)
                continue

            event = self.events[self.current_index]

            # adjust timing dynamically
            current_time = time.time() - start_time

            if current_time >= event["time"]:
                callback(event)
                self.current_index += 1
            else:
                time.sleep(0.05)
