import sys
import os
from sys import argv 

if __name__ == "__main__":
    print ("Please tell something about you")
    you = input('Who are you? : ')
    which_diff = input('Which Defferance you and me? : ')  
    me = str(sys.argv[2])  # pass parameter from command
    
    allstr = "%s & %s , The Differnace is %s" % (you,which_diff,me)
    print(allstr)
    
