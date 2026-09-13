from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_


def test_pet_schema():
    test_endpoint = "/pets/1"

    response = api_helpers.get_api_data(test_endpoint)

    assert response.status_code == 200

    # Validate the response schema against the defined schema in schemas.py
    validate(instance=response.json(), schema=schemas.pet)


@pytest.mark.parametrize("status", ["available", "sold", "pending"])
def test_find_by_status_200(status):
    test_endpoint = "/pets/findByStatus"
    params = {
        "status": status
    }

    response = api_helpers.get_api_data(test_endpoint, params)

    assert response.status_code == 200

    for pet in response.json():
        # Validate the 'status' property in the response is equal to the expected status
        assert pet["status"] == status
        # Validate the schema for each object in the response
        validate(instance=pet, schema=schemas.pet)


@pytest.mark.parametrize("pet_id", [10, 50, 100])
def test_get_by_id_404(pet_id):
    test_endpoint = f"/pets/{pet_id}"

    response = api_helpers.get_api_data(test_endpoint)

    # Validate the appropriate 404 response code
    assert_that(response.status_code, is_(404))

    # Validate the error message for the requested pet ID
    assert_that(
        response.json()["message"],
        contains_string(f"Pet with ID {pet_id} not found")
    )
