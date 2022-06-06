from src.app.app import app
from bs4 import BeautifulSoup
import json

test_data = {
        "characters": [
            { "name": "Harry Potter"},
            { "name": "Severus Snape"}
        ]
    }

def test_get_characters():
    client = app.test_client()
    app.data = { "characters": [] }

    # With no data
    response = app.test_client().get('/characters')
    soup = BeautifulSoup(response.data, 'html.parser')
    assert app.data == { "characters": [] }
    assert soup.title.string == "Harry Potter Characters"
    assert len(soup.find_all('tr')) == 1
    assert soup.find_all('tr')[0].find('th').string == "Name"

    # Add data
    app.data = test_data
    response = client.get('/characters')
    soup = BeautifulSoup(response.data, 'html.parser')
    assert soup.title.string == "Harry Potter Characters"
    assert len(soup.find_all('tr')) == 3
    assert soup.find_all('tr')[0].find('th').string == "Name"
    assert soup.find_all('tr')[1].find('td').string.strip() == "Harry Potter"
    assert soup.find_all('tr')[2].find('td').string.strip() == "Severus Snape"

def test_post_characters():
    client = app.test_client()
    app.data = { "characters": [] }
    client.post("/characters", json=test_data)
    assert app.data == test_data
