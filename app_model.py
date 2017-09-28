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
                indeces = 0
                for item in self.todo_list:
                    indeces += 1
                    print(str(indeces) + " - " + str(item))
    
    def add(self, todo):
        with open("todos.txt", "a") as self.file:
            self.file.write("0" + " " + todo + "\n" )
    
    def remove(self, index):
        with open("todos.txt", "w") as self.file:
            del self.todo_list[int([1]) - 1]
            self.todo_list.write(complete + task.description + "\n")

    

