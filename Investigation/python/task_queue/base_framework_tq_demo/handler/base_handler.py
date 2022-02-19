
import time
import flask
import flask_restful
from framework import _BasePipeline, LongCallBackPipeline

class BaseHandler(flask_restful.Resource):

    @classmethod
    def name(cls):
        return 'base_handler'

    @classmethod
    def initialize(cls, conf):
        worker = getattr(cls, cls.name() + '_processor', None)
        if worker is None:
            pipe = LongCallBackPipeline().load(conf)
            setattr(cls, cls.name() + '_processor', pipe)
        time.sleep(1)
    
    @property
    def processor(self):
        return getattr(self, self.name() + '_processor', None)
        
    def get(self):
        return "get_index"

    def post(self):
        try:
            inputs = flask.request.get_json(force=True)
            msg = self._default_check(inputs)
            outputs = self._process(msg)
        except Exception as e:
            return self._error_output(e)
        return outputs

    def _process(self, message):
        self.processor.process(message)
        outputs = self._success_output(message)
        return outputs

    def _default_check(self, inputs):
        raise NotImplementedError

    def _print_log(self, inputs, outputs):
        raise NotImplementedError

    def _success_output(self, process_msg):
        raise NotImplementedError

    def _error_output(self, e):
       return {"status": -1, "info":"error", "exception":e}

