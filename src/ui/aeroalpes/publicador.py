import pulsar

from .utils import consultar_schema_registry, obtener_schema_avro_de_diccionario, broker_host

client = pulsar.Client(f'pulsar://{broker_host()}:6650')
producer = client.create_producer('comandos-reservas')

for i in range(10):
    producer.send(('Hola-Pulsar-%d' % i).encode('utf-8'))

client.close()