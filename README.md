# Network Diagnostic Toolkit

A Python-based network diagnostic application that checks DNS resolution, TCP host availability, and TCP connection latency. It also generates a JSON report containing the diagnostic results.

## Project Overview

The Network Diagnostic Toolkit was developed to apply Python programming to practical computer networking tasks. It combines several network diagnostic techniques in one application, allowing users to assess basic connectivity to a specific hostname or IP address.

The application performs DNS lookup, ICMP ping tests, TCP port checks, and repeated TCP connection latency measurements. Results are displayed in the terminal and saved as a JSON report for later inspection.

## Features

- **DNS Lookup:** Resolves a hostname to its corresponding IPv4 address.
- **ICMP Connectivity Test:** Checks whether a host responds to ping requests and calculates packets loss.
- **TCP Port Checking:** Checks connectivity on ports 22 (SSH), 80 (HTTP), and 443 (HTTPS).
- **TCP Latency Measurement:** Measures the time required to establish TCP connections and calculates average, minimum, and maximum latency.
- **JSON Reporting:** Saves the diagnostic results in a structured JSON file with a report generation timestamp.
- **Automated Testing:** Uses pytest to test the individual components of the application.

## Technologies and Libraries

The project uses Python and its standard library:

| Library | Purpose |
|---|---|
|`socket` | DNS resolution and TCP socket connections |
| `subprocess` | Executes system ping commands |
| `re` | Extracts packet statistics from ping output |
| `time` | Measures TCP connection latency |
| `json` | Generates structured diagnostic reports |
| `datetime` | Records report generation time |

**Testing:** `pytest` and Python's mocking utilities.


## Project Structure

```text
network_diagnostic_toolkit/
│
├── main.py
├── diagnostics.py
├── dns_lookup.py
├── port_checker.py
├── latency.py
├── report.py
│
├── tests/
│   ├── test_diagnostics.py
│   ├── test_dns_lookup.py
│   ├── test_latency.py
│   ├── test_port_checker.py
│   └── test_report.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

### Module Descriptiom

- `main.py`: Coordinates the diagnostic operations and displays the results.
- `dns_lookup`: Handles hostname resolution.
- `diagnostics.py`: Performs ICMP ping tests and calculates packet loss.
- `port_checker.py`: Checks TCP connectivity on specified ports.
- `latency.py`: Measures TCP connection latency and calculates summary statistics.
- `report.py`: Saves diagnostic results in JSON format.
- `tests/`: Contains automated tests for the application modules.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/BlakkyWeb/network-diagnostic-toolkit.git
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

Run the following command from the project directory:

```bash
python main.py
```

Enter a hostname or IPv4 address when prompted.

Example:

```text
Enter destination: google.com
```

The application will then:

1. Resolve the hostname through DNS.
2. Check host availability using ICMP.
3. Test TCP connectivity on ports 22, 80, and 443.
4. Measure TCP connection latency on these ports.
5. Display the diagnostic results.
6. Save the results to `network_report.json`.


The report is saved in the current working directory and is overwritten when a new report is generated using the default filename.

## Sample Diagnostic Results

The exact results depend on the destination host and network conditions.

```text
DNS
----------------------------------------
Domain: google.com
IP Address: <resolved IP address>
Status: Success

ICMP
----------------------------------------
Host: google.com
Packets Sent: 4
Packets Received: 4
Packets Lost: 0
Packet Loss: 0.00%
Status: Responding
```

TCP port and latency results are also displayed for each tested port.

## JSON Report

The application generates a file named:

```text
network_report.json
```

The report contains:
- The date and time the report was generated.
- DNS lookup results.
- ICMP connectivity results.
- TCP port connectivity results.
- TCP latency measurements.

## Running Automated Tests
The project uses `pytest` for automated testing.

Run the complete test suite with:

```bash
python -m pytest -v
```

The tests cover DNS resolution, ICMP responses, TCP port checking, latency measurements, and JSON report generation.

**Latest test result:** 11 tests passed.

## Technical Notes

- The current ICMP implementation uses the Windows `ping` command and its command-line options.
- TCP latency represents the time taken to establish a TCP connection. It is not a measurement of internet download speed or bandwidth.
- A falied ping does not necessarily mean that a host is offline. Some networks block ICMP traffic while allowing TCP connections.

## Future Improvements

Possible extensions include:

- Support for user-defined TCP ports.
- Network route tracing.
- More detailed diagnostic summaries.
- Exporting reports in additional formats.
- Cross-platform ICMP command support.

## Author

**Ajetomobi Praise Kayode**

Engineering Physics | Python | Networking