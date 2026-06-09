import socket
from common_ports import ports_and_services


def get_open_ports(target, port_range, verbose=False):
    open_ports = []
    is_hostname = False
    hostname = ""
    ip = ""

    # Determine if target is hostname or IP
    # Check if it looks like an IP (only digits and dots)
    def looks_like_ip(s):
        return all(c.isdigit() or c == "." for c in s)

    if looks_like_ip(target):
        # Validate as proper IPv4
        parts = target.split(".")
        if len(parts) != 4:
            return "Error: Invalid IP address"
        try:
            if not all(0 <= int(p) <= 255 for p in parts):
                return "Error: Invalid IP address"
        except ValueError:
            return "Error: Invalid IP address"
        ip = target
    else:
        is_hostname = True
        hostname = target

    # Resolve hostname to IP
    if is_hostname:
        try:
            ip = socket.gethostbyname(hostname)
        except socket.gaierror:
            return "Error: Invalid hostname"
    else:
        # If it's an IP, try reverse lookup for verbose mode
        if verbose:
            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except socket.herror:
                hostname = ""

    # Scan ports
    for port in range(port_range[0], port_range[1] + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except Exception:
            pass

    if not verbose:
        return open_ports

    # Verbose mode
    display_name = hostname if hostname else ip
    header = f"Open ports for {display_name} ({ip})\n"
    header += "PORT     SERVICE\n"

    rows = ""
    for port in open_ports:
        service = ports_and_services.get(port, "unknown")
        rows += f"{port:<9}{service}\n"

    return header + rows