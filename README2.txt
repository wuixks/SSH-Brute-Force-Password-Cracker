CPSC 42700 Project 2: Python SSH Brute-force Login
Michael Wallin
March 1st, 2025

NAME
	./sshbrute.py
	
USAGE
	./sshbrute.py <-f filename|-g> <host> <username>
	
DESCRIPTION
	This is a simple password cracker designed to break 3 letter passwords or use a filename with preset passwords on it to crack it. This brute force password cracker is specifically designed to break into a Debian 6 machine that is configured with very weak security settings. 

	
COMMAND-LINE OPTIONS
	<-f filename>
		This is indicating that you are using file mode and asking you to input a file like passwords.txt
	<-g>
		This is indicating that you want to use the script for the generated 3 letter passwords
	<host>
		This is the target computer to ssh into, for my example I am targeting the 191.168.1.191 computer
	<username>
		This is the username of the target computer, in my example I have to use 1 of the 5 given names to target 
		(usera,userb, userc, userd, usere). 
   

INPUT FILE FORMAT
	./sshbrute.py <-f filename> <host> <username>
	example: ./sshbrute.py -f passwords.txt 192.168.1.191 usera

	./sshbrute.py <-g> <host> <username>
	example: ./sshbrute.py -g 192.168.1.191 usera

	
KNOWN BUGS AND LIMITATIONS
	Does not crack complex passwords, the generated python program is designed to crack 3 letter passwords only. 
	Does not crack any number passwords like 0-9 or any punctuation marks and special characters "!@#$%^&*()" 
	If you want to crack different passwords that arent 3 letters long you have to use a filename with a list of passwords.

	
ADDITIONAL NOTES
	Does not work with NAT NatNetwork, I used Bridged Network instead to connect the VMs. Thats why my IP is 192.168.1.x not 10.0.2.x 
	Might be a Virtualbox problem?
	
	user : password : how I got it
	
	usera : abc123    : password file
	userb : baseball  : password file
	userc : adf       : generating 3 letter passwords
	userd : letmein   : password file
	usere : cxv       : generating 3 letter passwords
	
