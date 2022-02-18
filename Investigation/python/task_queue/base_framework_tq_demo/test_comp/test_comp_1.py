import time
from framework.component import Component

class FeatureProcessor(Component):
    """ pretend feature processing """
    
    @classmethod
    def name(cls):
        return 'feature_processor'

    def _load(self, conf_dict):
        self.procss_time = conf_dict.get('delay', 5)

    def _process(self, message):
        time.sleep(self.procss_time)

    def process(self, message):
        self._process(message)