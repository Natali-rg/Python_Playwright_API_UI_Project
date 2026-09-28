import pytest
import allure

from assertpy import assert_that


@pytest.mark.negative
@allure.feature("Users API")
@allure.story("Get user")
@allure.title("Get nonexistent user")
def test_get_nonexistent_user(gorest_user):

    nonexistent_user_id = 999999999

    with allure.step("Get nonexistent user"):
        gorest_user.user_get(
            user_id=nonexistent_user_id,
            exp_status_code=404
        )


@pytest.mark.negative
@allure.feature("Users API")
@allure.story("Create user")
@allure.title("Create user with invalid email")
def test_create_user_invalid_email(gorest_user):

    user_data = {
        "name": "Invalid Email User",
        "email": "invalid-email",
        "gender": "male",
        "status": "active"
    }

    with allure.step("Create user with invalid email"):
        gorest_user.user_post(
            dict_validate=user_data,
            exp_status_code=422
        )


@pytest.mark.negative
@allure.feature("Users API")
@allure.story("Create user")
@allure.title("Create user without name")
def test_create_user_without_name(gorest_user):

    user_data = {
        "email": "noname@example.com",
        "gender": "male",
        "status": "active"
    }

    with allure.step("Create user without name"):
        gorest_user.user_post(
            dict_validate=user_data,
            exp_status_code=422
        )


@pytest.mark.negative
@allure.feature("Users API")
@allure.story("Update user")
@allure.title("Patch nonexistent user")
def test_patch_nonexistent_user(gorest_user):

    nonexistent_user_id = 999999999

    update_data = {
        "name": "Updated User"
    }

    with allure.step("Update nonexistent user using PATCH"):
        gorest_user.user_patch(
            user_id=nonexistent_user_id,
            dict_validate=update_data,
            exp_status_code=404
        )


@pytest.mark.negative
@allure.feature("Users API")
@allure.story("Update user")
@allure.title("Put nonexistent user")
def test_put_nonexistent_user(gorest_user):

    nonexistent_user_id = 999999999

    update_data = {
        "name": "Updated User",
        "email": "updated@example.com",
        "gender": "male",
        "status": "active"
    }

    with allure.step("Update nonexistent user using PUT"):
        gorest_user.user_put(
            user_id=nonexistent_user_id,
            dict_validate=update_data,
            exp_status_code=404
        )


@pytest.mark.negative
@allure.feature("Users API")
@allure.story("Delete user")
@allure.title("Delete nonexistent user")
def test_delete_nonexistent_user(gorest_user):

    nonexistent_user_id = 999999999

    with allure.step("Delete nonexistent user"):
        gorest_user.user_delete(
            user_id=nonexistent_user_id,
            exp_status_code=404
        )


@pytest.mark.negative
@allure.feature("Users API")
@allure.story("Create user")
@allure.title("Create user with invalid gender")
def test_create_user_invalid_gender(gorest_user):

    user_data = {
        "name": "Invalid Gender User",
        "email": "invalidgender@example.com",
        "gender": "unknown",
        "status": "active"
    }

    with allure.step("Create user with invalid gender"):
        gorest_user.user_post(
            dict_validate=user_data,
            exp_status_code=422
        )


@pytest.mark.negative
@allure.feature("Users API")
@allure.story("Create user")
@allure.title("Create user with invalid status")
def test_create_user_invalid_status(gorest_user):

    user_data = {
        "name": "Invalid Status User",
        "email": "invalidstatus@example.com",
        "gender": "male",
        "status": "unknown"
    }

    with allure.step("Create user with invalid status"):
        gorest_user.user_post(
            dict_validate=user_data,
            exp_status_code=422
        )


@pytest.mark.negative
@allure.feature("Users API")
@allure.story("Create user")
@allure.title("Create user without email")
def test_create_user_without_email(gorest_user):

    user_data = {
        "name": "No Email User",
        "gender": "male",
        "status": "active"
    }

    with allure.step("Create user without email"):
        gorest_user.user_post(
            dict_validate=user_data,
            exp_status_code=422
        )


@pytest.mark.negative
@allure.feature("Users API")
@allure.story("Create user")
@allure.title("Create user without status")
def test_create_user_without_status(gorest_user):

    user_data = {
        "name": "No Status User",
        "email": "nostatus@example.com",
        "gender": "male"
    }

    with allure.step("Create user without status"):
        gorest_user.user_post(
            dict_validate=user_data,
            exp_status_code=422
        )


@pytest.mark.negative
@pytest.mark.parametrize(
    "special_character",
    ["~", '"', "@", "#", "$", "%", "^", "&", "*"]
)
@allure.feature("Users API")
@allure.story("Create user")
@allure.title("Create user with special character in name")
def test_create_user_special_character_in_name(
        gorest_user,
        special_character
):

    user_data = {
        "name": special_character,
        "email": f"special{special_character}@example.com",
        "gender": "male",
        "status": "active"
    }

    with allure.step(
        f"Create user with special character: {special_character}"
    ):
        gorest_user.user_post(
            dict_validate=user_data,
            exp_status_code=422
        )


