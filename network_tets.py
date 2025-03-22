import subprocess
import time

# SSID and Passwords
SSID_1 = "7a"
PASSWORD_1 = "1234567890"

SSID_2 = "S24+"
PASSWORD_2 = "1234567890"

def connect_wifi(ssid, password):
    """ Connects to the specified Wi-Fi network on macOS """
    print(f"Connecting to {ssid}...")
    cmd = f"""networksetup -setairportnetwork en0 "{ssid}" "{password}" """
    subprocess.run(cmd, shell=True, check=True)
    time.sleep(5)  # Wait for connection

def get_ip():
    """ Retrieves the current IP address """
    cmd = "ipconfig getifaddr en0"
    ip_address = subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout.strip()
    return ip_address if ip_address else "No IP assigned"

def run_ping():
    """ Runs ping test to Google DNS (8.8.8.8) """
    print("Running ping test...")
    subprocess.run("ping -c 10 8.8.8.8", shell=True)

def disconnect_wifi():
    """ Disconnects Wi-Fi by turning it off and on """
    print("Disconnecting Wi-Fi...")
    subprocess.run("networksetup -setairportpower en0 off", shell=True)
    time.sleep(3)
    subprocess.run("networksetup -setairportpower en0 on", shell=True)
    time.sleep(5)

# **Process Execution**
# Connect to 1st SSID
connect_wifi(SSID_1, PASSWORD_1)
time.sleep(10)  # Ensure stable connection
print(f"Connected to {SSID_1}. IP Address: {get_ip()}")
run_ping()

# Disconnect and connect to 2nd SSID
disconnect_wifi()
connect_wifi(SSID_2, PASSWORD_2)
time.sleep(10)  # Ensure stable connection
print(f"Connected to {SSID_2}. IP Address: {get_ip()}")
run_ping()

print("Process Completed!")
