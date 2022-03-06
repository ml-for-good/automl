import os
import flask
import flask_restful
from flask_cors import CORS

from GLOBAL_KEY import *
from module_manager import *

app = flask.Flask(__name__)
api = flask_restful.Api(app)
CORS(app,  resources={r"/*": {"origins": "*"}})


handler_lst = [
    (TaskQueueHandler, '/tq', 'config/tq_test.json'),
]

for handler, path, conf in handler_lst:
    LAST_CONFIG_MODIFY_TIME[conf] = os.stat(conf).st_mtime 
    handler.initialize(conf)
    api.add_resource(handler, path)


if __name__ == "__main__":
    schedule.start()
    app.run(host='0.0.0.0', port='8030', debug=True)