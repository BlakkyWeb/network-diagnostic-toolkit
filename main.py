from dns_lookup import resolve_domain
from diagnostics import check_host_availability
from port_checker import check_tcp_port
from latency import measure_tcp_latency
from report import save_report


def run_diagnostics(host):

    results = {}

    # 1. DNS lookup
    print("\nRunning DNS lookup...")
    results["DNS"] = resolve_domain(host)

    # 2. ICMP availability
    print("\nChecking host availability...")
    results["ICMP"] = check_host_availability(host)

    # 3. TCP port checks
    print("\nChecking TCP ports...")

    ports = [22, 80, 443]
    results["TCP Ports"] = {}

    for port in ports:
        results["TCP Ports"][str(port)] = check_tcp_port(host, port)

    # 4. TCP latency measurements
    print("\nMeasuring TCP connection latency")

    results["TCP Latency"] = {}

    for port in ports:
        results["TCP Latency"][str(port)] = measure_tcp_latency(host, port, tests=5)

    return results

def display_results(results, level=0):

    for key, value in results.items():
        indent = " " * level

        if isinstance(value, dict):
            if level == 0:
                print(f"\n{key.upper()}")
                print("-" * 40)

            else:
                print(f"\n{indent}{key}:")

            display_results(value, level + 1)

        else:
            print(f"{indent}{key}: {value}")






def main():

    host = input("Enter destination: ").strip()

    if not host:

        print("Please enter a valid hostname or IP address.")
        return

    results = run_diagnostics(host)

    display_results(results)

    filename = save_report(results)

    print("\n" + "=" * 50)
    print(f"Report saved successfuly: {filename}")
    print("=" * 50)


if __name__ == "__main__":
    main()