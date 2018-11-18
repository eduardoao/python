
#This is my first hands on in python. 
#This sample show how to use it for deploy a API application with python
# Eduardo Alcantara de Oliveira 
# 11/17/2018 22:30 PM

#First we import the bottle in projetc.
#If you don't package just run the command below: 
# pip install bottle. (garrafa mesmo).
from bottle import run, get, post, request, delete 

#fake list to test.
animals= [
            {'name': 'python' , 'type': 'Snake' },
            {'name': 'Zed' , 'type': 'Zebra' },
            {'name': 'Gira' , 'type': 'Girafa' }
]

#Method for return all animals in list. 
@get('/animal')
def getAll(): 
    return {'animals' : animals}

@get('/animal/<name>')
def getOne(name): 
    the_animal = [animal for animal in animals if animal['name'] == name]
    return {'animal': the_animal[0] }

@post('/animal')
def addOne():
    new_animal = {'name': request.json.get('name'), 'type': request.json.get('type')}
    animals.append(new_animal)
    return {'animals' : animals}

@delete('/animal/<name>')
def removeOne(name): 
    the_animal = [animal for animal in animals if animal['name'] == name]
    animals.remove(the_animal[0])
    return {'animals': animals }

#This command is necessary for run a webserver. 
run(reloader=True, debug=True)