# Calcule_distance_with_Points
In the next code using Flask and Python I calculate the distance between from the Moscow Ring Road and a specific addres. The addrees is passed to the aplication in an HTTP request, if the specified address is located inside the MKAD, the distance does not to be calcule. And the result is add in .log file. 
To calculate the distance between to points I use geopy.

## Instructions
### Step 1:
Check that you have "Anaconda Prompt" installed on your computer.
### Step 2:
If so, open the program and enter the project directory by means of commands as follows:
C: \ calculate_distance - copy \
### Step 3: 
Create a virtual_envritment with the version 3.7.4 of Python.
## Step 4:
After you create the virtual_envirtment, install the necesary packages to run the application; with the next command:
pip install -r requirements.txt
### Step 5: 
To run the app.py file you need to be in the directory that the file to turn on the Flask server:
C:\calculate_distance\home
python app.py
### Step 6:
When executing the code, it will show you a legend where it will indicate the direction you can execute the code.
### Step 7:
Go to the following address from a web browser:
* http: //127.0.0.1: 5000 / *
### Step 8: 
You will see a form where it will ask you to enter the address.
![formulario](https://user-images.githubusercontent.com/59720195/130651787-1eb1449f-a986-4fd3-813c-cd4c6a4a1ffd.png)
### Step 9: 
Click on the send button, you wait for it to finish loading the page.
### Step 10: 
When finished loading, it will send you to another page showing a message on the screen. Depending on the address entered, it will show the message "Outside the Area Distance (km): ..." or "Inside of the Area".
![resultado](https://user-images.githubusercontent.com/59720195/130651909-5b919822-41b3-4a8a-afbe-97e2b0d7cefd.png)
### Step 11: 
This result will be saved in the file ".log"
![resultado_log](https://user-images.githubusercontent.com/59720195/130651942-3422df3c-02f8-40f3-8f0e-6696e8652a42.png)
