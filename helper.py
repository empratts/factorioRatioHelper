recipeData = {
          "Wire":                       {"Time":.5,    "Ratio": {"Copper":1}, "Yield": 2,},
          "Prod 3":                     {"Time":60,    "Ratio": {"Prod 2":5, "Blue":5, "Red":5}, "MaxProd": 0,},
          "Prod 2":                     {"Time":30,    "Ratio": {"Prod 1":4, "Blue":5, "Red":5}, "MaxProd": 0,},
          "Prod 1":                     {"Time":15,    "Ratio": {"Green":5, "Red":5}, "MaxProd": 0,},
          "Speed 3":                    {"Time":60,    "Ratio": {"Speed 2":5, "Blue":5, "Red":5}, "MaxProd": 0,},
          "Speed 2":                    {"Time":30,    "Ratio": {"Speed 1":4, "Blue":5, "Red":5}, "MaxProd": 0,},
          "Speed 1":                    {"Time":15,    "Ratio": {"Green":5, "Red":5}, "MaxProd": 0,},
          "Blue":                       {"Time":10,    "Ratio": {"Acid":5, "Green":20, "Red":2},},
          "Red":                        {"Time":6,     "Ratio": {"Wire":4, "Green":2, "Plastic":2},},
          "Green":                      {"Time":.5,    "Ratio": {"Wire":3, "Iron":1},},
          "Rocket Part":                {"Time":3,     "Ratio": {"LDS":10, "Rocket Fuel":10, "RCU":10},},
          "LDS":                        {"Time":20,    "Ratio": {"Copper":20, "Plastic":5, "Steel":2},},
          "Rocket Fuel":                {"Time":30,    "Ratio": {"Solid Fuel":10, "Light":10},},
          "RCU":                        {"Time":30,    "Ratio": {"Blue":1, "Speed 1":1},},
          "Satellite":                  {"Time":5,     "Ratio": {"Accumulator":100, "LDS":100, "Blue":100, "Radar":5,"Rocket Fuel":50, "Solar":100 },},
          "Solid Fuel":                 {"Time":2,     "Ratio": {"Light":10}, "MaxProd": 3,},
          "Solar":                      {"Time":10,    "Ratio": {"Copper":5, "Green":15, "Steel":5},},
          "Accumulator":                {"Time":10,    "Ratio": {"Battery":5, "Iron":2},},
          "Radar":                      {"Time":.5,    "Ratio": {"Green":5, "Gear":5, "Iron":10},},
          "Battery":                    {"Time":4,     "Ratio": {"Copper":1, "Iron":1, "Acid":20}, "MaxProd":3},
          "Gear":                       {"Time":.5,    "Ratio": {"Iron":2},},
          "Input":                      {"Time":0,     "Ratio": {},},
          "Space Science":              {"Time":0,     "Ratio": {"Rocket Part":100, "Satellite":1,}, "MaxProd": 0, "Yield":1000},
          "Utility Science":            {"Time":21,    "Ratio": {"LDS":3, "Flying Robot Frame":1, "Blue":2},"Yield":3},
          "Flying Robot Frame":         {"Time":20,    "Ratio": {"Battery":2, "Electric Engine Unit":1, "Steel":1, "Green":3},},
          "Electric Engine Unit":       {"Time":10,    "Ratio": {"Green":2, "Engine Unit":1, "Lubricant":15},},
          "Engine Unit":                {"Time":10,    "Ratio": {"Gear":1, "Pipe":2, "Steel":1},},
          "Pipe":                       {"Time":.5,    "Ratio": {"Iron":1,},},
          "Production Science":         {"Time":21,    "Ratio": {"Electric Furnace":1, "Prod 1":1, "Rail":30}, "Yield":3},
          "Electric Furnace":           {"Time":5,     "Ratio": {"Red":5, "Steel":10, "Stone Brick":10}, "MaxProd": 0,},
          "Rail":                       {"Time":.5,    "Ratio": {"Iron Stick":1, "Steel":1, "Stone":1}, "MaxProd": 0, "Yield":2,},
          "Iron Stick":                 {"Time":.5,    "Ratio": {"Iron":1,}, "Yield":2,},
          "Chemical Science":           {"Time":24,    "Ratio": {"Red":3, "Engine Unit":1, "Sulfur":20},"Yield": 2},
          "Military Science":           {"Time":10,    "Ratio": {"Grenade":1, "Piercing Rounds Magazine":1, "Wall":2},"Yield":2},
          "Grenade":                    {"Time":8,     "Ratio": {"Coal":10, "Iron":5,}, "MaxProd": 0},
          "Piercing Rounds Magazine":   {"Time":3,     "Ratio": {"Copper":5, "Firearm Magazine":1, "Steel":1}, "MaxProd": 0},
          "Wall":                       {"Time":.5,    "Ratio": {"Stone Brick":5,}, "MaxProd": 0},
          "Firearm Magazine":           {"Time":1,     "Ratio": {"Iron":4,}, "MaxProd": 0},
          "Logistic Science":           {"Time":6,     "Ratio": {"Inserter":1, "Transport Belt":1,},},
          "Inserter":                   {"Time":.5,    "Ratio": {"Green":1, "Gear":1, "Iron":1}, "MaxProd": 0},
          "Transport Belt":             {"Time":.5,    "Ratio": {"Gear":1, "Iron":1,}, "MaxProd": 0, "Yield": 2},
          "Automation Science":         {"Time":5,     "Ratio": {"Copper":1, "Gear":1,},},
          "Infinite Research":          {"Time":60,    "Ratio": {"Space Science":1, "Utility Science":1, "Production Science":1, "Chemical Science":1, "Military Science":1, "Logistic Science":1, "Automation Science":1, }, "MaxProd": 0},
          }

