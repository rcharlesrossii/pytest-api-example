# Assessment Notes

## Pet Tests

### Pet Schema Validation
- Investigated the failing pet schema test.
- Identified that the `name` property in `schemas.py` was incorrectly defined as an `integer` type.
- Updated the `name` property to a `string` type, matching the API response.
- Confirmed the API response successfully validates against the corrected schema.

### Find Pets by Status
- Extended the parameterized test to include all supported statuses: `available`, `sold`, and `pending`.
- Validated the HTTP 200 response.
- Validated that each returned pet has the requested status.
- Validated each returned pet against the pet JSON schema.

### Get Pet by ID - 404
- Parameterized the test with multiple nonexistent `pet_id`s to validate multiple invalid `pet_id` cases.
- Validated the HTTP 404 response.
- Validated that the response contains the expected error message for each requested `pet_id`.

## Store Tests

### Update Order
- Added a pytest fixture to create a valid order before testing the PATCH endpoint.
- Used the generated order ID to test `PATCH /store/order/{order_id}`.
- Validated the HTTP 200 response.
- Validated the expected success message.
- Verified that updating the order also updates the associated pet status.
- Added fixture cleanup to restore the pet to an available state after running the test.

### Order Schema Validation
- Added an `order` JSON schema to `schemas.py`.
- Validated newly created orders against the newly added `order` schema.

## Bugs Found

### Incorrect Pet Name Schema Type
- **File:** `schemas.py`
- **Issue:** The pet `name` property was defined as an `integer` type, but the API returns the pet names as a `string` type.
- **Resolution:** Changed the `name` property type to `string`, instead of being an `integer`.

## Test Results

The completed test suite included 8 tests covering:
- Pet schema validation
- Pet status filtering
- Pet 404 responses
- Store order creation and updates

After addressing the issues in the code repository, I successfully obtained `8 passed` pytest tests.
