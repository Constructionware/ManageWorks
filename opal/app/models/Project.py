#models.Project
import orjson as json
from asyncio import sleep
from asyncio.locks import Semaphore
from aspiredb.database import Controller

from aspiredb.core.encriptor import GenerateId
from app.schema.globalSchema import AddressSchema, BooleanType, ContactSchema, CommentSchema,  DictType, EmailType, EventSchema, IntType, ListType, LocationSchema,  MD5Type, Model, ModelType, NoteSchema, PhaseSchema, StateSchema, StringType, blacklist
from app.models.Task import TaskSchema


class ProjectSchema(Model):
    ''' A Managed Job of Multiple Tasks with more than one worker and a timeframe .'''
    access = StringType(default="public") # access = public | private   
    address = ModelType(AddressSchema)
    comments = ListType(ModelType(CommentSchema))
    event = ModelType(EventSchema)     
    employees = ListType(StringType())
    location = ModelType(LocationSchema)   
    name = StringType()
    notes =  ListType(ModelType(NoteSchema)) 
    phases = ListType(ModelType(PhaseSchema))
    project_type = StringType()    
    state = ModelType(StateSchema)    
    tasks = ListType(ModelType(TaskSchema))   

    class Options:
        roles = {'public': blacklist('notes', 'location', 'meta_data')}


class DataProcessor:
    def __init__(self) -> None:
        
        ''' '''
    def process_new_project(self, data:dict=None):
        return dict(
            access = data.get('access'), 
            address = data.get('address'), 
            comments = data.get('comments'), 
            event = data.get('event'),      
            employees = data.get('employees'), 
            location = data.get('location'),    
            name = data.get('name'), 
            notes =  data.get('notes'),  
            phases = data.get('phases'), 
            project_type = data.get('project_type'),     
            state = data.get('state'),     
            tasks = data.get('tasks')
        )
        
    def ready_data_state (self, args, **kwargs ):
        # Capture a checksum of the schematized portion of project data
        ready_data = { "checksum": self.hash_data(data=args) } 
        # Update with additional optional properties
        # Expecting _id:str, meta_data:dict, Any:int, Any:float, Any:dict, Any:list
        for key in kwargs.keys():
            ready_data[key] = kwargs.get(key)
        # Merge with schemaized data
        ready_data = ready_data | args
        # Data is now ready for storage
        return ready_data

    def hash_data(self, data:dict=None):
        from hashlib import md5
        try:
            return md5(json.dumps(data)).hexdigest()
        except Exception as e:
            return str(e)
        finally:
            del(md5)
            del(data)



class Project( DataProcessor ):
    ''' A Project object exposing two properties,
    and empty id field and an index of existing projects that is auto loaded at call time .
    The Ojbect can be called with or without data,
    Data can also be mounted into an existing Project Object overwriting its original values with new data 
    self.data becomes available at  mount time or at initialization with data 
    self.data.name = The project name,
    self.data.address
        address.lot
        address.street
        address.town
        address.city_parish
        address.country
    
    '''
    _id:str = None  # The Unique Identifier of a Project
    index:set = set() # A Set of Id's used to validate existing projects
    meta_data = DictType(StringType)


    def __init__(self, data:dict=None):  # A Project can be Initilaized with Data on the fly  
            
        if data:
            processed = self.process_new_project(data=data)

            self.data = ProjectSchema(processed)
            self.generate_id(data['name'])
        else:
            self.generate_id('system project')

    # Functions
    @property
    def con(self):
        return Controller()

    @property
    def handle(self):
        return self.con.handle
    
    def generate_id(self, nn):
        # Generates a new unique id 
        gena = GenerateId() 

        def isSpace(stringlist):
            return " " in stringlist 

        if self._id: # Id exist 
            pass
        if isSpace(nn):
            self._id = gena.name_id(nn, nn.split()[1])  
        else: 
            self._id = gena.name_id(nn, nn[1])              
    
    # MOUNTS
    def mount(self, data:dict=None):        
        if data:
            processed = self.process_new_project(data=data)
            self.data = ProjectSchema(processed)            
            self.__generate_id 
                   
        else:
            #log this event
            pass

    
    
    @property
    async def create_database(self):
        result = json.loads(await self.con.create_database( dbname='project', access="public"))
        return result

    @property
    async def loadProjects(self):        
        result = json.loads(await self.con.get_documents(dbname='project'))
        return result

    async def get_project(self, id):
        result = json.loads( await self.con.get_document(dbname='project', doc_id=id))
        return result

    async def create(self, data):
        project = self.mount(data)
        result = json.loads(await self.con.create_document(database='project', data=data))
        return result

    async def create_private(self, data, password):
        result = json.loads(await self.con.create_document(dbname='project', data=data, password=password))
        return result

    async def update(self, id,  data):
        result = json.loads(await self.con.update_document(database='project', doc_id=id,  data=data))
        return result

    async def delete(self, id):
        #result = json.loads(await self.con.delete_document(database='project', data=data))
        result = None
        return result

    async def clone(self, id, clone_id):
        result = json.loads( await self.con.clone_doc(dbname='project', doc_id=id, clone_id=clone_id))
        return result



    def __repr__(self) -> str:
        data = {
            "_id": self._id

        }
        
        return f"Opal's Project Model Properties {data}"
   

async def setup_project():
    temp = Project()
    await sleep(0.05)
    status = await temp.create_database
    print(f"Opal Database Status: {status}")
    await sleep(0.05)    
    del(status)
    del(temp)
    return None
