# Need to use Paramiko to ssh into the FreeBSD terminal on the NAS.

import paramiko
import subprocess, shlex 

server = "192.168.0.37" # Credentials
port = 22 # "TCP port found in the SSH options"
username = input("username:\t")
password = input("pass:\t")


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(server, port, username, password)

stdin0, stdout0, stderr0 = client.exec_command('ifconfig em0')

lines = stdout0.readlines() 

client.close()

if "1000baseT" in lines[7]:
    print("NAS box is not the limiting connection. ")
else: 
    print("NAS box is the limiting connection. ")

# Now need to run ethtool enp2s0 | grep -i speed 

command = 'ethtool enp2s0'
args = shlex.split(command)

output = subprocess.Popen(args, stdout = subprocess.PIPE, stderr=subprocess.STDOUT)

stdout, stderr = output.communicate()

stdout = str(stdout)

#print((stdout))

if 'Speed: 1000Mb/s\n\tDuplex: Full' in stdout:
    print("Computer is not limiting factor. ")
else: 
    print("Computer IS LIMITING FACTOR. ")