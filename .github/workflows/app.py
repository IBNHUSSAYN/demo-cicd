from flask import Flask, jsonify, request
app = Flask(__name__)

#Sample in-memory data store
DATA = {"status": "ok", "items": ["demo"]}

@app.route("/")
def home():
    return jsonify({"message": "Hello Github Actions!"})

@app.route("/health")
def health():
    return jsonifyP({"status": "Healthy"}),200

@app.route("/add", methods=["POST"])
def add_item():
    payload = request.get_json() or {}
    item = payload.get("item")
    if not item:
        return jsonify({"Error": "Item is required"}), 400
        DATA["items"].append(item)
        return jsonify({"items": DATA["items"]}), 201

#UNIT TESTS (RUN VIA PYTEST)
def test_home():
    client = app.test_client()
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json["status"] == "Healthy"

def test_add_item():
    client = app.test_client()
    res = client.post("/add", json={"item": "test_item"})
    assert res.status_code == 201
    assert "test_item" in res.json["items"]
