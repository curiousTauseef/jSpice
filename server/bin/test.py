#!/usr/bin/python
#############################################################
#             /######            /##                        #
#            /##__  ##          |__/                        #
#        /##| ##  \__/  /######  /##  /#######  /######     #
#       |__/|  ######  /##__  ##| ## /##_____/ /##__  ##    #
#        /## \____  ##| ##  \ ##| ##| ##      | ########    #
#       | ## /##  \ ##| ##  | ##| ##| ##      | ##_____/    #
#       | ##|  ######/| #######/| ##|  #######|  #######    #
#       | ## \______/ | ##____/ |__/ \_______/ \_______/    #
#  /##  | ##          | ##                                  #
# |  ######/          | ##                                  #
#  \______/           |__/                                  #
#							    #
#                 Jorge I. Zuluaga (C) 2016		    #
#############################################################
# Function: jSpice kernel
#############################################################

#############################################################
#EXTERNAL MODULES
#############################################################
import sys,os,inspect
PATH=os.path.realpath(
    os.path.abspath(os.path.split(
        inspect.getfile(
            inspect.currentframe()))[0]))
sys.path.insert(0,PATH+"/../bin")
from jspice.core import *

#############################################################
#READ CONFIGURATION FILE
#############################################################
CONF=loadConf(PATH+"/../")

#############################################################
#LOAD SPICE KERNELS
#############################################################
for kernel in glob.glob(PATH+"/../"+CONF["kernels_dir"]+"/*"):
    spy.furnsh(kernel)

#############################################################
#REMOVE AND ADD MODULES
#############################################################
#REMOVE SENSIBLE MODULES
exec("del(%s)"%CONF["sensible_modules"])
#ADD NEW MODULES
for mod in CONF["numerical_modules"]:exec(mod)

#############################################################
#TEST CODE
#############################################################
import sys

print spy.jutcnow()
print spy.jlocnow()
print spy.jetnow()

flog=open("/tmp/a","a")
logEntry(flog,"Log")