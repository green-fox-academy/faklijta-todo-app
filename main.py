import sys
from usage import Usage
from app_model import ToDoModel

def start():
    argument = sys.argv[1:]
    list_item = ToDoModel()
    usage = Usage()
    if not argument:
        usage.usage_info()
    elif argument[0] == "-l":
        list_item.list_todo()
    elif argument[0] == "-a":
        list_item.add(sys.argv[2])
    elif argument[0] == "-r":
        list_item.remove(sys.argv[2])
    elif argument[0] == "-c":
        list_item.list_todo
        
start()            