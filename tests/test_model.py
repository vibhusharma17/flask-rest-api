import unittest

from app import db, create_app
from app.models.store import Store
from manage import load_data


class ModelManagerTest(unittest.TestCase):

    def setUp(self):
        """
        Creates a new database for the unit test to use
        """
        app = create_app(test_connection=True)
        app.app_context().push()
        db.create_all(app=app)
        load_data(test=True)

    def tearDown(self):
        """
        Ensures that the database is emptied for next unit test
        """
        db.drop_all()

    def test_find_all(self):
        rows = Store.find_all()
        self.assertTrue(list, type(rows))
        self.assertEqual(5, len(rows))

    def test_find_all_returns_empty(self):
        rows = Store.find_all(store_id="")
        self.assertTrue(list, type(rows))
        self.assertEqual(0, len(rows))

    def test_find_one(self):
        store_id = "S00339198"
        row = Store.find_one(store_id=store_id)
        self.assertTrue(isinstance(row, Store))
        self.assertEqual(store_id, row.store_id)

    def test_find_one_returns_none(self):
        store_id = "XYZ"
        row = Store.find_one(store_id=store_id)
        self.assertEqual(None, row)

    def test_add_record(self):
        data = {"store_id": "XYZ123", "store_name": "XYZ", "area_code": "123"}
        Store.add_record(**data)
        row = Store.find_one(store_id="XYZ123")
        self.assertNotEqual(None, row)

    def test_to_dict(self):
        row = Store.find_all()[0]
        data = row.to_dict()
        self.assertTrue(dict, type(row))
