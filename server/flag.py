import sys


args = sys.argv

with open('flag.txt', 'w') as f: # write a flag to flag.txt
    flag = (args[1])
    f.write(flag)
