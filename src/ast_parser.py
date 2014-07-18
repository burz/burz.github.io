# dot -T jpg ast_parser.dot > ast_parser.jpg

handle = 0

def createNode(label):
    global handle
    variable = "x" + str(handle)
    handle = handle + 1
    return [variable, variable + " [label=\"" + label + "\",shape=circle]\n"]

def createChild(parent, child, options = ""):
    return parent + " -> " + child + options + "\n"

def createWrapper(code):
    return "strict digraph X {\n" + code + "}"

def simpleAST():
    minusNode = createNode("-")
    plusNode = createNode("+")
    oneNode = createNode("1")
    twoNode = createNode("2")
    threeNode = createNode("3")
    string = minusNode[1] + plusNode[1] + oneNode[1]
    string = string + twoNode[1] + threeNode[1]
    string = string + createChild(minusNode[0], oneNode[0])
    string = string + createChild(minusNode[0], twoNode[0])
    string = string + createChild(plusNode[0], minusNode[0])
    string = string + createChild(plusNode[0], threeNode[0])
    return string

def getCode():
    print createWrapper(simpleAST()) 

getCode()

