from app import api
from app.resources.resource import (SubmitJobApi, JobInfoApi, VisitInfoApi)

# Api resource routing
api.add_resource(SubmitJobApi, '/api/submit')
api.add_resource(JobInfoApi, '/api/status')
api.add_resource(VisitInfoApi, '/api/visits')
