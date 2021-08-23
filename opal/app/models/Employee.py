#models.Employee
from app.schema.globalSchema import AddressSchema, BooleanType, ContactSchema,  DictType, EmailType, IntType, NextOfKinSchema,  Model, ModelType,  StringType, blacklist

class EmployeeSchema(Model):
    ''' A Person or Machine Employed to do work'''  
    access = StringType(default="public") # access = public | private  
    imgurl = StringType()
    fname = StringType()
    lname = StringType()
    alias = StringType()
    dob = IntType()
    occupation = StringType()
    contact = ModelType(ContactSchema)
    address = ModelType(AddressSchema)
    nok = ModelType(NextOfKinSchema)
    
    class Options:
        roles = {'public': blacklist('dob', 'address', 'nok')}



class Employee:

    pass