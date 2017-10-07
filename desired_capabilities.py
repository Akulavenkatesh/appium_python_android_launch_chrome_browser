import os


def get_desired_capabilities():
    desired_caps = {
        'platformName': 'iOS',
        'platformVersion': '10.3',
        'deviceName': 'iPhone 7',
        'browserName': 'Safari',
        'autoAcceptAlerts': 'true',
    }
    return desired_caps
