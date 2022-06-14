from marshmallow import Schema, fields

class LastmileSchema(Schema):
    id_atendimento=fields.Integer()
    id_cliente=fields.Integer()
    angel=fields.String()
    polo_cidade=fields.String()
    polo_uf=fields.String()
    data_limite=fields.Date()
    data_atendimento=fields.DateTime()