from src.validations.index import RequiredField, TypeField
from src.presentation.errors.missing_param_error import MissingParamError
from src.main.factories.make_error_factory import makeValidatorFactory

httpRequest = {
    'body':{
        'name':'Maycon Carlete',
        'phone':'33218600'
    }
}


try:
    checkErrors = makeValidatorFactory().validate(httpRequest['body'])
    print(checkErrors)
except MissingParamError as e:
    print(e)