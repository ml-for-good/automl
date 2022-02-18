import time
from framework.component import Component

class ModelPredictor(Component):
    """ pretend model serving """
    @classmethod
    def name(cls):
        return 'model_predictor'

    def _load(self, conf_dict):
        self.predict_time = conf_dict.get('delay', 5)

    def _process(self, message):
        time.sleep(self.predict_time)
    
    def process(self, message):
        self._process(message)