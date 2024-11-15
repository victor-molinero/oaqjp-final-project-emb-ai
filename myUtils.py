import json

class CustomDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)
    def object_hook(self, obj):
        for key, value in obj.items():
            if value == 'null':
                obj[key] = None
        return obj
