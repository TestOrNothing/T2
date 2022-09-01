from ast import *
import os
from rewriter.rewriter import *
from rewriter.plusPlus import *
from rewriter.if_else_rewriter import *

path = "input-code/transform/"
dir_list = os.listdir(path)

print("Transforming files in '", path, "' :")


for file in dir_list:
    print(" ==== " + file + " ==== ")
    fileContent = open(path+file).read()
    tree = parse(fileContent)
    # we apply all rewriters in the file
    for commandClass in RewriterCommand.__subclasses__():
        command = commandClass()
        tree = command.apply(tree)
    # export in a new file
    f = open("transformed-code/"+file, "w")
    f.write(unparse(tree))
    f.close()
