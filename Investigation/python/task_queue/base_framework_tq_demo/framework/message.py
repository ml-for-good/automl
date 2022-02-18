
class Message(object):

    def __init__(self, query, data=None):
        self._data = {}
        self._output = {}
        for key in query:
            self.set(key, query[key], True)
        for key in data or {}:
            self.set(key, data[key])

    def set(self, key, val, add_to_output=False):
        self._data.update({key: val})
        if add_to_output:
            self._output.update({key: val})

    def get(self, key, default=None):
        return self._data.get(key, default)

    @property
    def output(self):
        return self._output