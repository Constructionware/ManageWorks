#models.Project

from app.schema.globalSchema import AddressSchema, BooleanType, ContactSchema, CommentSchema,  DictType, EmailType, EventSchema, IntType, ListType, LocationSchema, Model, ModelType, NoteSchema, PaymentStatusSchema,  PhaseSchema, StateSchema, StringType,UnitPriceSchema,  blacklist

#Job Schemas
class TaskSchema(Model):
    ''' An Item of Work on a particulat Project ...is  Shared '''  
    access = StringType(default="public") # access = public | private  
    title = StringType(required=True, max_length=102)
    description = StringType(max_length=102)
    metric = ModelType(UnitPriceSchema)
    imperial = ModelType(UnitPriceSchema)    
    state = ModelType(StateSchema)
    event = ModelType(EventSchema)   
    assigned = BooleanType(default=False)
    assignedto = StringType()
    phase = StringType(max_length=62)
    paid = ModelType(PaymentStatusSchema)
    comment = StringType(max_length=256)    
    class Options:
        roles = {'public': blacklist('notes', 'location', 'meta_data')}



class Task:
    meta_data = DictType(StringType)

    pass