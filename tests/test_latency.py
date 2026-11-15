from contextlib import nullcontext
import socket

from latency import measure_tcp_latency

def test_successful_latency(monkeypatch):

    # Simulate successful DNS resolution

    monkeypatch.setattr(
        "latency.socket.gethostbyname",
        lambda host: "142.250.129.100"
    )

    # Stimulate successful TCP connnections

    monkeypatch.setattr(
        "latency.socket.create_connection",
        lambda *args, **kwargs: nullcontext()
    )

    # Simulate connection timing

    times = iter([1.0, 1.025, 2.0, 2.050])

    monkeypatch.setattr(
        "latency.time.perf_counter",
        lambda: next(times)
    )

    result = measure_tcp_latency(
        "google.com", 443, tests=2
    )

    assert result["Successful Tests"] == 2
    assert result["Failed Tests"] == 0
    assert result["Average Latency (ms)"] == 37.5
    assert result["Minimum Latency (ms)"] == 25.0
    assert result["Maximum Latency (ms)"] == 50.0
    assert result["Status"] == "Completed"

def test_failed_connections(monkeypatch):

    monkeypatch.setattr(
        "latency.socket.gethostbyname",
        lambda host: "142.250.129.100"
    )

    def mock_connection(*args, **kwargs):
        raise socket.timeout("Connection timed out")

    monkeypatch.setattr(
        "latency.socket.create_connection",
        mock_connection
    )

    result = measure_tcp_latency("google.com", 443, tests=2)

    assert result["Successful Tests"] == 0
    assert result["Failed Tests"] == 2
    assert result["Status"] == "All Connections Failed"


def test_dns_resolution_failure(monkeypatch):

    def mock_dns(host):
        raise socket.gaierror("DNS lookup failed")

    monkeypatch.setattr(
        "latency.socket.gethostbyname",
        mock_dns
    )

    result = measure_tcp_latency("invalid.example", 443, tests=2)

    assert result["Status"] == "DNS Resolution Failed"
    assert result["Error"] == "DNS lookup failed"