# Log-Analysis

This project was assigned as the final project from the Back-End path of
Udacity's Intro to Programming Nanodegree.

This program is meant to answer 3 questions in a report format pulling data
from the _'news' database_.

Here are the 3 questions the program's output is looking to answer:
<ol>
  <li>What are the most popular three articles of all time?</li>
  <li>Who are the most popular article authors of all time?</li>
  <li>On which days did more than 1% of requests lead to errors?</li>
</ol>
  
## Set-up

There are a few programs that you will need to install and set-up before
we can run this program. There is a section with instructions for each.
Follow along to be able to run this program as intended.

#### Terminal

If you are using a <strong>Mac or Linux based system</strong> you can move
ahead. If you are used a <strong>Windows based system</strong> please following
the instructions in this section.

<ul>
  <li>Download <strong>Git Bash</strong> from <a href="https://git-scm.com/downloads">here</a></li>
  <li>Once downloaded run the installer</li>
  <li>Now Git Bash is ready to be used!</li>
</ul>


#### Installing Vagrant

<ul>
    <li>Vagrant will be used to configure our virtual machine and a download
    link is provided <a href="https://www.vagrantup.com/downloads.html">here</a>
    The version of Vagrant this program is intended to run with is 2.1.4</li>
    <li>Download from the website the copy of Vagrant that is compatible with
    your system</li>
    <li>Once downloaded, run the installer and follow the instructions
    provided by the installer</li>
    <li>Now Vagrant is ready to be used!</li>
</ul>

#### Installing VirtualBox

<ul>
    <li>VirtualBox will be used to hold our virtual machine and a download link
    is provided <a href="https://www.virtualbox.org/wiki/Downloads">here</a>
    </li>
    <li>Download from the website the copy of VirtualBox that is compatible
    with your system</li>
    <li>Once downloaded, run the installer and follow the instructions
    provided by the installer</li>
    <li>Now VirtualBox is ready to be used!</li>
</ul>

#### VM Configuration

<ul>
    <li>The configuration file for our virtual machine can be downloaded <a href="https://bit.ly/2PVvjuS">here</a></li>
    <li>Once the zip file is downloaded navigate to your downloads folder</li>
    <li>Extract the contents of the zip file into the same folder</li>
    <li>In Git Bash you will have to navigate to this directory</li>
      <ul>
          <li> If the command line in the users folder use the following
          commands to get to the folder containing the configuration `cd Downloads/FSND-VIRTUAL-MACHINE` then `cd vagrant/`
          <li>Then we will run the command `vagrant up` to start the set-up
          of your virtual machine</li>
          <li>Once `vagrant up` is complete run `vagrant ssh` to gain access
          to your VM</li>
      </ul>
    <li>Now your Virtual Machine is ready to be used!</li>
</ul>

#### Getting The Data

<ul>
    <li>Data for the project can be found <a href="https://bit.ly/2y4PPQy">here</a></li>
    <li>Once the zip file is downloaded navigate to your downloads folder</li>
    <li>Extract the contents of the zip file into the same folder</li>
    <li>Take the extracted folder and place it into your
    FSND-VIRTUAL-MACHINE folder</li>
      <ul>
        <li>Having this folder in the same folder as Vagrant will allow for
        Vagrant to access the files in the folder to run the program</li>
      </ul>
    <li>Now the data used in this program is ready to be used!</li>
</ul>

## Directions To Run The Program

<ul>
    <li>Have your virtual machine configured based on the configuration
    provided above and download the data provided</li>
    <li>Make sure your data is in the same folder are your Vagrantfile</li>
    <li>Launch your virtual machine by navigating to the folder the Vagrant
    file is located, once there type `vagrant up` this will start up your
    virtual machine</li>
    <li>After your virtual machine is started login using the following command `vagrant ssh`</li>
    <li>Then you will be prompted to change directories to access shared files
    with vagrant by entering the command `cd /vagrant`</li>
    <li>Then you will change directories to access the python file to run
    the program `cd newsdata`</li>
    <li>You will then run the following command to access the data base
    `psql -d news`</li>
    <li>Open another instance of Git Bash and navigate to the folder
    where your Vagrantfile is located
    (/Downloads/FSND-Virtual-Machine/vagrant)</li>
    <li>Then run the command `vagrant ssh` to gain access to your VM</li>
    <li>Then you will be prompted to change directories to access shared files
    with vagrant by entering the command `cd /vagrant`</li>
    <li>Then you will change directories to access the python file to run
    the program `cd newsdata`</li>
    <li>Once you are in the correct directory run the file with the following
    command `python  newsdatadb.py`</li>
</ul>

## Design

The program was designed to combine PostgreSQL & Python to create a report.
The program will import module psycopg2 into Python and use the
_'news' database_ provided in the data above. Once we have our database the
program will run 3 seperate queries to gather the outputs for the questions
needed to fill the report. After the outputs are gathered, they will be
formatted to allow for greater readability to the user. File newsdatadb.py was written to be used with Python 2 for any development activity you may use it
for. There have been no views created for this version of the project.

### Credit for this project's instructions  
*Goes to [Udacity](https://www.udacity.com/) in their Intro to Programming Nanodegree track*
