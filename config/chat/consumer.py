import json

from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):

        self.room_name=self.scope["url_route"]["kwargs"]["room_name"]
        self.room_id=f"chat_{self.room_name}"

        async_to_sync(self.channel_layer.group_add)(
            self.room_id,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):

        async_to_sync(self.channel_layer.group_discard)(
            self.room_id,
            self.channel_name
        )


    def receive(self, text_data):

        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        if text_data:

            text_data_json=json.loads(text_data)
            print("$$$$$$$$$$$$$$$$$$$$")
            print("$$$$$$$$$$$$$$$$$$$$")
            print(text_data_json)
            print("$$$$$$$$$$$$$$$$$$$$")
            print("$$$$$$$$$$$$$$$$$$$$")
            async_to_sync(self.channel_layer.group_send)(
                self.room_id,
                {
                    "type":"chat_message",
                    "text":text_data
                }
            )

        # self.send(text_data=json.dumps({"message": message}))


    def chat_message(self,event):
        print(event)
        print("$$$$$$$$$$$$$$$$$$$$")
        print("$$$$$$$$$$$$$$$$$$$$")
        print("$$$$$$$$$$$$$$$$$$$$")
        print("$$$$$$$$$$$$$$$$$$$$")
        # message=event["message"]
        self.send(text_data=event["text"])