rawResourseValues = {"Iron":1,"Copper":1,"Stone":1,"Coal":1,"Light":1,"Iron":1,"Iron":1,"Iron":1,"Iron":1,}

productivityModuleRates = [0,.04,.06,.10]
fullProdModules = [3,3,3,3]

class Node:
    def __init__(self, name:str, productivity=[]):
        self.name = name
        self.totalCrafts = 0
        self.distance = -1
        self.totalSpeedRequired = 0
        self.output = {}
        self.ratio = recipeData[name]["Ratio"]
        self.recipeYeild = recipeData[name].get("Yield", 1)

        maxProd = min(recipeData[name].get("MaxProd",4), len(productivity))
        self.productivity = 1.0

        for i in range(maxProd):
            self.productivity += productivityModuleRates[productivity[i]]

        self.productivity = round(self.productivity,2)

        self.input = {}
        for inputName in self.ratio:
            self.input[inputName] = 0
        self.totalOutput = 0

    def __str__(self):
        #s = '{:s} -- Total Output {:.2f}; Output {:s} , from {:.2f}'.format(self.name, self.totalOutput, str(self.output), self.totalCrafts)
        #return s
        return self.name + " -- Total Output: " + str(self.totalOutput) + " Output: " + str(self.output) + ", from " + str(self.totalCrafts) + " crafts (" +str(self.productivity) + " prod, " + str(self.totalSpeedRequired) + " speed) using Input: " + str(self.input) + " at a distance of: " + str(self.distance)

