import mqtt_device
import time


class Display(mqtt_device.MqttDevice):
    """Displays the number of cars and the temperature"""

    def __init__(self, config):
        super().__init__(config)
        self.client.on_message = self.on_message
        self.client.subscribe('display')
        self.client.loop_forever()

    def display(self, *args):
        print('*' * 20)
        for val in args:
            print(val)
            time.sleep(1)

        print('*' * 20)

    def on_message(self, client, userdata, msg):
        data = msg.payload.decode()
        self.display(*data.split(','))
        # TODO: Parse the message and extract free spaces,\
        #  temperature, time



import json

if __name__ == '__main__':

    # TODO: Read config from file
    path = "../smartpark/config.json"
    file_handle = open(path, "r")
    config = json.load(file_handle)
    file_handle.close()

    display = Display(config)
