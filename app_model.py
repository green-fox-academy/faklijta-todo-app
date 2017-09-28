import sys

class ToDoModel(object):
    def __init__(self):
        self.todo_list = []

    def list_todo(self):
        with open("todos.txt", "r") as items:
            self.todo_list = items.read().splitlines()
            if self.todo_list == []:
                print("Have fun! There are no To Dos!")
            else:
                print(self.todo_list)
    
    def add(self, todo):
        with open("todos.txt", "a") as self.file:
            self.file.write("0" + " " + todo + "\n" )
    
    def remove(self, index):
        with open("todos.txt", "w") as self.file:
            del self.todo_list[int(argument[1]) - 1]
            self.todo_list.write(complete + task.description + "\n")

    

