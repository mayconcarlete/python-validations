from src.validations.index import ValidatorComposite, RequiredField

def makeValidatorFactory():
    errorsArray = []
    errorsArray.append(RequiredField('name'))
    errorsArray.append(RequiredField('zipCode'))

    return ValidatorComposite(errorsArray)