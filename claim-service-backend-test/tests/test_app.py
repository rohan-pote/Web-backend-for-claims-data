def test_ping_end_point(client):
    assert client.get("/ping").status_code == 200

