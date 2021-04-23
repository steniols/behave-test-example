from behave import *
from nose.tools import assert_equal
from pages.login_page import LoginPage

loginPage = LoginPage()


@given("que acesso a página de Login")
def step_impl(context):
    loginPage.acess_page("https://opensource-demo.orangehrmlive.com/")


@given("que preencho o campo username com Admin")
def step_impl(context):
    loginPage.send_keys_input_user()


@given("que preencho o campo de password com admin123")
def step_impl(context):
    loginPage.send_keys_input_password()


@when("clico no botão login")
def step_impl(context):
    loginPage.click_button_login()


@then("devo visualizar a tela inicial com Dashboard")
def step_impl(context):
    assert_equal(loginPage.get_result_text(), "Dashboard")
