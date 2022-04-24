#!/usr/bin/env python3

import subprocess
import time
from colorama import Fore,Style,Back
from progress.bar import Bar

#coded by g0dmax55

def bar():
    bar = Bar('Processing', max=100)
    for i in range(100):
        bar.next()
        time.sleep(.01)
    bar.finish()
    print("")

def packages():
    try:
        subprocess.call(["sudo", "apt-get", "clean"], stdout=subprocess.DEVNULL)
        subprocess.call(["clear"])
        time.sleep(3)
        print(Fore.RED + "[*] Updateing")
        subprocess.call(["sudo", "apt-get", "update"], stdout=subprocess.DEVNULL)
        bar()
        print("[*] Upgrading")
        subprocess.call(["sudo", "apt-get", "upgrade", "-y"], stdout=subprocess.DEVNULL)
        bar()
        print("[*] Dist-Upgrading")
        subprocess.call(["sudo", "apt-get", "dist-upgrade", "-y"], stdout=subprocess.DEVNULL)
        bar()
        print("[+] Installing Wget")
        subprocess.call(["sudo", "apt-get", "install", "wget", "-y"], stdout=subprocess.DEVNULL)
        bar()
        print("[+] Installing Net-Tools")
        subprocess.call(["sudo", "apt-get", "install", "net-tools", "-y"], stdout=subprocess.DEVNULL)
        bar()
        print("[+] Installing Gpg")
        subprocess.call(["sudo", "apt-get", "install", "gpg", "-y"], stdout=subprocess.DEVNULL)
        bar()
        print("[+] Installing Vs-Code")
        subprocess.call(["wget", "https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64", "-O", "code.deb"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        subprocess.call(["sudo", "apt-get", "install", "-f", "./code.deb"], stdout=subprocess.DEVNULL)
        subprocess.call(["rm", "code.deb"])
        bar()
        print("[+] Installing Nmap")
        subprocess.call(["sudo", "apt-get", "install", "nmap", "-y"], stdout=subprocess.DEVNULL)
        bar()
        print("[+] Installing Sublime")
        subprocess.call(["wget", "https://download.sublimetext.com/sublime-text_build-3211_amd64.deb", "-O", "sublime.deb"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        subprocess.call(["sudo", "apt-get", "install", "-f", "./sublime.deb"], stdout=subprocess.DEVNULL)
        subprocess.call(["rm", "sublime.deb"])
        bar()
        print("[+] Installing Tshark")
        subprocess.call(["sudo", "apt-get", "install", "tshark", "-y"], stdout=subprocess.DEVNULL)
        bar()
        print("[+] Installing Fuzz")
        subprocess.call(["sudo", "apt-get", "install", "fuzz", "-y"], stdout=subprocess.DEVNULL)
        bar()
        print("[+] Installing Terminator")
        subprocess.call(["sudo", "apt-get", "install", "terminator", "-y"], stdout=subprocess.DEVNULL)
        bar()
        print("[+] Installing Metasploit")
        subprocess.call(["curl", "https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb", "-o", "msfinstall"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        subprocess.call(["chmod", "+x", "msfinstall"])
        subprocess.call(["./msfinstall"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        subprocess.call(["rm", "msfinstall"])
        bar()
        print("[+] Installing Hydra")
        subprocess.call(["sudo", "apt-get", "install", "hydra", "-y"], stdout=subprocess.DEVNULL)
        bar()
        print("[+] Installing Curl")
        subprocess.call(["sudo", "apt-get", "install", "curl", "-y"], stdout=subprocess.DEVNULL)
        bar()
        print("[+] Installing John")
        subprocess.call(["sudo", "apt-get", "install", "john", "-y"], stdout=subprocess.DEVNULL)
        bar()
        print("[+] Installing Hashcat")
        subprocess.call(["sudo", "apt-get", "install", "hashcat", "-y"], stdout=subprocess.DEVNULL)
        bar()
        print("[+] Installing Bmon")
        subprocess.call(["sudo", "apt-get", "install", "bmon", "-y"], stdout=subprocess.DEVNULL)
        bar()
        print("[+] Installing Wireshark")
        subprocess.call(["sudo", "apt-get", "install", "wireshark", "-y"], stdout=subprocess.DEVNULL)
        bar()
        print("[+] Installing Bashtop")
        subprocess.call(["sudo", "apt-get", "install", "bashtop", "-y"], stdout=subprocess.DEVNULL)
        bar()
        print("[+] Installing Aircrack-Ng")
        subprocess.call(["sudo", "apt-get", "install", "aircrack-ng", "-y"], stdout=subprocess.DEVNULL)
        bar()
        print("[+] Installing Wifite")
        subprocess.call(["sudo", "apt-get", "install", "wifite", "-y"], stdout=subprocess.DEVNULL)
        bar()
        print("[+] Installing Netcat")
        subprocess.call(["sudo", "apt-get", "install", "netcat", "-y"], stdout=subprocess.DEVNULL)
        bar()
        print("[+] Installing Tor")
        subprocess.call(["sudo", "apt-get", "install", "tor", "-y"], stdout=subprocess.DEVNULL)
        bar()
        print("[+] Installing Proxy-Chains")
        subprocess.call(["sudo", "apt-get", "install", "proxychains", "-y"], stdout=subprocess.DEVNULL)
        bar()
        time.sleep(3)
        print("[*] Finish")

    except KeyboardInterrupt:
        print("")

packages()


