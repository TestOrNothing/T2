from ast import *
import os
from rules.rule import *
from rules.suspiciousVariableName import *
from rules.neverReadedVariable import *
from rules.dataClass import *

path = "input-code/analyze/"
dir_list = os.listdir(path)

print("Analyzing files in '", path, "' :")


for file in dir_list:
    print(" ==== " + file + " ==== ")
    fileContent = open(path+file).read()
    tree = parse(fileContent)
    warnings = []
    for ruleClass in Rule.__subclasses__():
        newRule = ruleClass()
        result = newRule.analyze(tree)
        warnings.extend(result)
    for warning in warnings:
        warning.wprint()
