from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_predict_non_spam():
    response = client.post("/predict/",
                           json={"text": "Hey so this sat are we going for the intro pilates only? Or the kickboxing too?"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'LABEL_0'


def test_predict_spam():
    response = client.post("/predict/",
                           json={"text": "U have a secret admirer. REVEAL who thinks U R So special. Call 09065174042. To opt out Reply REVEAL STOP. 1.50 per msg recd."})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'LABEL_1'
