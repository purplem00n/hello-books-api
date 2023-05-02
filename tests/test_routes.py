def test_get_all_books_with_no_records(client):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_book(client):
    response = client("/books/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": "",
        "title": "",
        "description": ""
    }

def test_get_book_by_id(client, two_saved_books): # where is twosavedbooks getting called?
    response = client.get("/books/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body = {
        "id": 1,
        "book": "Ocean Book",
        "description": "watr 4evr"
        }

