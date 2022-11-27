# Network Contacts Parser
Its a simple script which helps you parse telephone numbers with Fist and Last name (If they do exist). 
Collects data into a database (SQLite) and can output in TXT file.
Also you can clear data base.

For example i prepare test HTML page with test numbers for check script.

	Scripts functional
	[1] Parse site
	[2] Output data from data base to TXT file
	[3] Clear database
	[4] Exit from script

How to use parser? 
First of all you need paste your link to HTML page in next string

	r = requests.get("your link")

After that save the file and open command line (cmd, PowerShell, Terminal).

You need install external modules via pip

	pip install sqlite
	pip install requests
	pip install bs3

Go to directory where file is located
Type: python3 parserV2.py

Congratulations! Script is working
