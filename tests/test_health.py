"""Smoke tests for StreamForge HTTP control plane."""

from fastapi.testclient import TestClient

from streamforge.main import app

client = TestClient(app)


def test_status_returns_200_and_running() -> None:
    response = client.get("/status")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "RUNNING"


def test_metrics_returns_200_and_expected_keys() -> None:
    response = client.get("/metrics")
    assert response.status_code == 200
    data = response.json()
    assert "active_streams" in data
    assert "streams" in data
    assert isinstance(data["active_streams"], int)
    assert isinstance(data["streams"], dict)