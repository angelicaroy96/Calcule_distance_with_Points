# Program that create a .log file with data.
# import the package
import logging

# create a class that with the code


class Crear_log():

    # Method that create the file .log
    def crear_archivo(self):
        # Creating the format of Logger, that is: levelname,
        # datatime and message.
        Log_Format = "%(levelname)s %(asctime)s - %(message)s"
        # line 12: Configuraation of the LOG file
        # line 12: Name of the file
        # line 13: Specified file document "write/read"
        # line 14: Specified format of the file
        # line 15: Specified type of logging level
        logging.basicConfig(filename="result.log",
                            filemode="w",
                            format=Log_Format,
                            level=logging.DEBUG)
        # Get the logger specified in the file.
        logging.getLogger(__name__)
        # Message that is going to be in the file.
        return logging

    # Method that is going to write in the file if the address
    # is inside the Area.
    def inside(self, logging):
        write = logging.debug('\nInside of the Area')
        return write

    # Method that is going to write in the file if the address
    # is outside the Area
    # and the calcule of the distance
    def outside(self, logging, distance):
        write = logging.debug("""\nOutside of the
        Area Distance (km): {}""".format(distance))
        return write
