from app import db


class ModelManager:
    """
    Model manager class to add db functionality. All models must extend this class.
    """

    def to_dict(self, excludes=[]):
        d = {}
        for column in self.__table__.columns:
            if column.name in excludes:
                continue
            d[column.name] = str(getattr(self, column.name))
        return d

    @classmethod
    def add_record(cls, **kwargs):
        """
        :param kwargs:
        :return: <StoreDetails>|Exception
        """
        obj = cls(**kwargs)
        db.session.add(obj)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            raise
        return obj

    @classmethod
    def find_all(cls, **kwargs):
        rows = db.session.query(cls).filter_by(**kwargs).all()
        return rows

    @classmethod
    def find_one(cls, **kwargs):
        row = db.session.query(cls).filter_by(**kwargs).first()
        return row

    @staticmethod
    def rows_to_dict(rows, excludes=[]):
        records = []
        for row in rows:
            d = row.to_dict(excludes)
            records.append(d)
        return records
