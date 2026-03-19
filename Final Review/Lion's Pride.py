class Lion:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []
    def add_child(self, lion):
        self.children.append(lion)
    def __str__(self):
        return f"Lion name: {self.name} Age: {self.age}"
    def print_family(self,depth=0):
        As = 'A' * depth
        Exclamations = "!" * (1 + depth)
        print(f"{self.name} says ROA{As}R{Exclamations}")
        for child in self.children:
            child.print_family(depth+1)
grandpa = Lion("Grandpa",75)
child1 = Lion("Child 1",25)
child2 = Lion("Child 2",20)
child3 = Lion("Child 3",18)
grandchild1 = Lion("Grandchild 1", 10)
grandpa.add_child(child1)
grandpa.add_child(child2)
grandpa.add_child(child3)
child3.add_child(grandchild1)
greatgrandchild1 = Lion("Great Grandchild 1",2)
grandchild1.add_child(greatgrandchild1)
grandpa.print_family()
