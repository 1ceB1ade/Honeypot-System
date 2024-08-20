import socket
import threading
import logging
from datetime import datetime

SETTINGS = {
    "logging": {
        "log_file": "honeypot.log",
        "log_level": logging.INFO,
    },
    "alerting": {
        "enabled": True,
        "alert_message": "ALERT! Suspicious activity detected from {ip} on {service} service."
    },
    "services": [
        {"ip": "0.0.0.0", "port": 22, "name": "SSH"},
        {"ip": "0.0.0.0", "port": 80, "name": "HTTP"}
    ]
}

logging.basicConfig(filename=SETTINGS["logging"]["log_file"], 
                    level=SETTINGS["logging"]["log_level"], 
                    format='%(asctime)s - %(message)s')

def alert_admin(ip, service, data):
    if SETTINGS["alerting"]["enabled"]:
        alert_message = SETTINGS["alerting"]["alert_message"].format(ip=ip, service=service)
        logging.warning(alert_message)

class ServiceEmulator:
    def __init__(self, ip='0.0.0.0', port=22, service_name='SSH'):
        self.ip = ip
        self.port = port
        self.service_name = service_name
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.ip, self.port))
        self.sock.listen(5)
        logging.info(f"{self.service_name} service started on {self.ip}:{self.port}")

    def start(self):
        while True:
            client, addr = self.sock.accept()
            logging.info(f"Connection attempt on {self.service_name} from {addr[0]}")
            threading.Thread(target=self.handle_client, args=(client, addr)).start()

    def handle_client(self, client, addr):
        try:
            data = client.recv(1024).decode('utf-8')
            logging.info(f"Received data from {addr[0]} on {self.service_name}: {data}")
            client.send(f"{self.service_name} access denied.\n".encode('utf-8'))
            alert_admin(addr[0], self.service_name, data)
        except Exception as e:
            logging.error(f"Error handling client {addr[0]}: {e}")
        finally:
            client.close()

class Honeypot:
    def __init__(self):
        self.services = []

    def load_services(self):
        for service in SETTINGS["services"]:
            self.services.append(ServiceEmulator(service['ip'], service['port'], service['name']))

    def start(self):
        self.load_services()
        for service in self.services:
            threading.Thread(target=service.start).start()

if __name__ == "__main__":
    honeypot = Honeypot()
    honeypot.start()
