from pymodm import connect, MongoModel, fields

connect("mongodb+srv://alex_thomason:Highbar96@bme547.cajq2.mongodb.net/health_db?retryWrites=true&w=majority")

class User(MongoModel):
    name=fields.CharField()

x = User(name="David")
x.save()