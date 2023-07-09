class Node:
    def __init__(self,value) -> None:
        self.value = value;

class Tree():
    def __init__(self) -> None:
        self.root = None;
        self.branches = [];

    def add_node(self,value):
        if self.root == None:
            self.root = Node(value);
            return;
        self.root.children.append(Node(value));
        return self.children;

    def print_tree(self):
        if self.root == None:
            return;
        print(self.root.value);
        for child in self.children:
            print(child.value);
    
    def addBranch(self,branch):
        self.branches.append = branch;
    


# t = Tree();
# t.add_node(10);
# t.add_node(20);
# t.add_node(30);
# t.print_tree();

class Human:
    def __init__(self) -> None:
        self.cool = True;
        print(self.cool);
    def say_bro(self):
        print("it`s human bro");
class Animal:
    def __init__(self) -> None:
        self.legs = 4;
        self.tail = True;
    @property
    def legs(self):
        return self.legs;
    @legs.setter
    def legs(self,value):
        self.value = value;

class Person(Human,Animal):
    def __init__(self) -> None:
        self.human = Human();
        self.human.cool = True;
        super().__init__();
        super().say_bro();
        self.human.pr = self.print_info();

    def print_info(self):
        print("Hello world");

def iter(n):
    for i in range(5):
        yield i;


def pattern_show(n,res = ""):
    if n < 1:
        return;
    for i in range(n):
        if i % 2 == 0:
            res+="*";
        if i % 2 == 1:
            res+="#";
        print(res);
    # print(res);
# pattern_show(4,"");

def pascal_triangle(n,stroka = "",arr = []):
    if n == 1:
        return [1];
    if n == 2:
        return [1,1];
    arr = [1,1];
    res = [];
    if n > 2:
        for j in range(n):
            for i in range(0,j):
                if i == 1:
                    res.append(1);
                if i == len(arr):
                    res.append(1);
                if i >0 and i < len(res) - 1:
                    res.append(res[i-1] + res[i+1]);
                    pass;
                
        print(res);

