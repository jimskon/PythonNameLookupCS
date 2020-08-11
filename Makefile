#MakeFile to build and deploy the Sample US CENSUS Name Data using ajax
# For SCMP318 Software Development

all: PutCGI PutHTML

PutCGI:
	chmod 757 namelookup.py
	cp nameclient.py /usr/lib/cgi-bin/nameclientCS.py

	echo "Current contents of your cgi-bin directory: "
	ls -l /usr/lib/cgi-bin/

PutHTML:
	cp namelookupCS.html /var/www/html/softdev/pNameserver/
	cp namelookupCS.css /var/www/html/softdev/pNameserver/
	cp namelookupCS.js /var/www/html/softdev/pNameserver/

	echo "Current contents of your HTML directory: "
	ls -l /var/www/html/softdev/pNameserver/
