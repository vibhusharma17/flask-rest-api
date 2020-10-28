class JobHandler:
    """
    Handler class to create background job and return status of job.
    """

    def __init__(self, task):
        self.task = task

    def create_job(self, data):
        return self.task.run(data)

    def get_status(self, task_id):
        return self.task.status(task_id)


class StoreHandler:
    """
    Handler to Retrieve store related data.
    """

    def __init__(self, store_model, store_details_model):
        self.store_model = store_model
        self.store_details_model = store_details_model

    def get_store_info(self, store_id):
        store_obj = self.store_model.find_one(store_id=store_id)
        if not store_obj:
            return None
        rows = self.store_details_model.find_all(store_id=store_id)
        rows_dict = self.store_details_model.rows_to_dict(rows, excludes=["id", "store_id", "image_url"])
        data = store_obj.to_dict(excludes=["id"])
        data["visits"] = rows_dict
        return data
