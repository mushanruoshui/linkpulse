from fastapi.testclient import TestClient

from app.main import app

# TestClient 把请求直接送进 app，不经过网络
client = TestClient(app)


def test_healthz_returns_200():
    """健康检查接口应该返回 200。"""
    response = client.get("/healthz")
    assert response.status_code == 200


def test_healthz_body():
    """健康检查接口的响应体应该包含 status=ok。"""
    response = client.get("/healthz")
    body = response.json()
    assert body["status"] == "ok"
    assert "version" in body