import sys

class ToDoModel(object):
    def __init__(self):
        self.todo_list = []

    def list_todo(self):
        with open("todos.txt", "r") as items:
            self.todo_list = items.read().split('\n')
            print(self.todo_list)
    
    def add(self, todo):
        with open("todos.txt", "a") as self.file:
            self.file.write('\n' + "0" + " " + todo)
    
    def remove(self, index):
        del self.todo_list[int(sys.argv[2])-1]
        self.file.write()
