#!/usr/bin/env python3
#Author ID: nmohammadiafshar

import subprocess

def free_space():
    # Run the command using subprocess.Popen and capture the output
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", shell=True, stdout=subprocess.PIPE)
    output = p.communicate()
    return output[0].decode('utf-8').strip()
    

if __name__ == "__main__":
    print(free_space())