
import flask
import flask_restful
from framework.message import Message
from handler.base_handler import BaseHandler

class TaskQueueHandler(BaseHandler):
    
    @classmethod
    def name(self):
        return "taskqueue_handler"

    def _default_check(self, inputs):
        """
        do some check, then transfer inputs to message object
        """
        msg = Message(inputs)
        return msg
    
    def _success_output(self, process_msg):
        """
        transfer pressed message to dict, then do some check
        """
        outputs = process_msg.output
        outputs.update({"status": 1, "info":"success"})
        return outputs
