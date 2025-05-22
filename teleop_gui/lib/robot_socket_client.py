import socket
import json

class SocketTeleop:
    def __init__(self, callback=None, host = 'localamr.local', port = 65432):

        self.host = host
        self.port = port

        self.client = self.tel_connect()
    
    def tel_connect(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.host, self.port))
            print(f'Connected to server {self.host}:{self.port}')
            self.is_running = True
            return s
        except Exception as e:
            print("Could not connect", e)
            return
    
    def stop(self):
        self.client.close()
    
    def send_vel(self, x, z):
        msg = {
            "header": "velocity",
            "x": x,
            "z": z
        }

        self.send_message(json.dumps(msg))
    
    def send_color(self, color):
        msg = {
            "header": "led_control",
            "led_command": color
        }

        self.send_message(json.dumps(msg))
    
    def set_red(self):
        self.send_color("r")
    
    def set_green(self):
        self.send_color("g")
    
    def set_blue(self):
        self.send_color("m")
    
    def set_yellow(self):
        self.send_color("y")
    
    def start_animation(self):
        self.send_color("i")
    
    def send_message(self, msg):
        print(f'Sending message: {msg}')
        if self.is_running:
            self.client.sendall(msg.encode())


if __name__ == '__main__':
    soc_client = SocketTeleop()
    while True:
        msg = input("send_vel: ")
        # soc_client.send_vel(0.12, 0.0)
        soc_client.set_red()
    # soc_client.stop()
    # soc_client.send_message(msg)