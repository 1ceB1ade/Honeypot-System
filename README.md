# Honeypot System for Simulated Vulnerable Services

This is a simple honeypot system designed to detect and log potential attackers targeting a list of simulated vulnerable services. It's implemented in Python using sockets and threading.

## How it Works

The system listens on multiple ports corresponding to commonly targeted services such as FTP, SSH, Telnet, SMTP, DNS, HTTP, and HTTPS. Whenever a connection is established with one of these ports, it logs the IP address of the connecting client and sends a predefined response indicating that access is denied, simulating a vulnerable system.

## Setup

To run this honeypot system, follow these steps:

1. Clone this repository to your local machine.

2. Ensure you have Python installed (version 3.x).

3. Open a terminal or command prompt and navigate to the directory containing the cloned repository.

4. Run the Python script `honeypot.py` using the command:
    ```
    python honeypot.py
    ```

5. The honeypot system will start listening on the specified ports for incoming connections.

## Simulated Vulnerable Services

The following services are simulated in this honeypot system:

- FTP (Port 21)
- SSH (Port 22)
- Telnet (Port 23)
- SMTP (Port 25)
- DNS (Port 53)
- HTTP (Port 80)
- HTTPS (Port 443)

## Logging

The system logs the IP addresses of potential attackers in the file `attackers.log`. You can review this log file to identify suspicious activity.

## Disclaimer

This honeypot system is for educational and research purposes only. It should not be used in any malicious or unauthorized activities. By using this software, you agree to comply with all applicable laws and regulations.

## Contributing

Contributions are welcome! If you have suggestions for improvements or encounter any issues, feel free to submit a pull request or open an issue on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
