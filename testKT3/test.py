import pytest
from base_request import BaseRequest

url = 'https://petstore.swagger.io/v2'
base = BaseRequest(url)

def test_GETstoreOrder():
    storeOrderGET = base.get('store/order', 1)
    assert storeOrderGET is not None

def test_GETuser():
    userGET = base.get('user', 'test', True)
    assert userGET is not None

def test_GETstoreInventory():
    storeInventoryGET = base.get('store', 'inventory')
    assert storeInventoryGET is not None

def test_DELETEstoreOrder():
    delete = base.delete('store/order', 1) is not None
    assert delete is not None

def test_DELETEuserTest():
    delete = base.delete('user', 'test')
    assert delete is not None

def test_POSTuser():
    post = base.post('user', '', {
    "id": 9223372036854761595,
    "username": "test",
    "firstName": "test",
    "lastName": "test",
    "email": "test@test.tt",
    "password": "test",
    "phone": "test",
    "userStatus": 0
})
    assert post is not None

def test_POSTstoreOrder():
    post = base.post('store', 'order',
              {"id": 1, "petId": 11, "quantity": 111, "shipDate": "2024-10-28T12:23:10.818Z", "status": "placed",
                  "complete": True})
    assert post is not None

def test_POSTcreateWithArray():
    post_data = [
        {"id": 2, "username": "new_test", "firstName": "new_test", "lastName": "new_test", "email": "new_test@test.tt",
            "password": "new_test", "phone": "new_test", "userStatus": 3},
        {"id": 3, "username": "new_test2", "firstName": "new_test2", "lastName": "new_test2",
            "email": "new_test2@test.tt", "password": "new_test2", "phone": "new_test2", "userStatus": 4}]

    post = base.post('user/createWithArray', '', post_data)
    assert post is not None