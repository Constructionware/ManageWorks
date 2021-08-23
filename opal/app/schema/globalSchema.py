#globalSchema.py

#................... Dependencies ................................

from schematics.models import Model
from schematics.types import (BooleanType, EmailType, StringType, FloatType, IntType, NumberType, DateTimeType, ListType, DictType, MD5Type, ModelType, TimestampType)
from schematics.transforms import blacklist



class StateSchema(Model):
    '''The Motive Condition of a Project or Task'''
    active = BooleanType(default=False)
    complete = BooleanType(default=False)
    pause = BooleanType(default=False)  
    terminate = BooleanType(default=False)


class EventSchema(Model):
    """Time Record of an action taken """
    started = IntType()
    completed = IntType()
    paused = ListType(IntType())
    restart = ListType(IntType())
    terminated = IntType()


class PhaseSchema(Model):
    """Construction Phase """   
    name = StringType(required=True, max_length=62)
    started = IntType()
    end = IntType()
    notes = StringType(max_length=256)


class UnitPriceSchema(Model):
    ''' Records Amount of a material or thing with unit Prices '''
    unit = StringType()
    quantity = FloatType()
    price = FloatType()
    total = FloatType()

class PaymentStatusSchema(Model):
    " Task or bill payment status record"
    paid = BooleanType(default=False)
    date = IntType()
    

class CommentSchema(Model):
    ''' Coment on Tasks , Projects '''
    author = StringType(max_length=32)
    email = EmailType()
    date = IntType()
    text = StringType(max_length=128)


class NoteSchema(Model):
    ''' Take Notes on Tasks , Projects '''
    author = StringType(max_length=64)
    topic = StringType(max_length=64)
    date = IntType()
    text = StringType(max_length=256)

#Human Resources Schemas

class AddressSchema(Model):
    ''' Legal Address of a Person of Entity.'''
    lot = StringType()
    street = StringType()
    town = StringType()
    city_parish = StringType()
    country = StringType()


class LocationSchema(Model):
    ''' Geographical Point of Location of A fixed Object '''
    lat = FloatType()
    lon = FloatType()
    alt = FloatType()


class ContactSchema(Model):
    ''' Contact information of a Person or Company '''
    tel = StringType()
    mobile = StringType()
    email = EmailType()


class NextOfKinSchema(Model):
    ''' Relative or Next Person of contact of an Employee '''
    name = StringType()
    relation = StringType()
    contact = ContactSchema()
    address = AddressSchema()
