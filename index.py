##############################################################
##  simple python server for static website home network    ##
##############################################################
#              with learning comments                        #



# importing a python module and a class it includes

import http.server
from http.server import SimpleHTTPRequestHandler


#give the server adress a variable so its more practical

serveradress = ("0.0.0.0", 8000)


# next variable i call sleepyserver > becomes object (of server class)
# when it gets the parameters adress and Handlerclass
# Handlerclasseses are also included in the imported module,
# such handy, very wow <333

sleepyserver = http.server.HTTPServer(serveradress, SimpleHTTPRequestHandler)



# now i can make her run till i manually tell her to stop
# as shes an object now there is methods/functions for her.

sleepyserver.serve_forever()



# it can only work as long as all stuff is in same dir its running from
# sleepyserver can deal with Html request> 
# it reads the browser the .html in my directory and the html directs
# browser to the .css, images.etc


#ok thats it, lets try it