class Tree:
    def __init__(self, timeMetric:float):
        self.nodes = {}
        self.time = timeMetric

    def addResult(self, name:str, count:int, productivity=[]):
        if name not in self.nodes:
            newNode = Node(name, productivity)
            #first check if there are existing nodes that depend on our output
            dependantOutputsExists = False
            for _ , node in self.nodes.items():
                if name in node.input:
                    newNode.output[node.name] = 0
                    dependantOutputsExists = True
            
            if dependantOutputsExists:
                for inName in newNode.input:
                    if inName in self.nodes:
                        self.nodes[inName].output[name] = 0

            #then add our result output
            newNode.output["Result"] = count
            self.nodes[name] = newNode
    
    def addNode(self, name:str, productivity=[]):
        dependantOutputsExists = False
        if name not in self.nodes:
            newNode = Node(name, productivity)
            for _ , node in self.nodes.items():
                if name in node.input:
                    newNode.output[node.name] = 0
                    dependantOutputsExists = True
            
            if dependantOutputsExists:
                for inName in newNode.input:
                    if inName in self.nodes:
                        self.nodes[inName].output[name] = 0
            #changed this to add the node even if no dependant outputs exist yet to allow adding of nodes any any order. This means that if nodes are added that
            #dont interact with the other nodes, they may never end up linked and should have -1 distance at the end with 0 output and 0 input
            self.nodes[name] = newNode
            
        return dependantOutputsExists

    def addRemainingDependencies(self, productivity=[]):

        while(self.addMissingDependency(productivity)):
            pass

    def addMissingDependency(self, productivity=[]):
        for node in self.nodes.values():
            for inputName in node.input:
                if inputName not in self.nodes and inputName in recipeData:
                    self.addNode(inputName, productivity)
                    return True
        return False

    def calcDistance(self, name:str):
        if name is "Result":
            return -1

        if self.nodes[name].distance >= 0:
            return self.nodes[name].distance
        
        currentDistance = -1
        for subNode in self.nodes[name].output:
            subNodeDistance = self.calcDistance(subNode)
            if subNodeDistance > currentDistance:
                currentDistance = subNodeDistance
        
        self.nodes[name].distance = currentDistance + 1
        return self.nodes[name].distance

    def calcOutputValues(self):
        ##in order of distance, get the values of the outputs from the other nodes and calculate the requred inputs to meet those values

        currentDistance = 0
        itemsFoundOnCurrentStep = True

        while(itemsFoundOnCurrentStep):
            itemsFoundOnCurrentStep = False
            for node in self.nodes.values():
                #for each node at the current distance:
                if node.distance == currentDistance:
                    itemsFoundOnCurrentStep = True
                    #gather the outputs:
                    for outputName in node.output:
                        if outputName is not "Result":
                            node.output[outputName] = self.nodes[outputName].input[node.name]
                        node.totalOutput += node.output[outputName]
                    #calculate the nodes inputs based on the total output needed
                    node.totalCrafts = (node.totalOutput / node.recipeYeild) / node.productivity
                    for inputName in node.input:
                        node.input[inputName] = node.totalCrafts * node.ratio[inputName]

                    node.totalSpeedRequired = round((node.totalCrafts / self.time) * recipeData[node.name]["Time"], 2)
            currentDistance += 1
    
    def collectInputs(self):
        inputNode = Node("Input", [])
        for _, node in self.nodes.items():
            for inputName in node.input:
                if inputName not in self.nodes:
                    currentValue = inputNode.output.get(inputName, 0)
                    inputNode.output[inputName] = currentValue + node.input[inputName]
        self.nodes["Input"] = inputNode


    def compute(self):
        for node in self.nodes:
            self.calcDistance(node)
        self.calcOutputValues()
        self.collectInputs()

        for node in self.nodes.values():
            for inputName in node.input:
                node.input[inputName] = round(node.input[inputName], 2)

            for outputName in node.output:
                node.output[outputName] = round(node.output[outputName], 2)

            node.totalCrafts = round(node.totalCrafts,2)
            node.totalOutput = round(node.totalOutput, 2)

    def display(self):
        for node in self.nodes.values():
            print(node)
            print("")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

def main():

    science = Tree(60)
    science.addResult("Infinite Research", 100)
    science.addRemainingDependencies(fullProdModules)
    science.compute()
    science.display()

    module = Tree(60)
    module.addResult("Prod 3",1)
    module.addRemainingDependencies(fullProdModules)
    module.compute()
    module.display()

main()
