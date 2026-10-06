from flask import Flask, jsonify, request

app = Flask(__name__)

datos = [{'id': 1, 'paciente_id': 1, 'concepto': 'Consulta', 'valor': 80000, 'estado': 'PENDIENTE'}, {'id': 2, 'paciente_id': 2, 'concepto': 'Laboratorio', 'valor': 120000, 'estado': 'PAGADA'}, {'id': 3, 'paciente_id': 3, 'concepto': 'Consulta especializada', 'valor': 150000, 'estado': 'PENDIENTE'}]

@app.get("/")
def inicio():
    return jsonify({
        "servicio": "Facturacion",
        "estado": "activo",
        "recurso": "/facturas"
    })

@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.get("/facturas")
def listar():
    return jsonify(datos), 200

@app.get("/facturas/<int:item_id>")
def obtener(item_id):
    item = next((x for x in datos if x["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Registro no encontrado"}), 404
    return jsonify(item), 200

@app.post("/facturas")
def crear():
    nuevo = request.get_json(silent=True)
    if not isinstance(nuevo, dict):
        return jsonify({"error": "Se requiere un cuerpo JSON válido"}), 400

    nuevo["id"] = max([x["id"] for x in datos], default=0) + 1
    datos.append(nuevo)
    return jsonify(nuevo), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
