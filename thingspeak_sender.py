import urllib.request as ul

ACCESS_TOKEN = ''


def send_data(field):
    ul.urlopen('https://api.thingspeak.com/update?api_key=' + ACCESS_TOKEN + '&field' + field + '=1')


def send_motion_data():
    send_data('2')


def send_alert_data():
    send_data('1')

