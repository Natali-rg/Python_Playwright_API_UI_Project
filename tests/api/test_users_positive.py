import pytest
import time
import allure

from assertpy import assert_that


@pytest.mark.positive
@allure.feature("Users API")
@allure.story("Get users")
@allure.title("Get all users")
def test_get_users(gorest_user):

    with allure.step("Get all users"):
        response = gorest_user.user_get()

    with allure.step("Verify users list is not empty"):
        assert_that(response).is_not_empty()

    with allure.step("Verify each user has an ID"):
        for user in response:
            assert_that(user["id"]).is_not_none()


@pytest.mark.positive
@allure.feature("Users API")
@allure.story("Get user")
@allure.title("Get user by ID")
def test_get_user_by_id(gorest_user):

    with allure.step("Get list of users"):
        response = gorest_user.user_get()

    with allure.step("Get user ID from the first user"):
        user_id = response[0]["id"]
        print(f"User ID: {user_id}")

    with allure.step("Get user by ID"):
        response_user_id = gorest_user.user_get(
            user_id=user_id
        )

    with allure.step("Verify user ID"):
        assert_that(response_user_id["id"]).is_equal_to(user_id)


@pytest.mark.positive
@pytest.mark.parametrize("gender", ["male", "female"])
@allure.feature("Users API")
@allure.story("Filter users")
@allure.title("Get users by gender")
def test_get_users_by_gender(gorest_user, gender):

    with allure.step(f"Get users with gender: {gender}"):
        response = gorest_user.user_get(
            param={"gender": gender}
        )

    with allure.step("Verify users list is not empty"):
        assert_that(response).is_not_empty()

    with allure.step(f"Verify all users have gender: {gender}"):
        for user in response:
            assert_that(user["gender"]).is_equal_to(gender)


@pytest.mark.positive
@allure.feature("Users API")
@allure.story("Create user")
@allure.title("Create user with valid data")
def test_create_user(gorest_user):

    user_data = {
        "name": "Tela Ramakina",
        "email": f"telaRa@{time.time()}.com",
        "gender": "male",
        "status": "active"
    }

    with allure.step("Create user"):
        response = gorest_user.user_post(user_data)
        user_id = response["id"]
        print(f"User created with ID: {user_id}")

    with allure.step("Verify created user data"):
        assert_that(response["id"]).is_not_none()
        assert_that(response["name"]).is_equal_to(user_data["name"])
        assert_that(response["email"]).is_equal_to(user_data["email"])
        assert_that(response["gender"]).is_equal_to(user_data["gender"])
        assert_that(response["status"]).is_equal_to(user_data["status"])

    with allure.step("Delete created user"):
        delete_response = gorest_user.user_delete(user_id)

        assert_that(delete_response).is_equal_to(204)


@pytest.mark.positive
@allure.feature("Users API")
@allure.story("Update user")
@allure.title("Patch user data")
def test_patch_user(gorest_user):

    user_data = {
        "name": "Tela Ramakina",
        "email": f"telaRa@{time.time()}.com",
        "gender": "male",
        "status": "active"
    }

    with allure.step("Create user"):
        response = gorest_user.user_post(user_data)
        user_id = response["id"]
        print(f"User created with ID: {user_id}")

    update_data = {
        "name": "Updated Tela"
    }

    with allure.step("Update user using PATCH"):
        response_update = gorest_user.user_patch(
            user_id=user_id,
            dict_validate=update_data
        )

    with allure.step("Verify patched user data"):
        assert_that(response_update["id"]).is_equal_to(user_id)
        assert_that(
            response_update["name"]
        ).is_equal_to(update_data["name"])
        assert_that(
            response_update["email"]
        ).is_equal_to(user_data["email"])
        assert_that(
            response_update["gender"]
        ).is_equal_to(user_data["gender"])
        assert_that(
            response_update["status"]
        ).is_equal_to(user_data["status"])

    with allure.step("Delete test user"):
        delete_response = gorest_user.user_delete(user_id)

        assert_that(delete_response).is_equal_to(204)


@pytest.mark.positive
@allure.feature("Users API")
@allure.story("Update user")
@allure.title("Put user data")
def test_put_user(gorest_user):

    user_data = {
        "name": "Tela Ramakina",
        "email": f"telaRa@{time.time()}.com",
        "gender": "male",
        "status": "active"
    }

    with allure.step("Create user"):
        response = gorest_user.user_post(user_data)
        user_id = response["id"]
        print(f"User created with ID: {user_id}")

    update_data = {
        "name": "PUT Tela",
        "email": f"putTela@{time.time()}.com",
        "gender": "female",
        "status": "inactive"
    }

    with allure.step("Update user using PUT"):
        response_update = gorest_user.user_put(
            user_id=user_id,
            dict_validate=update_data
        )

    with allure.step("Verify updated user data"):
        assert_that(response_update["id"]).is_equal_to(user_id)
        assert_that(
            response_update["name"]
        ).is_equal_to(update_data["name"])
        assert_that(
            response_update["email"]
        ).is_equal_to(update_data["email"])
        assert_that(
            response_update["gender"]
        ).is_equal_to(update_data["gender"])
        assert_that(
            response_update["status"]
        ).is_equal_to(update_data["status"])

    with allure.step("Delete test user"):
        delete_response = gorest_user.user_delete(user_id)

        assert_that(delete_response).is_equal_to(204)


