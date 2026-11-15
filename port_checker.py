import socket

def check_tcp_port(host, port, timeout=3):

    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    sock.settimeout(timeout)

    try:
        result = sock.connect_ex((host, port))

        if result == 0:
            status = "Open"

        elif result == 10060:
            status = "Timed Out"

        else:
            status = "Not Reachable"

        return{
            "Host": host,
            "Port": port,
            "Status": status,
            "Error Code": result
        }

    except socket.timeout:
        return{
            "Host": host,
            "Port": port,
            "Status": "Timed Out",
            "Error": "Connection attempt exceeded timeout"
        }

    finally:
        sock.close()
