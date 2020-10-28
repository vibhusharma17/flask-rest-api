import json
import celery
from app import redis_db
from app.helpers.exception import InvalidDataType


class JobStatus:
    ONGOING = "Ongoing"
    COMPLETED = "completed"
    FAILED = "failed"

    def __init__(self, job_id):
        self.job_id = job_id
        self.status = self.ONGOING
        self.errors = []

    def _save(self):
        message = {"job_id": self.job_id, "status": self.status}
        if self.errors:
            message["error"] = self.errors
        redis_db.set(self.job_id, json.dumps(message))

    def mark_ongoing(self):
        self.status = self.ONGOING
        self._save()

    def mark_completed(self):
        self.status = self.COMPLETED
        self._save()

    def mark_failed(self, errors):
        self.errors = errors
        self.status = self.FAILED
        self._save()


class BackgroundJob:

    def __init__(self, task_func):
        if not isinstance(task_func, celery.local.PromiseProxy):
            raise InvalidDataType("Unsupported function passed.")
        self.task_runner = task_func

    def run(self, data):
        result = self.task_runner.delay(data)
        return result.task_id

    def status(self, task_id):
        status = redis_db.get(task_id)
        if not status:
            return None
        return json.loads(status)
