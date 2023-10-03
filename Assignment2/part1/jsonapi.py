import json
from typing import Any

"""
the student class performs the encode and decode function
    
"""
class Student():
    def __init__(self, id, name):
        """
        create the student object
        """
        self.id = id
        self.name = name
        
        
class ModifiedEncoder(json.JSONEncoder):
    def default(self, obj):
        """
        Modify the default function in encoder
        """
        name = type(obj).__name__
        try:
            encoder = getattr(self, f"encode_{name}")
        except AttributeError:
            super().default(obj)
        else:
            encoded = encoder(obj)
            encoded["__extended_json_type__"] = name
            return encoded      
          
class MyEncoder(ModifiedEncoder):
    def encode_Student(self, obj):
        """
        encode student object
        """
        return {"id": obj.id, "name": obj.name}



class ModifiedDecoder(json.JSONDecoder):
    def __init__(self, **kwargs):
        """
        the decoded object
        """
        kwargs["object_hook"] = self.object_hook
        super().__init__(**kwargs)

    def object_hook(self, obj):
        """
        modify the hook object
        """
        try:
            name = obj["__extended_json_type__"]
            decoder = getattr(self, f"decode_{name}")
        except (KeyError, AttributeError):
            return obj
        else:
            return decoder(obj)
        

class StudentDecoder(ModifiedDecoder):
    def decode_Student(self, obj):
        """
        decode student object
        """
        return Student(obj["id"], obj["name"])

# Test the result
student1 = Student(12, "sb")   
stu_encode = json.dumps(student1, cls=MyEncoder)
print(stu_encode)

print(json.loads(stu_encode, cls=StudentDecoder))
print(type(student1))




