from confluent_kafka import Consumer

default_config = {
	'bootstrap.servers': 'localhost:9092',
	'group.id': '0',
}


class ConsumerGetter:
	def __init__(self, config=None):
		if config is None:
			config = default_config
		self.config = config
		self.consumer = Consumer(self.config)
	
	def set_config(self, config: dict):
		self.config = config
		self.consumer = Consumer(self.config)
	
	def subscribe_topics(self, topics: list):
		self.consumer.subscribe(topics)
	
	def start(self):
		while True:
			msg = self.consumer.poll(1.0)
			
			if not msg:
				continue
			if msg.error():
				print(f'Consumer error: {msg.error()}')
				continue
			
			if msg.value().decode("utf-8") == 'END':
				self.consumer.close()
				break
			
			print(f'Received Message: {msg.value().decode("utf-8")}')
		print('Ended')


def test():
	getter = ConsumerGetter()
	getter.subscribe_topics(['test'])
	getter.start()


if __name__ == '__main__':
	test()
