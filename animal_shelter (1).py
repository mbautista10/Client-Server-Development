from pymongo import MongoClient
#from bson.json_util import dumps
#from bson.objectid import ObjectID

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:54603/AAC' % (username, password))
     
        self.database = self.client['AAC']

    # Method to implement the (C)reate in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary 
           
            return True
                    
        else:
            
            raise Exception("Nothing to save, because data parameter is empty")


    # Method to implement the (R)ead in CRUD.
    def read(self, data):

        # criteria is not None then this find will return all rows which matches the criteria
        if data is not None:        
            
            return self.database.animals.find(data,{"_id":False})

        else:
        #if there is no search criteria then all the rows will be return  
            return False

        return data
    
    # Method to implement the (U)pdate in CRUD
    def update(self, query, record):
        
        if record is not None: 
           
            self.database.animals.update_one(query, record)
        
            return True
        
        else:
           
           raise Exception("No data Updated")
            
    # Method to implement the (D)elete in CRUD
    def delete(self,data):
        
        if data is not None:
            
            return self.database.animals.delete_one(data)
            
                                                            
        else:
            
            raise Exception("No record provided")
       
        
