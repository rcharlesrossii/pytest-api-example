from jsonschema import validate
import pytest
import schemas
import api_helpers


@pytest.fixture
def order():
    test_endpoint = "/store/order"
    test_data = {
        "pet_id": 0
    }

    response = api_helpers.post_api_data(test_endpoint, test_data)

    assert response.status_code == 201

    order_data = response.json()

    # Validate the order response schema
    validate(instance=order_data, schema=schemas.order)

    yield order_data

    # Reset the pet status after the test is complete
    api_helpers.patch_api_data(
        f"/store/order/{order_data['id']}",
        {"status": "available"}
    )


def test_patch_order_by_id(order):
    order_id = order["id"]

    test_endpoint = f"/store/order/{order_id}"
    test_data = {
        "status": "sold"
    }

    response = api_helpers.patch_api_data(test_endpoint, test_data)

    # Validate the appropriate response code
    assert response.status_code == 200

    # Validate the response message
    assert response.json()["message"] == "Order and pet status updated successfully"

    # Validate the pet status was updated
    pet_response = api_helpers.get_api_data(f"/pets/{order['pet_id']}")

    assert pet_response.status_code == 200
    assert pet_response.json()["status"] == "sold"
