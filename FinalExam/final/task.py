class Task:
    def __init__(self, name):
        self.name = name
        self.subtasks = []

    def __str__(self):
        def indented(self,depth=0):
            lines = []
            numSpaces = " " * depth
            lines.append(numSpaces + self.name)
            for t in self.subtasks:
                lines.extend(indented(t, depth + 4))
            return lines
        return "\n".join(indented(self)) + "\n"
    def add_subtask(self, subtask):
        self.subtasks.append(subtask)
