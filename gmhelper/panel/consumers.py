import json

from channels.generic.websocket import WebsocketConsumer

class ControlConsumer(WebsocketConsumer):

  def connect(self):
    self.accept()
    self.send(text_data="asdf")

  def disconnect(self, close_code):
    pass

  def receive(self, text_data):
    json_data = json.loads(text_data)
