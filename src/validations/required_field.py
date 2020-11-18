from src.presentation.protocols.validate import IValidate
from src.presentation.errors.missing_param_error import MissingParamError
from typing import Any, Union

class RequiredField(IValidate):
    def __init__(self, paramName:str):
        self.paramName = paramName
        
    def validate(self, input:Any)->Union[None, Exception]:
        if input.get(self.paramName) is not None:
            return None
        else:
            raise MissingParamError(self.paramName)
            #return MissingParamError(self.paramName)

