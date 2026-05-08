import socket

def get_ip_from_hostname(hostname):
    ip = socket.gethostbyname(hostname)
    if ip:
        return ip
    else:
        return "Something Wrong!"

