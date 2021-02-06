import urllib.request as ul

ACCESS_TOKEN = 'CAXKXAL98TK3WTG7'


def send_data(field):
    ''' Sends a value of 1 to a specified field '''
    ul.urlopen('https://api.thingspeak.com/update?api_key=' + ACCESS_TOKEN + '&field' + field + '=1')


def send_alert_data():
    ''' Sends a value of 1 to field one '''
    send_data('1')


def send_motion_data():
    ''' Sends a value of 1 to field two '''
    send_data('2')
