from pushbullet import Pushbullet

ACCESS_TOKEN = None

pb = Pushbullet(ACCESS_TOKEN)

device = pb.get_device('Galaxy S7')
device.push_note('Test Message', 'Hello World, from Python!')
