import paho.mqtt.client as mqtt

class MqtttClientConnection:
    def __init__(self, broker_ip: str, port: int, client_name: str, keepalive=60):
        self.__broker_ip = broker_ip
        self.__port = port
        self.__client_name = client_name
        self.__keepalive = keepalive

    # Função de startar a conexão
    def start_connection(self):
        # Definindo o client 
        mqtt_client = mqtt.Client(self.__client_name)
        # Realizando a conexão de fato 
        mqtt_client.connect(host=self.__broker_ip, port=self.__port, keepalive=self.__keepalive)
        # Realiza sempre um loop pra semprer procurar mensagem do broker
        mqtt_client.loop_start()
