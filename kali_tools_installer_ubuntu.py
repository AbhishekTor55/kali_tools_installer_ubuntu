#!/usr/bin/env python3

import os
import subprocess

def run_command(command):
    """Runs a shell command and displays the output."""
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def add_kali_repo():
    """Add Kali Linux repositories to the system."""
    print("[*] Adding Kali Linux repositories...")
    repo_lines = """deb http://http.kali.org/kali kali-rolling main non-free contrib
deb-src http://http.kali.org/kali kali-rolling main non-free contrib"""
    
    with open("/etc/apt/sources.list", "a") as file:
        file.write("\n" + repo_lines + "\n")
    
    print("[*] Repositories added successfully!")

    print("[*] Adding Kali GPG key...")
    run_command("wget -q -O - https://archive.kali.org/archive-key.asc | sudo apt-key add -")
    print("[*] GPG key added successfully!")

def install_kali_tools():
    """Install specific Kali Linux tools or metapackages."""
    print("\n[1] Install Top 10 Tools (kali-linux-top10)")
    print("[2] Install Default Tools (kali-linux-default)")
    print("[3] Install All Tools (kali-linux-everything)")
    print("[4] Install Custom Tools")
    choice = input("\nEnter your choice: ")

    if choice == "1":
        run_command("sudo apt update && sudo apt install -y kali-linux-top10")
    elif choice == "2":
        run_command("sudo apt update && sudo apt install -y kali-linux-default")
    elif choice == "3":
        run_command("sudo apt update && sudo apt install -y kali-linux-everything")
    elif choice == "4":
        tools = input("Enter tool names separated by space (e.g., nmap hydra): ")
        run_command(f"sudo apt update && sudo apt install -y {tools}")
    else:
        print("Invalid choice!")

def remove_kali_repo():
    """Remove Kali Linux repositories."""
    print("[*] Removing Kali Linux repositories...")
    with open("/etc/apt/sources.list", "r") as file:
        lines = file.readlines()
    
    with open("/etc/apt/sources.list", "w") as file:
        for line in lines:
            if "kali" not in line:
                file.write(line)
    
    print("[*] Repositories removed successfully!")

def main_menu():
    """Display the main menu."""
    while True:
        print("\n--- Kali Tools Installer ---")
        print("[1] Add Kali Repositories")
        print("[2] Install Kali Tools")
        print("[3] Remove Kali Repositories")
        print("[4] Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_kali_repo()
        elif choice == "2":
            install_kali_tools()
        elif choice == "3":
            remove_kali_repo()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("Please run this script as root!")
    else:
        main_menu()
