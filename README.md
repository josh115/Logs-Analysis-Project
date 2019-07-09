## Description

This project was to create a reporting tool that would return information for 3 given questions. I did this by using python along with the module psycopg2 to be able to connect to database. Then I used postgreSQL queries to get the information wanted from the database which then can be displayed on the console as plaintext.

The 3 questions were: 
1. What are the most popular three articles of all time?
	* This was done by counting each time the log showed access to an article then show 3 articles with the highest views.
2. Who are the most popular article authors of all time?
	* This was done by counting each time the log showed access to an article written by the author then ordering it by highest to lowest.
3. On which days did more than 1% of requests lead to errors?
	* This was done by counting the number of status codes and the number of status codes starting with a 4 then dividing them and multiplying by a hundred to get a percentage then displaying ones which it was higher than 1.

## Instructions

1. Download and install the following:

    [Python 3.7.3](https://www.python.org/downloads/release/python-373/)
	
    [VirtualBox 6.0.8](https://www.virtualbox.org/wiki/Downloads)
	
    [Vagrant 2.2.5](https://www.vagrantup.com/downloads.html)

2. Once you have installed the above download or use git clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) into your chosen directory so that python and postgreSQL will be automatically be installed when your vagrant server is ran.

3. Navigate to the fullstack-nanodegree-vm directory then run ```vagrant up``` in the terminal to start the virtual machine. Once it has started use ```vagrant ssh``` to log into the virtual machine. 

4. Download [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and place inside the vagrant directory.

5. Download the LogAnalysis.py file from this repository and place inside the vagrant directory.

6. Now go back onto your terminal and change directory to the vagrant directory by using ```cd /vagrant``` and then run the command ```psql -d news -f newsdata.sql``` to load the tables and data into the news database.

7. Now in the terminal run ```python LogAnalysis.py``` to run the python script and it should display the questions and answers.
