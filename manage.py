import unittest
import csv
from flask_script import Manager
from app import app
from app import db
from app.models.store import Store

manager = Manager(app)


@manager.command
def test():
    """Runs the unit tests without."""
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


def load_data(test=False):
    with open("StoreMasterAssignment.csv") as f:
        datalist = [{k: str(v) for k, v in row.items()}
                    for row in csv.DictReader(f, skipinitialspace=True)]

    if test is True:
        datalist = datalist[:5]

    for d in datalist:
        d["store_id"] = d.pop("StoreID")
        d["store_name"] = d.pop("StoreName")
        d["area_code"] = d.pop("AreaCode")
        Store.add_record(**d)
    print("store created", len(datalist))


@manager.command
def initdb():
    # Create tables
    db.create_all()
    db.session.commit()
    print("DB tables created.")
    load_data()


if __name__ == '__main__':
    manager.run()