@pytest.mark.positive
@allure.feature("Users API")
@allure.story("Delete user")
@allure.title("Delete existing user")
def test_delete_user(gorest_user):

    user_data = {
        "name": "Test Delete User",
        "email": f"delete{time.time()}@example.com",
        "gender": "male",
        "status": "active"
    }

    with allure.step("Create user"):
        response = gorest_user.user_post(user_data)
        user_id = response["id"]
        print(f"User ID: {user_id}")

    with allure.step("Delete user"):
        delete_response = gorest_user.user_delete(user_id)

    with allure.step("Verify delete response status"):
        assert_that(delete_response).is_equal_to(204)

    with allure.step("Verify user was deleted"):
        gorest_user.user_get(
            user_id=user_id,
            exp_status_code=404
        )


@pytest.mark.positive
@allure.feature("Users API")
@allure.story("Full CRUD lifecycle")
@allure.title("Complete user CRUD lifecycle")
def test_full_user_crud_lifecycle(gorest_user):

    # 1. CREATE

    user_data = {
        "name": "CRUD Test User",
        "email": f"crud{time.time()}@example.com",
        "gender": "male",
        "status": "active"
    }

    with allure.step("Create user"):
        response_create = gorest_user.user_post(user_data)

        user_id = response_create["id"]
        print(f"User created with ID: {user_id}")

        time.sleep(6)

    with allure.step("Verify created user"):
        assert_that(user_id).is_not_none()
        assert_that(
            response_create["name"]
        ).is_equal_to(user_data["name"])
        assert_that(
            response_create["email"]
        ).is_equal_to(user_data["email"])
        assert_that(
            response_create["gender"]
        ).is_equal_to(user_data["gender"])
        assert_that(
            response_create["status"]
        ).is_equal_to(user_data["status"])

    # 2. READ

    with allure.step("Get user by ID"):
        response_get = gorest_user.user_get(
            user_id=user_id
        )

    with allure.step("Verify user data after GET"):
        assert_that(response_get["id"]).is_equal_to(user_id)
        assert_that(
            response_get["name"]
        ).is_equal_to(user_data["name"])
        assert_that(
            response_get["email"]
        ).is_equal_to(user_data["email"])
        assert_that(
            response_get["gender"]
        ).is_equal_to(user_data["gender"])
        assert_that(
            response_get["status"]
        ).is_equal_to(user_data["status"])

    # 3. PATCH

    patch_data = {
        "name": "PATCH Updated User",
        "email": f"telaRa@{time.time()}.com",
        "gender": "male",
        "status": "active"
    }

    with allure.step("Update user using PATCH"):
        response_patch = gorest_user.user_patch(
            user_id=user_id,
            dict_validate=patch_data
        )

    with allure.step("Verify PATCH response"):
        assert_that(response_patch["id"]).is_equal_to(user_id)
        assert_that(
            response_patch["name"]
        ).is_equal_to(patch_data["name"])
        assert_that(
            response_patch["email"]
        ).is_equal_to(patch_data["email"])
        assert_that(
            response_patch["gender"]
        ).is_equal_to(patch_data["gender"])
        assert_that(
            response_patch["status"]
        ).is_equal_to(patch_data["status"])

    # 4. READ after PATCH

    with allure.step("Get user after PATCH"):
        response_get_after_patch = gorest_user.user_get(
            user_id=user_id
        )

    with allure.step("Verify user data after PATCH"):
        assert_that(
            response_get_after_patch["id"]
        ).is_equal_to(user_id)
        assert_that(
            response_get_after_patch["name"]
        ).is_equal_to(patch_data["name"])

    # 5. PUT

    put_data = {
        "name": "PUT Updated User",
        "email": f"put{time.time()}@example.com",
        "gender": "female",
        "status": "inactive"
    }

    with allure.step("Update user using PUT"):
        response_put = gorest_user.user_put(
            user_id=user_id,
            dict_validate=put_data
        )

    with allure.step("Verify PUT response"):
        assert_that(response_put["id"]).is_equal_to(user_id)
        assert_that(
            response_put["name"]
        ).is_equal_to(put_data["name"])
        assert_that(
            response_put["email"]
        ).is_equal_to(put_data["email"])
        assert_that(
            response_put["gender"]
        ).is_equal_to(put_data["gender"])
        assert_that(
            response_put["status"]
        ).is_equal_to(put_data["status"])

    # 6. READ after PUT

    with allure.step("Get user after PUT"):
        response_get_after_put = gorest_user.user_get(
            user_id=user_id
        )

    with allure.step("Verify user data after PUT"):
        assert_that(
            response_get_after_put["id"]
        ).is_equal_to(user_id)
        assert_that(
            response_get_after_put["name"]
        ).is_equal_to(put_data["name"])
        assert_that(
            response_get_after_put["email"]
        ).is_equal_to(put_data["email"])
        assert_that(
            response_get_after_put["gender"]
        ).is_equal_to(put_data["gender"])
        assert_that(
            response_get_after_put["status"]
        ).is_equal_to(put_data["status"])

    # 7. DELETE

    with allure.step("Delete user"):
        response_delete = gorest_user.user_delete(user_id)

    with allure.step("Verify DELETE response"):
        assert_that(response_delete).is_equal_to(204)

    # 8. VERIFY DELETE

    with allure.step("Verify user was deleted"):
        gorest_user.user_get(
            user_id=user_id,
            exp_status_code=404
        )

    print(f"User ID {user_id} successfully deleted")