import socket
import threading

class SocketTeleop(threading.Thread):
    def __init__(self, callback=None, host = '192.168.31.28', port = 65432,*args, **kwargs):
        # target = kwargs.pop('target')
        super(SocketTeleop, self).__init__(target=self.target_with_callback, *args, **kwargs)

        self.callback = callback

        self.host = host
        self.port = port

        self.is_running = False

        self.client = self.tel_connect()
    
    def target_with_callback(self):
        if self.callback is not None:
            while self.is_running:
                data = self.client.recv(1024)
                self.callback(data)
    
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
        self.is_running = False
        # self.client.close()
    
    def send_message(self, msg):
        if self.is_running:
            self.client.sendall(msg.encode())

def socket_callback(data):
    print(f'Received from server: {data.decode()}')

if __name__ == '__main__':
    soc_client = SocketTeleop(callback=socket_callback)
    soc_client.start()
    msg = input("send_vel: ")
    soc_client.send_message(msg)
