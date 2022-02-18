
class Component(object):

    @classmethod
    def name(cls):
        return "component"

    def load(self, conf_dict):
        self._load(conf_dict)

    def _load(self, conf_dict):
        raise NotImplementedError

    def process(self, message):
        raise NotImplementedError

    def train(self):
        raise NotImplementedError

class ClassFactory:

    @staticmethod
    def all_subclasses(cls):
        """Returns all known (imported) subclasses of a class."""
        _sub_cls_lst = [g for s in cls.__subclasses__() for g in ClassFactory.all_subclasses(s)]
        return cls.__subclasses__() + _sub_cls_lst

    @staticmethod
    def all_classes(cls):
        return ClassFactory.all_subclasses(cls) + [cls]

    @staticmethod
    def subclasses_dict(cls):
        assert issubclass(cls, Component)
        subclasses = ClassFactory.all_classes(cls)
        sub_dict = {}
        for sub_cls in subclasses:
            sub_name = sub_cls.name()
            if sub_name in sub_dict:
                raise Exception("class {} and {} have the same name".format(
                    sub_dict[sub_name], sub_cls))
            sub_dict[sub_name] = sub_cls
        return sub_dict