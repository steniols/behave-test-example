from browser import Browser


def before_all(context):
    context.browser = Browser()

def after_all(context):
    context.browser.browser_quit()

def after_scenario(context, scenario):
    context.browser.browser_clear()
