```python
# main.py
# This is the main script for the hacking simulation project, coordinating all other modules.

from ZeroDayExploit import exploit_zero_day
from BackdoorScript import inject_backdoor
from SandboxEscape import escape_sandbox
from PhishingLinkGenerator import generate_phishing_link
from Keylogger import install_keylogger
from DatabaseAccess import access_database
from DDoSAttack import perform_ddos_attack
from DataAnalysis import analyze_data
from VirtualMachineSetup import setup_virtual_machine

def main():
    # Setup a virtual environment for safe simulation
    vm_details = setup_virtual_machine()
    print(f"Virtual machine set up at IP: {vm_details['ip']}")

    # Target system details
    target_url = "http://tianwang-bank.com/api"
    target_system_ip = "192.168.1.100"

    # Step 1: Exploit zero-day vulnerability
    if exploit_zero_day(target_url):
        # Step 2: Inject backdoor
        if inject_backdoor(target_system_ip):
            # Step 3: Escape from sandbox (if necessary)
            if escape_sandbox():
                # Step 4: Generate and send phishing link
                target_email = "employee@tianwang-bank.com"
                phishing_link = generate_phishing_link(target_email)
                print(f"Phishing link generated and sent to {target_email}: {phishing_link}")

                # Step 5: Install keylogger via phishing
                if install_keylogger(target_system_ip):
                    # Step 6: Access database
                    database_credentials = access_database(target_system_ip)
                    if database_credentials:
                        print("Accessed database successfully.")

                        # Step 7: Perform data analysis
                        valuable_data = analyze_data(database_credentials)
                        print(f"Data analysis complete. Found {len(valuable_data)} valuable entries.")

                        # Step 8: Prepare to extract data
                        # Simulate a DDoS attack to distract and cover tracks
                        if perform_ddos_attack(target_system_ip):
                            print("DDoS attack launched, extracting data...")
                            # Data extraction logic here
                        else:
                            print("Failed to launch DDoS attack.")
                    else:
                        print("Failed to access database.")
                else:
                    print("Failed to install keylogger.")
            else:
                print("Failed to escape sandbox.")
        else:
            print("Failed to inject backdoor.")
    else:
        print("Failed to exploit zero-day vulnerability.")

if __name__ == "__main__":
    main()
```
