#models.User
from app.schema.globalSchema import Model, StringType, EmailType, BooleanType,IntType, DictType, blacklist

class UserSchema(Model):
    ''' A User of The Platform ''' 
    access = StringType(default="public") # access = public | private  
    username = StringType()
    email = EmailType()
    password_hash = StringType()
    active:bool = BooleanType(default=False)    
    authenticated = BooleanType(default=False)
    role:str = StringType()
    confirmed:bool = BooleanType(default=False)
    class Options:
        roles = {"public": blacklist('password_hash', 'meta_data')}


class User:
    pass