from pages.login_page import LoginPage

def test_valid_login(driver):
    login = LoginPage(driver)
    login.open()
    login.login("student", "Password123")

    assert "logged-in-successfully" in driver.page_source