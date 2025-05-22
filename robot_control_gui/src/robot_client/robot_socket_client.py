import socket
import json

class RobotSocketClient:
    def __init__(self, host = 'localamr.local', port = 65432):

        self.host = host
        self.port = port

        self.current_vel = 0.0
        self.current_ang = 0.0

        self.max_vel = 0.3

        self.client = self.__tel_connect()
    
    def __tel_connect(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.host, self.port))
            print(f'Connected to server {self.host}:{self.port}')
            self.is_running = True
            return s
        except Exception as e:
            print("Could not connect", e)
            return
    
    def close(self):
        self.stop()
        self.client.close()
    
    def is_connected(self):
        if self.client:
            try:
                self.client.sendall(b'')
                return True
            except Exception as e:
                print("Connection error", e)
                return False
        return False
    
    def __send_vel(self, x, z):
        self.current_vel = x
        self.current_ang = z
        msg = {
            "header": "velocity",
            "x": x,
            "z": z
        }

        self.__send_message(json.dumps(msg))
    
    def stop(self):
        self.__send_vel(0.0, 0.0)
    
    def move_forward(self, speed:float):
        if speed < 0.0:
            raise ValueError("Speed must be positive")
        self.current_vel = speed
        self.__send_vel(self.current_vel, 0.0)
    
    def move_backward(self, speed:float):
        if speed < 0.0:
            raise ValueError("Speed must be positive")
        self.current_vel = -speed
        self.__send_vel(self.current_vel, 0.0)
    
    def increase_vel(self, d=0.02):
        if self.current_vel < 0.0:
            self.current_vel -= d
        else:
            self.current_vel += d
        self.__send_vel(self.current_vel, 0.0)
    def decrease_vel(self, d=0.02):
        if self.current_vel < 0.0:
            self.current_vel += d
            if self.current_vel > 0.0:
                self.current_vel = 0.0
        else:
            self.current_vel -= d
            if self.current_vel < 0.0:
                self.current_vel = 0.0
        self.__send_vel(self.current_vel, 0.0)
    
    def turn_left(self, speed:float):
        if speed < 0.0:
            raise ValueError("Speed must be positive")
        self.current_ang = speed
        self.__send_vel(0.0, self.current_ang)
    
    def turn_right(self, speed:float):
        if speed < 0.0:
            raise ValueError("Speed must be positive")
        self.current_ang = -speed
        self.__send_vel(0.0, self.current_ang)
    
    def __send_color(self, color):
        msg = {
            "header": "led_control",
            "led_command": color
        }

        self.__send_message(json.dumps(msg))
    
    def set_red(self):
        self.__send_color("r")
    
    def set_green(self):
        self.__send_color("g")
    
    def set_blue(self):
        self.__send_color("m")
    
    def set_yellow(self):
        self.__send_color("y")
    
    def start_animation(self):
        self.__send_color("i")
    
    def __send_message(self, msg):
        print(f'Sending message: {msg}')
        if self.is_running:
            self.client.sendall(msg.encode())


if __name__ == '__main__':
    soc_client = RobotSocketClient()
    while True:
        msg = input("send_vel: ")
        # soc_client.send_vel(0.12, 0.0)
        soc_client.set_red()
    # soc_client.stop()
    # soc_client.send_message(msg)