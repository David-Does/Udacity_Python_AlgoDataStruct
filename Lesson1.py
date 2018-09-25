class Classy(object):
    def __init__(self):
        self.items = [object]

    def getClassiness(self):
        classiness = 0
        for str in self.items:
            if (str == "tophat"):
                classiness = classiness + 2;
            if (str == "bowtie"):
                classiness = classiness + 4;
            if (str == "monocle"):
                classiness = classiness + 5;
        return classiness;

    def addItem(self,str):
        self.items.append(str)


# Test cases
me = Classy()

# Should be 0
print me.getClassiness()

me.addItem("tophat")
# Should be 2
print me.getClassiness()

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print me.getClassiness()

me.addItem("bowtie")
# Should be 15
print me.getClassiness()