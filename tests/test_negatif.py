import pytest
from pages.login_page import Login

@pytest.mark.parametrize("username, password, expected_error_displayed", [
    ("invalid_user", "secret_sauce", True),
    ("standard_user", "wrong_pass", True),
    ("wrong_user", "wrong_pass", True),
])
def test_login_negatif_pom(setup, username, password, expected_error_displayed):
    login = Login(setup)
    login.input_username(username)
    login.input_password(password)
    login.click_login_button()
    assert login.is_error_displayed() == expected_error_displayed
