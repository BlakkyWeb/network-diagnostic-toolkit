import socket
import time

def measure_tcp_latency(host, port, tests=5, timeout=3):
    
    if tests < 1:
        raise ValueError("Number of tests must be atleast 1")

    # Resolve Hostname
    try:
       ip_address = socket.gethostbyname(host) 

    except socket.gaierror as error:
        return{
            "Host": host,
            "Port": port,
            "Status": "DNS Resolution Failed",
            "Error": str(error)
        }

    latencies = []
    failed_tests = 0

    for _ in range(tests):

        try:

            start_time = time.perf_counter()

            with socket.create_connection(
                (ip_address, port),
                timeout=timeout
            ):
                end_time = time.perf_counter()

            elapsed_time = (end_time - start_time) * 1000

            latencies.append(elapsed_time)

        except socket.timeout:
            failed_tests += 1
            print(f"Connection timed out")

        except OSError:
            failed_tests += 1
            print(f"Connection error")

    successful_test = len(latencies)

    # If every connection fails?
    if successful_test == 0:
        return{
            "Host": host,
            "IP Address": ip_address,
            "Port": port,
            "Tests Requested": tests,
            "Successful Tests": 0,
            "Failed Tests": failed_tests,
            "Status": "All Connections Failed"
        }

    if successful_test == 0:
        status = "All Connections Falied"
    elif failed_tests > 0:
        status = "Partially Completed"
    else: status = "Completed"

    # Calculate latency stats
    average_latency = sum(latencies)/successful_test
    mininnum_latency = min(latencies)
    maximum_latency = max(latencies)

    return{
        "Host": host,
        "IP Address": ip_address,
        "Port": port,
        "Test Requested": tests,
        "Successful Tests": successful_test,
        "Failed Tests": failed_tests,
        "Average Latency (ms)": round(average_latency, 2),
        "Minimum Latency (ms)": round(mininnum_latency, 2),
        "Maximum Latency (ms)": round(maximum_latency, 2),
        "Individual Measurements (ms)": [
            round(value, 2) for value in latencies
        ],
        "Status": status
    }