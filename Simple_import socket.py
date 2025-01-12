import socket
import threading

# COMMON VULNERABLE PORTS WITH DESCRIPTIONS
VULNERABLE_PORTS = {
    21: "FTP (Anonymous login vulnerability)",
    22: "SSH (Weak credentials or outdated versions)",
    23: "Telnet (Insecure communication)",
    80: "HTTP (Unpatched web servers, misconfigurations)",
    443: "HTTPS (SSL/TLS vulnerabilities)",
    445: "SMB (EternalBlue vulnerability)",
    3389: "RDP (Weak credentials or unpatched versions)"
}

def scan_port(ip, port):
    """
    Function to scan a single port and report if it's open and vulnerable.
    """
    try:
        # ATTEMPTED CONNECTION TO THE PORT
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((ip, port)) == 0:
                print(f"[OPEN] Port {port}: {VULNERABLE_PORTS.get(port, 'No known vulnerability')}")

    except socket.error:
        pass

def main():
    print("           ")
    print("           *** PORT SCANNER & VULNERABILITY DETECTORS ***")
    print("           ")
    ip = input("Enter the target IP address: ").strip()
    print("Scanning... Please wait.")

    # SCANS VARIOUS PORTS
    threads = []
    for port in range(1, 65536): 
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()

    
    for t in threads:
        t.join()

    print("\nScan complete")

if __name__ == "__main__":
    main()