from unittest.mock import MagicMock
from port_checker import check_tcp_port


def test_open_port(monkeypatch):

    mock_socket = MagicMock()
    mock_socket.connect_ex.return_value = 0

    monkeypatch.setattr(
        "port_checker.socket.socket",
        lambda *args, **kwargs: mock_socket
    )

    result = check_tcp_port("google.com", 443)

    assert result["Status"] == "Open"
    assert result["Error Code"] == 0

    mock_socket.close.assert_called_once()


def test_failed_port(monkeypatch):
    mock_socket = MagicMock()
    mock_socket.connect_ex.return_value = 10061

    monkeypatch.setattr(
        "port_checker.socket.socket",
        lambda *args, **kwargs: mock_socket
    )

    result = check_tcp_port("google.com", 22)

    assert result["Status"] == "Not Reachable"
    assert result["Error Code"] == 10061


    mock_socket.close.assert_called_once()