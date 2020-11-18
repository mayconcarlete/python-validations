from abc import ABCMeta, abstractproperty
from typing import Any, Union

class IValidate(metaclass = ABCMeta):
    @abstractproperty
    def validate(self, input:Any)->Union[None, Exception]:
        pass

#__all__ = ['IValidate']
