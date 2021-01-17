import subprocess
from subprocess import PIPE
import os
import time
import threading
from ..helpers.status import is_open

class ServerHandler():
    def __init__(self):
        self.thread = None
        self.process = None

    def start_server(self):
        self.set_up_server()
        #self.thread = threading.Thread(target=self.read_output)
        #self.thread.start()

    def set_up_server(self):
        if is_open():
            raise Exception("Server already running or port is busy")
        
        os.chdir("mc_server")
        self.process = subprocess.Popen(["java", "-Xmx2048M", "-Xms2048M", "-jar", "server.jar"], stdout=PIPE, stdin=PIPE, stderr=PIPE)
        os.chdir("../")

    def shut_down(self):
        self.input_command("stop\n")
        self.read = False
        self.thread = None

    def input_command(self, command):
        self.process.stdin.flush()
        self.process.stdin.write(command.encode("utf-8"))

    def read_output(self):
        self.read = True
        while self.read:
            out = self.process.stdout.readline().strip()
            if out != "":
                print(out)

serverHandler = ServerHandler()