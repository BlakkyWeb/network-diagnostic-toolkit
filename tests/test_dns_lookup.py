from dns_lookup import resolve_domain

def test_successful_dns_lookup(monkeypatch):

    def mock_gethostbyname(domain):
        return "142.250.129.100"

    monkeypatch.setattr(
        "dns_lookup.socket.gethostbyname",
        mock_gethostbyname
    )

    result = resolve_domain("google.com")

    assert result["Domain"] == "google.com"
    assert result["IP Address"] == "142.250.129.100"
    assert result["Status"] == "Success"

def test_failed_dns_lookup(monkeypatch):
    import socket

    def mock_gethostbyname(domain):
        raise socket.gaierror("DNS lookup failed")

    monkeypatch.setattr(
        "dns_lookup.socket.gethostbyname",
        mock_gethostbyname
    )

    result = resolve_domain("invalid.example")

    assert result["IP Address"] is None
    assert result["Status"] == "Failed"
    assert "Error" in result