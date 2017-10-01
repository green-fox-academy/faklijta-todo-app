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
                for i, self.todo_list in enumerate(self.todo_list):
                    print(str(i+1) + " - " + str(self.todo_list))
    
    def add(self, todo):
        with open("todos.txt", "a") as self.file:
            self.file.write("0" + " " + todo + "\n" )
    
    def remove(self, index):
            f = open("todos.txt", 'r')
            listed = list(f)
            del listed[int(index)-1]
            f = open("todos.txt", 'w')
            for line in listed:
                f.write(line)
            f.close()
        # with open("todos.txt", "w") as self.file:
        #     self.todo_list.remove(self.todo_list[int(index)-1])
        #     self.file.write("0" + " " + todo + "\n" )
    
    def status(self, status):
        self.todo_list[int(index)-1]["checked"] = True
        self.write()

    

