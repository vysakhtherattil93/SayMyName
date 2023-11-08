Install git for windows: https://git-scm.com/downloads.(look for latest version)
Open git bash and enter the commands as follows.
check your directory using command "pwd" this should provide you with the current path.
cd to your desired path. example:c/Users/vijay/OneDrive/Desktop/
create a new directory using mkdir <foldername> . example mkdir saymyname
cd into that directory from your gitbash.
run below commands to clone the files into your directory.
git clone https://github.com/vysakhtherattil93/SayMyName.git 
once done check the folder for all the file by opening it from desktop.
now go to command prompt cd into the saymyname folder depending on your IDE open say my name project using it command or you can directly open IDE and open file folder from files. for visual studio code once you in the directoy type code .
once the project is open in your IDE, check for the path to be as same as the current folder path in your terminal, you can open terminal with ctrl+~ and select command prompt or powershell.
run the command to create a virtual environment python3 -m venv venv which create a virtual environment.
run the command to activate your virtual environnment venv\Scripts\activate.bat which will activate your virtual environment.
To install dependencies for back end run the command pip install -r requirements.txt (make sure you activate you virtual environment before doing this step easy way to know if your virtual environment is shows before the directory.)
cd into the backend folder and run the command python main.py which will run the backend.
open another command prompt in your IDE and run the frontend, you should now have a working backend and frontend.

