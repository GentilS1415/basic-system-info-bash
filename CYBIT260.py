#CYBIT 260 Bash Script Assignment
#Basic System Info

bash_script_content = """#!/bin/bash
echo "Hello World!"
echo "Hostname: $(hostname)"
echo "Current date and time: $(date)"
echo "System uptime: $(uptime)"
echo "Linux Kernel Version: $(uname -r)"
echo "Memory Information: $(free -h)"
echo "Network Interface Information: $(ip address)"
"""

with open("CYBIT260_script.sh", "w") as file:
    file.write(bash_script_content)

import os
os.chmod("CYBIT260_script.sh", 0o755)

import subprocess
subprocess.run(["./CYBIT260_script.sh"])