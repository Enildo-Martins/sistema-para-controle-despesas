import json

DATA_FILE = 'data.json'

def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"categorias": [], "despesas": []}

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def add_categoria(nome):
    data = load_data()
    categoria = {"id": len(data["categorias"]) + 1, "nome": nome}
    data["categorias"].append(categoria)
    save_data(data)
    return categoria

def add_despesa(valor, data_despesa, categoria_id, descricao, status):
    data = load_data()
    despesa = {
        "id": len(data["despesas"]) + 1,
        "valor": valor,
        "data": data_despesa,
        "categoria_id": categoria_id,
        "descricao": descricao,
        "status": status
    }
    data["despesas"].append(despesa)
    save_data(data)
    return despesa

def get_categorias():
    return load_data()["categorias"]

def get_despesas():
    return load_data()["despesas"]