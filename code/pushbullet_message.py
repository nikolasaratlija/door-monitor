from pushbullet import Pushbullet

ACCESS_TOKEN = 'o.PoTFdtH5s25dcuVgNqcVDoPnBBY2NCrL'

pb = Pushbullet(ACCESS_TOKEN)


def send_alert():
	''' Sends a notification to the PushBullet service '''
	device = pb.get_device('Galaxy S7')
	device.push_note(
		'45 Minutes Have Passed', 
		'It\'s time to head out for a bit, buddy.')
