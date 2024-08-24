from app.domain.checkin.checkin_service import CheckinService
from app.infrastructure.util.logz import create_logger
import threading
import random
from paho.mqtt import client as mqtt_client
from dynaconf import settings
from app.domain.uncheck_user.uncheck_user_service import UncheckUserService

client_id = f'publish-{random.randint(0,10000)}'

class Checkin():
    def __init__(self, checkinService : CheckinService):
        self.checkinService = checkinService 
        self.broker = settings.get('BROKER_URL')
        self.port = settings.get('BROKER_PORT')
        self.topic = settings.get('BROKER_TOPIC')
        self.logger = create_logger(f'[bold cyan]Consumer:[bold yellow]{self.topic}[/bold yellow][/bold cyan]')
        
    def run(self):
        thead = threading.Thread(target=self.worker)
        thead.start()   

    def connect_mqtt(self):
        def on_connect(client,userdata, flags, rc):
            if rc == 0:
                print("CONNECTED IN MQTT SERVER:✔️")
            else:
                print(f"FAILED TO CONNECT:❌ - error code : {rc} ")
                
        client = mqtt_client.Client(client_id)
        self.logger.info("🚩 [yellow] Try connect in MQTT Server[/yellow]")
        client.on_connect = on_connect
        client.connect(self.broker, self.port)
        self.logger.info(f"New client MQTT in {self.broker + ":" + str(self.port)}")
        return client
        
    def worker(self):
        def on_message(client, userdata, msg):
            self.logger.info(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic 📭")
            self.checkinService.checkin(msg.payload.decode())
            
        client = self.connect_mqtt()
        client.subscribe(self.topic)
        client.on_message = on_message
        self.logger.info(f"Subscribe in {self.topic} 📪")
        client.loop_forever()
