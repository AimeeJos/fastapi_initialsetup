import os
from celery import Celery
import time

broker_url = os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0")
backend_url = os.getenv("CELERY_RESULT_BACKEND", "redis://redis:6379/0")

celery_app = Celery(
    "worker",
    broker=broker_url,
    backend=backend_url
)

@celery_app.task
def sample_task(x, y):
    time.sleep(5)  # Simulate a long-running task
    return x + y
