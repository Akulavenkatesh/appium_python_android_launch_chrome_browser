import os


def get_desired_capabilities():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '6.0.1',
        'deviceName': 'Sony',
        'browserName': 'Chrome',
        'autoAcceptAlerts': 'true',
    }
    return desired_caps
