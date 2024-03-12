import allure
from demoqa_tests.data.users import user, user_interests
from demoqa_tests.pages.registration_page import RegistrationPage


def test_fill_out_the_form():
    registration_page = RegistrationPage()

    with allure.step("Open registration form"):
        registration_page.open()

    with allure.step("Filling out the form"):
        registration_page.registration(user)

    with allure.step("Check if it is filled out correctly"):
        registration_page.modal_window_check(user, user_interests)