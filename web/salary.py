from bottle import (
    route,
    run,
    template
)
from bottle import static_file
import json

def _salary():
    salaries = []
    current = 50000
    for i  in range(0,20):
        if i > 15:
            salaries.append(0)
        else:
            current = current + current * float(10.0/100)
            salaries.append(current)

    return salaries
        

def _food():
    fexpenses = []
    current = 10000
    for i  in range(0,20):
        current = current + current * float(12.0/100)
        fexpenses.append(current)
    return fexpenses

def _education():
    eexpenses = []
    current = 3000
    for i  in range(0,20):
        current = current + current * float(18.0/100)
        eexpenses.append(current)
    return eexpenses


def _rent():
    rexpenses = []
    current = 12000
    for i in range(0,20):
        current = current + current * float(8.0/current)
        rexpenses.append(current)
    return rexpenses


@route('/visualize')
def visualize():
    salaries = _salary()
    foods = _food()
    educations = _education()
    rents = _rent()
    context = [
        ]
    for i,a,b,c,d in zip(range(0,20),salaries, foods, educations, rents):
        context.append({'Year':2013 + i ,
                        'Salary': a,
                        'food' : b,
                        'education': c,
                        'rent': d,
                        })
        
        
    return json.dumps(context)


@route('/<filepath:path>')
def server_static(filepath):
        return static_file(filepath, root='/home/amit/dc.js/web')


run(host='localhost', port=8080)

