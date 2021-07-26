*************Steps to run the project**************
1. Open cmd and clone the project using command
  git clone https://github.com/letzzBuild/ElectiveAPI.git 

2. Go inside project folder => to go inside project folder type 
cd ElectiveAPI
3. type pip install -r requirements.txt
4. Start Mysql from xampp and open phpmyadmin and create a new
database with name `elective_recommander`
5. open cmd in the project folder and run following commands.
which will create the required tables in the database.
   1. python manage.py makemigrations
   2. python manage.py migrate
6. Run the project by typing python manage.py runserver.

******** ADMIN URL TO ADD CONFIGURATIONS ********
http://127.0.0.1:8000/admin => open admin panel
http://127.0.0.1:8000 => application runs on this url
