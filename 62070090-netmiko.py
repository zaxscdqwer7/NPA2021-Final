from netmiko import ConnectHandler
import re

device_ip = '10.0.15.104'
username = 'admin'
password = 'cisco'

device_params = {
    'device_type': 'cisco_ios',
    'ip': device_ip,
    'username': username,
    'password': password
}

createLoopback = [
    "int lo62070090",
    "ip add 192.168.1.1 255.255.255.0",
    "no sh"
]

deleteLoopback = [
    "no int lo62070090"
]

with ConnectHandler(**device_params) as ssh:
    result = ssh.send_command('sh ip int br')
    if 'Loopback62070090' in result:
        ssh.send_config_set(deleteLoopback)
        ssh.save_config()
    else:
        ssh.send_config_set(createLoopback)
        ssh.save_config()
    result = ssh.send_command('sh ip int br')
    print(result)
