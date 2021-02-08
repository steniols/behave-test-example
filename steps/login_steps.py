from behave import *
from pages.login_page import LoginPage
from nose.tools import assert_equal

loginPage = LoginPage()


@given('que acesso a página de Login')
def step_impl(context):
    loginPage.acess_page('https://s2.demo.opensourcecms.com/orangehrm/symfony/web/index.php/auth/login')


@given('que preencho o campo username com opensourcecms')
def step_impl(context):
    loginPage.send_keys_input_user()


@given('que preencho o campo de password com opensourcecms')
def step_impl(context):
    loginPage.send_keys_input_password()


@when('clico no botão login')
def step_impl(context):
    loginPage.click_button_login()


@then('devo visualizar a tela inicial com No Employees Available')
def step_impl(context):
    assert_equal(loginPage.get_result_text(), 'No Employees Available')