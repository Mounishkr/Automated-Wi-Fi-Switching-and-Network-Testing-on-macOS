# **Automated Wi-Fi Switching and Network Testing on macOS**  

## **Overview**  
This Python script automates the process of:  
- Connecting to two different Wi-Fi networks (SSIDs).  
- Identifying the **IP address** of the MacBook.  
- Running **10 ping requests** to test network connectivity.  
- Disconnecting from the first Wi-Fi network and connecting to the second one.  
- Repeating the IP check and ping test.  

This is useful for **network testing, troubleshooting, and performance comparison** between two Wi-Fi networks.  

---

## **Features**  
✅ Connects to Wi-Fi networks automatically.  
✅ Retrieves the IP address of the connected network.  
✅ Runs a **ping test** to Google's DNS (`8.8.8.8`).  
✅ Disconnects and reconnects to another SSID.  
✅ Works on **macOS** using `networksetup` and `ipconfig`.  

---

## **Requirements**  
📌 **Python 3.x** (Pre-installed on macOS)  
📌 **Admin/Sudo access** (for Wi-Fi management commands)  

---

## **Installation & Usage**  

### **1. Clone the Repository**  
```sh
git clone https://github.com/your-username/WiFi-Network-Test.git
cd WiFi-Network-Test
```

### **2. Update SSID & Passwords**  
Edit the `wifi_test.py` file and replace:  
```python
SSID_1 = "Your_First_SSID"
PASSWORD_1 = "Your_First_Password"

SSID_2 = "Your_Second_SSID"
PASSWORD_2 = "Your_Second_Password"
```
with your **actual Wi-Fi names and passwords**.  

### **3. Run the Script**  
```sh
python3 wifi_test.py
```
If you get permission errors, run:  
```sh
sudo python3 wifi_test.py
```

---

## **Expected Output**  
```
Connecting to FirstSSID...
Connected to FirstSSID. IP Address: 192.168.1.100
Running ping test...
10 packets transmitted, 10 received, 0% packet loss

Disconnecting Wi-Fi...
Connecting to SecondSSID...
Connected to SecondSSID. IP Address: 192.168.2.150
Running ping test...
10 packets transmitted, 10 received, 0% packet loss

Process Completed!
```

---

## **How It Works**  
1️⃣ **Connects to the first Wi-Fi (SSID 1)**  
2️⃣ **Fetches the IP address**  
3️⃣ **Runs a ping test** (10 packets)  
4️⃣ **Disconnects from SSID 1**  
5️⃣ **Connects to the second Wi-Fi (SSID 2)**  
6️⃣ **Fetches the new IP address**  
7️⃣ **Runs another ping test**  

---

## **Customization**  
- Change the **ping test target** by modifying:  
  ```python
  subprocess.run("ping -c 10 8.8.8.8", shell=True)
  ```
  (Replace `8.8.8.8` with your desired server.)  
- Add **logging** to save results to a file.  

---

## **License**  
📜 MIT License – Free to use and modify.  
