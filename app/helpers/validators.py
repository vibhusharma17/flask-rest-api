from marshmallow import Schema, fields, post_load, ValidationError


class StoreSchema(Schema):
    store_id = fields.Str()
    image_url = fields.List(fields.Url(), required=True)
    visit_time = fields.DateTime()


class PayloadSchema(Schema):
    count = fields.Int()
    visits = fields.List(fields.Nested(lambda: StoreSchema()))

    @post_load
    def unwrap_envelope(self, data, **kwargs):
        if data["count"] != len(data["visits"]):
            raise ValidationError('Count should be equal to length of visits.')
        return data
