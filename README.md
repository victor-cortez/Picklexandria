# Picklexandria
A simple Python module to store in disk large amounts of data using small amounts of RAM.

# Usage:

The module will create a folder in the current directory, in this folder it will add all the parts of your data. The module allows for reduced usage of RAM because once a part is dumped in disk it can be discarded in the RAM, therefore, by dividing the data storage in parts, storing the entire data in RAM is not necessary, only one part at a given time. To read, the module will open only one data part per turn and it will keep yielding the itens inside while automatically discarding the used data parts from RAM and loading the next one.

Functions:
addpart(list_of_itens,folder_name) 

Receives two arguments, list_of_itens is a list containing the part to be stored and folder_name is a string representing the name of the folder which contains the data, the module will automatically detect the index of the new part and append to the folder accordingly.

loadall(folder_name)

Receives onew argument, folder_name is a string representing the name of the folder containing the data to be retrieved. The functions returns an generator that yields item by item in the data, without storing the entire data in RAM (only each part at once).
