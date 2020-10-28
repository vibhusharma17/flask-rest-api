import os
import uuid


def random_name_generator(extension):
    target_directory = "{}/tmp".format(os.path.abspath(os.getcwd()))
    timestamp = str(uuid.uuid4())
    return f"{target_directory}/{timestamp}.{extension}"
