ports = {
    20: "FTP",
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    67: "DHCP",
    68: "DHCP",
    69: "TFTP",
    80: "HTTP",
    110: "POP3",
    123: "NTP",
    143: "IMAP",
    161: "SNMP",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    993: "IMAPS",
    995: "POP3S",
}

try:
    while True:
        port = int(input("Enter a Port number: "))
        service = ports.get(port)
        if service is None:
            print("Not available ...")
        else:
            print(f"Port {port}: {service}")

except Exception:
    print("Exit Successfully ...")