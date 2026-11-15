import subprocess

from diagnostics import check_host_availability

def test_successful_ping(monkeypatch):

    def mock_run(*args, **kwargs):

        return subprocess.CompletedProcess(
            args=args,
            returncode=0,
            stdout="Packets: Sent=4, Received=4, Lost=0 (0% loss)",
            stderr=""
        )

    monkeypatch.setattr(
        "diagnostics.subprocess.run",
        mock_run
    )

    result = check_host_availability("google.com")

    assert result["Packets Sent"] == 4
    assert result["Packets Received"] == 4
    assert result["Packets Lost"] == 0
    assert result["Status"] == "Responding"


def test_failed_ping(monkeypatch):

    def mock_run(*args, **kwargs):

        return subprocess.CompletedProcess(
            args=args,
            returncode=1,
            stdout="Packets: Sent=4, Received=0, Lost=4 (100% loss)",
            stderr=""
        )
    monkeypatch.setattr(
        "diagnostics.subprocess.run",
        mock_run
    )

    result = check_host_availability("google.com")

    assert result["Packets Received"] == 0
    assert result["Packets Lost"] == 4
    assert result["Packet Loss"] == "100.00%"
    assert result["Status"] == "No ICMP Response"



def test_ping_timeout(monkeypatch):

    def mock_run(*args, **kwargs):

        raise subprocess.TimeoutExpired(
            cmd="ping",
            timeout=10
        )

    monkeypatch.setattr(
        "diagnostics.subprocess.run",
        mock_run
    )

    result = check_host_availability("google.com")

    assert result["Status"] == "Timed Out"
    assert "Error" in result