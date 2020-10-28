import unittest
import json

from app import app

http_headers = {"Content-Type": "application/json"}


class ResourceTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.payload = json.dumps({
            "count": 1,
            "visits": [
                {
                    "store_id": "S00339221",
                    "image_url": [
                        "https://www.gstatic.com/webp/gallery/2.jpg",
                        "https://www.gstatic.com/webp/gallery/3.jpg"
                    ],
                    "visit_time": "2020-10-24 19:16:40.916885"
                }
            ]
        })

    def test_submit_job_201(self):
        response = self.app.post('/api/submit', headers=http_headers, data=self.payload)
        self.assertTrue("job_id" in response.json)
        self.assertEqual(201, response.status_code)

    def test_submit_job_400(self):
        self.payload = {"count": 5, "visits": []}
        response = self.app.post('/api/submit', headers=http_headers, data=self.payload)
        self.assertTrue("message" in response.json)
        self.assertEqual(400, response.status_code)

    def test_job_info_200(self):
        resp = self.app.post('/api/submit', headers=http_headers, data=self.payload)
        job_id = resp.json["job_id"]
        response = self.app.get('/api/status?jobid={}'.format(job_id), headers=http_headers)
        self.assertTrue("status" in response.json)
        self.assertEqual(200, response.status_code)

    def test_job_info_400(self):
        job_id = "ok"
        response = self.app.get('/api/status?jobid={}'.format(job_id), headers=http_headers)
        self.assertEqual({}, response.json)
        self.assertEqual(400, response.status_code)

    def test_visit_info_200(self):
        store_id = "S00339221"
        response = self.app.get('/api/visits?storeid={}'.format(store_id), headers=http_headers)
        self.assertTrue("visits" in response.json)
        self.assertEqual(200, response.status_code)

    def test_visit_info_400(self):
        store_id = ""
        response = self.app.get('/api/visits?storeid={}'.format(store_id), headers=http_headers)
        self.assertEqual({}, response.json)
        self.assertEqual(400, response.status_code)

    def tearDown(self):
        pass
