from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock

# Mock redis before importing app
import sys
sys.modules['redis'] = MagicMock()

from main import app  # noqa: E402

client = TestClient(app)


def test_health_returns_200():
    """Health endpoint must return 200"""
    response = client.get("/health")
    assert response.status_code == 200


def test_health_returns_ok():
    """Health endpoint must return status ok"""
    response = client.get("/health")
    assert response.json() == {"status": "ok"}


def test_create_job_returns_job_id():
    """Create job must return a job_id"""
    with patch("main.r") as mock_redis:
        mock_redis.lpush.return_value = 1
        mock_redis.hset.return_value = 1
        response = client.post("/jobs")
        assert response.status_code == 200
        assert "job_id" in response.json()


def test_create_job_pushes_to_queue():
    """Create job must push to redis jobs queue"""
    with patch("main.r") as mock_redis:
        mock_redis.lpush.return_value = 1
        mock_redis.hset.return_value = 1
        client.post("/jobs")
        mock_redis.lpush.assert_called_once()
        args = mock_redis.lpush.call_args[0]
        assert args[0] == "jobs"


def test_get_job_returns_status():
    """Get job must return status when job exists"""
    with patch("main.r") as mock_redis:
        mock_redis.hget.return_value = "queued"
        response = client.get("/jobs/test-123")
        assert response.status_code == 200
        assert response.json()["status"] == "queued"


def test_get_job_returns_404_when_not_found():
    """Get job must return 404 when job does not exist"""
    with patch("main.r") as mock_redis:
        mock_redis.hget.return_value = None
        response = client.get("/jobs/nonexistent")
        assert response.status_code == 404


def test_get_job_returns_correct_job_id():
    """Get job must return the correct job_id in response"""
    with patch("main.r") as mock_redis:
        mock_redis.hget.return_value = "completed"
        response = client.get("/jobs/test-abc")
        assert response.json()["job_id"] == "test-abc"

