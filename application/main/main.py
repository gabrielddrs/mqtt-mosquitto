import time
from application.configs.broker_configs import broker_configs
from .mqtt_connection.mqtt_client_connection import MqtttClientConnection

def start():
    mqtt_client_connection = MqtttClientConnection(
        broker_configs["HOST"],
        broker_configs["PORT"],
        broker_configs["CLIENT_NAME"],
        broker_configs["KEEPALIVE"]
    )
    mqtt_client_connection.start_connection()

    while True:
        time.sleep(0.001)
