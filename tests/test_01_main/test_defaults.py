import os
import time

import docker
import requests
from docker.client import DockerClient

from ..utils import (
    CONTAINER_NAME,
    get_config,
    get_logs,
    get_response_text1,
    remove_previous_container,
)

client = docker.from_env()


def verify_container(container: DockerClient, response_text: str) -> None:
    response = requests.get("http://127.0.0.1:8000")
    data = response.json()
    assert data["message"] == response_text
    config_data = get_config(container)
    assert config_data["workers_per_core"] == 1
    assert config_data["use_max_workers"] is None
    assert config_data["host"] == "0.0.0.0"
    assert config_data["port"] == "80"
    assert config_data["loglevel"] == "info"
    assert config_data["workers"] >= 2
    assert config_data["bind"] == "0.0.0.0:80"
    assert config_data["graceful_timeout"] == 120
    assert config_data["timeout"] == 120
    assert config_data["keepalive"] == 5
    assert config_data["errorlog"] == "-"
    assert config_data["accesslog"] == "-"
    logs = get_logs(container)
    assert "Checking for script in /app/prestart.sh" in logs
    assert "Running script /app/prestart.sh" in logs
    assert (
        "Running inside /app/prestart.sh, you could add migrations to this file" in logs
    )
    assert '"GET / HTTP/1.1" 200' in logs
    assert "[INFO] Application startup complete." in logs
    assert "Using worker: uvicorn.workers.UvicornWorker" in logs


def test_defaults() -> None:
    name = os.getenv("NAME")
    image = f"tiangolo/uvicorn-gunicorn-fastapi:{name}"
    response_text = get_response_text1()
    sleep_time = int(os.getenv("SLEEP_TIME", 1))
    remove_previous_container(client)
    container = client.containers.run(
        image, name=CONTAINER_NAME, ports={"80": "8000"}, detach=True
    )
    time.sleep(sleep_time)
    verify_container(container, response_text)
    container.stop()
    # Test that everything works after restarting too
    container.start()
    time.sleep(sleep_time)
    verify_container(container, response_text)
    container.stop()
    container.remove()
