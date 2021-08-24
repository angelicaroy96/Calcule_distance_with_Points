# CODE to present the form in a web navigator

# import libraries
import logging

from flask import Flask
from flask import render_template
from flask import request
from flask import Blueprint
from modules.coor_direc import Coordinates
from modules.create_file_log.crear_log import Crear_log
# import class that calculate

# create a Falsk object
app = Flask("myapp", template_folder="templates")
#app = Blueprint('admin',__name__, template_folder='templates') 

# create a instances of a the class Coordinates
coordinates = Coordinates()

# method to prenset the form where you write the address


@app.route('/inicio')
def inicio():
    return render_template("formulario.html")

# method to prenset the page where show the address result


@app.route('/procesar', methods=['POST', 'GET'])
def procesar():
    # if that compare if method is POST
    if request.method == 'POST':
        # result save the data that recive in the form
        result = request.form.get("direccion")
        # call to the function "calcular_cordenadas"
        # to calculate the coordinates of the address
        cords = coordinates.calcular_coordenadas(result)
        # calculate the distance between the address and the Moscow Ring Road
        distance = coordinates.haversine(cords)
        # in kilometers
        radius = 1.00
        # check is the distance is less that the "radius"
        if distance <= radius:
            # create an instance of the class Crear_log
            crear = Crear_log()
            crear.crear_archivo()
            # write in the file .log
            crear.inside(logging)
            # write in the .log file this message
            return("<h1>Inside of the Area</h1>")
        else:
            # create an instance of the class Crear_log
            crear = Crear_log()
            crear.crear_archivo()
            # write in the file .log
            crear.outside(logging, distance)
            # write in the .log file this message
            return("""<h1>Outside the Area Distance (km): {}</h1>""".format(distance))



if __name__ == "__main__":
# run the application that we create in line 13
    app.run()
