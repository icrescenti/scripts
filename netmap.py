# Linux only atm
import subprocess

def ping(host):
    command = ['ping', host, '-c', '1', '-s', '1', '-W', '3']

    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) == 0

# Your subnet
subnet = '192.168.0.'
for ip in range(1, 256):
    if(ping(subnet + str(ip))):
        print(subnet + str(ip))