from flask import request
from app.resources.base import BaseResource
from app.helpers.validators import PayloadSchema
from app.helpers.dependency import HandlerClient


class SubmitJobApi(BaseResource):
    """
    Submit new JOB Api
    """
    validator_class = PayloadSchema
    handler_class = HandlerClient.job_handler

    def post(self):
        result = self.validate_request()
        job = self.handler_class()
        job_id = job.create_job(result)
        return self.response201({"job_id": job_id})


class JobInfoApi(BaseResource):
    """
    Job status Api
    """
    validator_class = None
    handler_class = HandlerClient.job_handler

    def get(self):
        job_id = request.args.get("jobid", "")
        job = self.handler_class()
        data = job.get_status(job_id)
        if data is None:
            return self.response400({})
        return self.response200(data)


class VisitInfoApi(BaseResource):
    """
    Store info and visits Api
    """
    validator_class = None
    handler_class = HandlerClient.store_handler

    def get(self):
        store_id = request.args.get("storeid")
        handler = self.handler_class()
        data = handler.get_store_info(store_id)
        if data is None:
            return self.response400({})
        return self.response200(data)
