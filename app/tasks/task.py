import datetime

from app import celery
from app.models.store import StoreDetails
from app.services.crawler import AsyncCrawler
from app.services.image_processor import ImageProcessor
from app.services.job import JobStatus


@celery.task()
def fetch_images(data):
    job_status = JobStatus(fetch_images.request.id)
    job_status.mark_ongoing()

    errors = []
    for d in data["visits"]:
        store_id, urls = d["store_id"], d["image_url"]
        crawler = AsyncCrawler(urls)
        try:
            filenames = crawler.run()
            processor = ImageProcessor(filenames)
            perimeters = processor.run()
        except Exception as err:
            error = {"store_id": store_id, "error": str(err)}
            errors.append(error)
        else:
            for i in range(len(urls)):
                record = {"store_id": store_id, "image_url": urls[i], "perimeter": perimeters[i],
                          "date": datetime.datetime.now()}
                StoreDetails.add_record(**record)

    if errors:
        job_status.mark_failed(errors)
    else:
        job_status.mark_completed()
    return True
