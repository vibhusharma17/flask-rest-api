from dependency_injector import containers
from dependency_injector import providers

from app.models.store import Store, StoreDetails
from app.tasks.task import fetch_images
from app.services.handler import JobHandler, StoreHandler
from app.services.job import BackgroundJob


class TaskClient(containers.DeclarativeContainer):
    task = providers.Factory(
        BackgroundJob,
        task_func=fetch_images,
    )


class HandlerClient(containers.DeclarativeContainer):
    job_handler = providers.Factory(
        JobHandler,
        TaskClient.task

    )

    store_handler = providers.Factory(
        StoreHandler,
        Store, StoreDetails
    )
