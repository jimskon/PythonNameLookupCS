#MakeFile to build and deploy the Sample US CENSUS Name Data using ajax
# For CSC3004 Software Development

# Put your user name below:
USER= skon

all: PutCGI PutHTML

PutCGI:
	chmod 757 namelookup.py
	cp nameclient.py /usr/lib/cgi-bin/$(USER)_nameclient.py

	echo "Current contents of your cgi-bin directory: "
	ls -l /usr/lib/cgi-bin/

PutHTML:
	cp namelookupCS.html /var/www/html/class/softdev/$(USER)/python/
	cp namelookupCS.css /var/www/html/class/softdev/$(USER)/python/
	cp namelookupCS.js /var/www/html/class/softdev/$(USER)/python/

	echo "Current contents of your HTML directory: "
	ls -l /var/www/html/class/softdev/$(USER)/python/
