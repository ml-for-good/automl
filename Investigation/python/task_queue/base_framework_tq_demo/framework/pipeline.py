import time

from framework.component import Component, ClassFactory
from utils.tool import read_json

class _BasePipeline(object):

    def __init__(self):
        self._sub_component_dict = ClassFactory.subclasses_dict(Component)

    def load(self, conf):
        config = read_json(conf)
        self._load(config)
        return self

    def _load(self, config):
        raise NotImplementedError

    def process(self, message):
        raise NotImplementedError

    def train(self, message):
        raise NotImplementedError


class LongCallBackPipeline(_BasePipeline):

    def __init__(self):
        self._pipeline = []
        super(LongCallBackPipeline, self).__init__()

    @staticmethod
    def _add_pipeline(sub_component_dict, pipeline_list, component):
            comp_name = component['name']
            comp_conf = component['conf']
            assert comp_name in sub_component_dict, \
                "Wrong component nane {}".format(comp_name)
            comp_obj = sub_component_dict[comp_name]()
            comp_obj.load(comp_conf)
            pipeline_list.append(comp_obj)

    def _load(self, config):
        for component in config:
            # print("loading:{}".format(component))
            self._add_pipeline(
                self._sub_component_dict, 
                self._pipeline, 
                component
            )
    
    def process(self, message):
        # TODO: implement task queue pipeline based on Celery
        try:
            for comp in self._pipeline:
                st = time.time()
                comp.process(message)
                et = time.time()
                print("comp:{}, cost:{:.2f}ms".format(comp.name(), round((et-st)*1000)))
        except Exception as e:
            raise ValueError("fail to process a comp, sine {}".format(e))
        


