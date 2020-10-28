import unittest

from app.helpers.dependency import HandlerClient


class JobHandlerTest(unittest.TestCase):

    def setUp(self):
        self.handler = HandlerClient.job_handler()

    def test_create_job(self):
        result = self.handler.create_job({})
        self.assertTrue(str, type(result))

    def test_get_status_with_invalid_task_id(self):
        result = self.handler.get_status("123")
        self.assertEqual(result, None)


class StoreHandlerTest(unittest.TestCase):

    def setUp(self):
        self.handler = HandlerClient.store_handler()

    def _test_get_store_info(self):
        result = self.handler.get_store_info("123")
        self.assertEqual(None, result)
