import subprocess
import csv

def run_nmap(target):
    """Add additonal Nmap tags here"""
    cmd = ["nmap", "-sV", "-oN", "nmap_results.txt", target]
    subprocess.run(cmd)

def run_nikto(target, open_ports):
    """Runs nikto"""
    cmd = ["nikto", "-host", target, "-port", open_ports, "-output", "nikto_results.txt"]
    subprocess.run(cmd)

def analyze_results():
    """Analyzes Nmap and Nikto results"""
    # Parse Nmap results
    with open("nmap_results.txt", "r") as nmap_file:
        nmap_data = csv.reader(nmap_file, delimiter="\t")
        # Process Nmap data

    # Parse Nikto results
    with open("nikto_results.txt", "r") as nikto_file:
        nikto_data = nikto_file.readlines()
        # Process Nikto data


if __name__ == "__main__":
    target = "192.168.1.1" # Specify target here 
    run_nmap(target)

    # Extracting open ports from nmap_results.txt
    with open("nmap_results.txt", "r") as nmap_file:
        nmap_data = csv.reader(nmap_file, delimiter="\t")
        open_ports = [row[-1] for row in nmap_data if "open" in row]

    run_nikto(target, ",".join(open_ports))
    analyze_results()
