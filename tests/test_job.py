import unittest

from app.helpers.dependency import TaskClient
from app.helpers.exception import InvalidDataType
from app.services.job import BackgroundJob


class BackgroundJobTest(unittest.TestCase):

    def setUp(self):
        self.task = TaskClient.task()

    def test_raise_error(self):
        def test_func():
            pass

        self.assertRaises(InvalidDataType, BackgroundJob, test_func)

    def test_run(self):
        result = self.task.run({})
        self.assertTrue(str, type(result))

    def test_status(self):
        result = self.task.status("abc")
        self.assertEqual(None, result)
