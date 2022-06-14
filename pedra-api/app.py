from flask import jsonify,request
from lastmile_class import last_mile, app, db
from schema import LastmileSchema
from feed import feed_db

@app.route('/atendimentos', methods=['GET'])
def get_all_atendimentos():
    atendimentos=last_mile.get_all()
    serializer=LastmileSchema(many=True)
    data=serializer.dump(atendimentos)
    return jsonify(
        data
    )

@app.route('/atendimentos', methods=['POST'])
def create_atendimentos():
    data=request.get_json()
    new_atendimento=last_mile(
        id_atendimento=data.get('id_atendimento'),
        id_cliente=data.get('id_cliente'),
        angel=data.get('angel').upper(),
        polo_cidade=data.get('polo_cidade').upper(),
        polo_uf=data.get('polo_uf').upper(),
        data_limite=data.get('data_limite'),
        data_atendimento=data.get('data_atendimento')
    )
    new_atendimento.save()
    serializer=LastmileSchema()
    data=serializer.dump(new_atendimento)
    return jsonify(
        data
    ),201

@app.route('/atendimentos/<int:id_atendimento>', methods=['PUT'])
def update_atendimentos(id_atendimento):
    atendimento_to_update=last_mile.get_by_id_atendimento(id_atendimento)
    data=request.get_json()
    atendimento_to_update.id_atendimento=data.get('id_atendimento')
    atendimento_to_update.id_cliente=data.get('id_cliente')
    atendimento_to_update.angel=data.get('angel').upper()
    atendimento_to_update.polo_cidade=data.get('polo_cidade').upper()
    atendimento_to_update.polo_uf=data.get('polo_uf').upper()
    atendimento_to_update.data_limite=data.get('data_limite')
    atendimento_to_update.data_atendimento=data.get('data_atendimento')
    db.session.commit()
    serializer=LastmileSchema()
    atendimento_data=serializer.dump(atendimento_to_update)
    return jsonify(
        atendimento_data
    ),200


@app.route('/atendimentos/<int:id>', methods=['DELETE'])
def delete_atendimentos(id):
    atendimento_to_delete=last_mile.get_by_id_atendimento(id)
    atendimento_to_delete.delete()
    return jsonify(
        {"message":"Deleted"}
    ),204

@app.route('/atendimentos/<int:id_atendimento>', methods=['GET'])
def get_atendimentos_id(id_atendimento):
    atendimento=last_mile.get_by_id_atendimento(id_atendimento)
    serializer=LastmileSchema()
    data=serializer.dump(atendimento)
    return jsonify(
        data
    ),200

@app.route('/atendimentos/cliente/<int:id_cliente>', methods=['GET'])
def get_atendimentos_id_cliente(id_cliente):
    atendimento=last_mile.get_by_id_cliente(id_cliente)
    serializer=LastmileSchema(many=True)
    data=serializer.dump(atendimento)
    return jsonify(
        data
    ),200

@app.route('/atendimentos/angel/<string:name>', methods=['GET'])
def get_atendimento_angel(name):
    atendimento=last_mile.get_by_angel(name)
    serializer=LastmileSchema(many=True)
    data=serializer.dump(atendimento)
    return jsonify(
        data
    ),200

@app.route('/atendimentos/uf/<string:uf>', methods=['GET'])
def get_atendimento_uf(uf):
    atendimento=last_mile.get_by_uf(uf)
    serializer=LastmileSchema(many=True)
    data=serializer.dump(atendimento)
    return jsonify(
        data
    ),200


if __name__=='__main__':
    app.run(debug=True)

db.create_all()
feed_db()