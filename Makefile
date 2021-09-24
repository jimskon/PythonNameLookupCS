#MakeFile to build and deploy the Sample US CENSUS Name Data using ajax
# For SCMP318 Software Development
user= skon
all: PutCGI PutHTML

PutCGI:
	cp nameclient.py /usr/lib/cgi-bin/$(user)_nameclient.py
	chmod 757 /usr/lib/cgi-bin/$(user)_nameclient.py

	find /usr/lib/cgi-bin/ -type f -mmin -5 -ls

PutHTML:
	cp namelookupCS.html /var/www/html/class/softdev/$(user)/pNameserver/
	cp namelookupCS.css /var/www/html/class/softdev/$(user)/pNameserver/
	cp namelookupCS.js /var/www/html/class/softdev/$(user)/pNameserver/

	echo "Current contents of your HTML directory: "
	ls -l /var/www/html/class/softdev/$(user)/pNameserver/
