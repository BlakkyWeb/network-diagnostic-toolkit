import subprocess
import re

def check_host_availability(host, count=4):

    command = [
        "ping",
        "-4",
        "-n", str(count),
        "-w", "1000",
        host
    ]

    try:

        result = subprocess.run(
            command,
            capture_output= True,
            text= True,
            timeout=10
        )

        output = result.stdout

        received_match = re.search(
            r"Received\s*=\s*(\d+)",
            output
        )

        received = (
            int(received_match.group(1))
            if received_match else 0
        )

        packet_loss = (
            (count - received) / count
        ) * 100

        return{
            "Host": host,
            "Packets Sent": count,
            "Packets Received": received,
            "Packets Lost": count - received,
            "Packet Loss": f"{packet_loss:.2f}%",
            "Status": "Responding" if received > 0 else "No ICMP Response"
        }

    
    except subprocess.TimeoutExpired:

        return{
            "Host": host,
            "Status": "Timed Out",
            "Error": "Ping process exceeded 10 seconds"
        }