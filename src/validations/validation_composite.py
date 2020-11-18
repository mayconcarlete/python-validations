from src.presentation.protocols.validate import IValidate
from typing import List, Any,Union

class ValidatorComposite(IValidate):
    def __init__(self, validators:List):
        self.validators = validators
    def validate(self, input:Any)->Union[None, Exception]:
        for validator in self.validators:
            error = validator.validate(input)
            if error is not None:
                raise error
        return None         