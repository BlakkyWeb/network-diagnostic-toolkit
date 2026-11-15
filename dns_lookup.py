import socket

def resolve_domain(domain):

    try:
        ip_address = socket.gethostbyname(domain)

        return{
            "Domain": domain,
            "IP Address": ip_address,
            "Status": "Success"
        }

    except socket.gaierror:
        return{
            "Domain": domain,
            "IP Address": None,
            "Status": "Failed",
            "Error": "Unable to resolve domain"
        }