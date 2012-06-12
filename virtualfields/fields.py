from django.core.exceptions import ValidationError
from django.utils.simplejson import dumps, loads



class Validator(object):
    def __call__(self, value, name):
        pass


class IntegerValidator(Validator):
    def __call__(self, value, name):
        try:
            return int(value)
        except ValueError:
            raise ValidationError("%s is not a valid integer" % name)




class TextValidator(Validator):


    def __init__(self, max_length=None):
        self.max_length=max_length

    def __call__(self, value, name):
        if not isinstance(value, basestring):
            raise ValidationError("%s is not a valid string" % name)
        elif self.max_length and len(value) > self.max_length:
            raise ValidationError("%s is longer than %d" % (name, self.max_length))
            

class VirtualField(object):

    def __init__(self, parent_field="json", validator=Validator()):
        self.parent_field = parent_field
        self.validator = validator

    def contribute_to_class(self, cls, name):
        self.name = name
        self.model = cls
        cls._meta.add_virtual_field(self)
        setattr(cls, name, self)


    def clean(self, instance):
        self.validator(getattr(instance, self.name), self.name)

    def _get_data(self, instance):
        value = getattr(instance, self.parent_field)
        if value in (None, ""):
            return {}
        else:
            return loads(value)

    def _set_data(self, instance, data):
        json = dumps(data)
        setattr(instance, self.parent_field, json)

    def __get__(self, instance, instance_type=None):
        data = self._get_data(instance)
        if self.name in data:
            return data[self.name]
        return None

    def __set__(self, instance, value):
        data = self._get_data(instance)
        data[self.name] = value
        self._set_data(instance, data)



class VirtualTextField(VirtualField):
    def __init__(self, parent_field="store", max_length=None):
        self.validator = TextValidator(max_length=max_length)
        self.parent_field = parent_field


class VirtualIntegerField(VirtualField):
    def __init__(self, parent_field="store"):
        self.validator = IntegerValidator()
        self.parent_field = parent_field

    

