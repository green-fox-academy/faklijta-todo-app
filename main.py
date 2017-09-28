import sys
from usage import Usage

class Main(object):
    def __init__(self):
        self.actions = [
            {"arg" : "l", "desc" : "Lists all the tasks"},
            {"arg" : "a", "desc" : "Adds a new task"},
            {"arg" : "r", "desc" : "Removes an task"},
            {"arg" : "c", "desc" : "Completes an task"},]


def start():
    arguments = sys.argv[1:]
    usage = Usage()
    if not arguments:
        usage.usage_info()

start()            


    # def add_item():
    #     pass
        
    # def list_items():
    #     pass

    # def remove_item():
    #     pass

    # def complete_item():
    #     pass

