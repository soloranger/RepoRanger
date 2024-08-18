import pytest

from api.view.v1 import api_bp

API_URL_PRIFIX = api_bp.url_prefix
API_REQUEST_HEADERS = {"Content-Type": "application/json"}


def test_get_repositories_apiv1(client):
    response = client.get(
        f"{API_URL_PRIFIX}/repositories",
        headers=API_REQUEST_HEADERS,
    )
    result = response.get_json()
    assert response.status_code == 200
    assert result["status"]["code"] == 100
    assert result["status"]["message"] == "OK."
