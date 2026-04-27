import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Teste 1: Verifica se a página inicial carrega com sucesso (Status 200)
def test_home_status_code(client):
    response = client.get('/')
    assert response.status_code == 200

# Teste 2: Verifica se o texto esperado aparece na tela
def test_home_data(client):
    response = client.get('/')
    assert b"Atividade de DevOps" in response.data

# Teste 3: Verifica se uma página que não existe retorna erro 404
def test_not_found(client):
    response = client.get('/pagina-falsa')
    assert response.status_code == 404

# Teste 4: Verifica se o método POST é bloqueado na rota principal (Status 405)
def test_method_not_allowed(client):
    response = client.post('/')
    assert response.status_code == 405

# Teste 5: Verifica se o app Flask foi instanciado corretamente
def test_app_is_flask_instance():
    assert str(type(app)) == "<class 'flask.app.Flask'>"