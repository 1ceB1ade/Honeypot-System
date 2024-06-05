import socket
import threading

services = [
    ('ftp', 21),
    ('ssh', 22),
    ('telnet', 23),
    ('smtp', 25),
    ('dns', 53),
    ('http', 80),
    ('https', 443)
]

def handle_client(client_socket, address):
    try:
        data = client_socket.recv(1024).decode()
        print(f"Received data from {address}: {data}")
        
        with open('attackers.log', 'a') as log_file:
            log_file.write(f"{address[0]}\n")
        
        client_socket.send("Access denied. This is a honeypot system.".encode())
    except Exception as e:
        print(f"Error handling client {address}: {str(e)}")
    finally:
        client_socket.close()

def start_honeypot(service_name, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(5)
    print(f"Honeypot for {service_name} is running on port {port}")
    
    while True:
        client_socket, address = server_socket.accept()
        print(f"New connection from {address}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()
for service_name, port in services:
    honeypot_thread = threading.Thread(target=start_honeypot, args=(service_name, port))
    honeypot_thread.start()
