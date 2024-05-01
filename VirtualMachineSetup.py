import subprocess

def setup_virtual_machine():
    """
    Sets up a virtual machine environment using VirtualBox.
    This function automates the creation and configuration of a new virtual machine.
    """
    try:
        # Check if VirtualBox is installed
        subprocess.run(["VBoxManage", "--version"], check=True)

        # Create a new virtual machine
        vm_name = "HackerVM"
        print(f"Creating virtual machine: {vm_name}")
        subprocess.run(["VBoxManage", "createvm", "--name", vm_name, "--register"], check=True)

        # Set the VM's system properties
        print("Configuring system properties...")
        subprocess.run(["VBoxManage", "modifyvm", vm_name, "--memory", "2048", "--cpus", "2", "--vram", "128"], check=True)

        # Setup storage
        print("Setting up storage...")
        subprocess.run(["VBoxManage", "createhd", "--filename", f"{vm_name}_Disk.vdi", "--size", "50000"], check=True)
        subprocess.run(["VBoxManage", "storagectl", vm_name, "--name", "SATA Controller", "--add", "sata", "--controller", "IntelAhci"], check=True)
        subprocess.run(["VBoxManage", "storageattach", vm_name, "--storagectl", "SATA Controller", "--port", "0", "--device", "0", "--type", "hdd", "--medium", f"{vm_name}_Disk.vdi"], check=True)

        # Install an operating system from an ISO image
        print("Installing operating system...")
        iso_path = "/path/to/your/iso_file.iso"
        subprocess.run(["VBoxManage", "storageattach", vm_name, "--storagectl", "SATA Controller", "--port", "1", "--device", "0", "--type", "dvddrive", "--medium", iso_path], check=True)
        subprocess.run(["VBoxManage", "startvm", vm_name], check=True)

        print("Virtual machine setup complete.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    setup_virtual_machine()
