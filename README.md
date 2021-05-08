# BLOOD SEEKER
## Easy Search for Blood Donors


#### PREREQUISITE
- Install [VS CODE](http://https://code.visualstudio.com/download "VS CODE") (Please install the following from the **extensions** tab in VS CODE ):
	- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
	- [Python](http://https://marketplace.visualstudio.com/items?itemName=ms-python.python "Python")
	- [Prettier](http://https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode "Prettier") 
		- For Formatting Purposes.
		- To run Prettier:
			- >Ctrl + Shift + P - > Format Document
		- **Remember: Always run Prettier after editing HTML and CSS files**

- Install [XAMPP 8.0.5 / PHP 8.0.5](http:/https://www.apachefriends.org/download.html/ "XAMPP 8.0.5 / PHP 8.0.5")
- Install [Github Desktop](https://desktop.github.com/ "Github Desktop")
	- Login to your github account.

# CLONE THIS PROJECT
1. Fork this project first:
	- Please see this [Image](https://imgur.com/Fd2omst "Image").
2.  Open Github Desktop and Clone the Repository that you **cloned**:
	> File -> Clone Repository -> URL


# Project Setup
1. Create a new database in **phpMyAdmin**
	- **Database Name:** *dbbloodseeker*

2. Open the project in VS Code(**bloodseeker-django**0
   - Right Click **bloodseeker-django** and click **Open with Code**
   - After opening in VS Code, your file tree will look like this:
```
|-- bloodseeker-django
  |-- bloodseeker
  |-- static
  |-- user
  |-- manage.py
  |-- README.md
```

3. Open VS Code Terminal
	> Ctrl + `

	#### Enter the commands below:
`pip install django`

`pip install mysqlclient`

`python manage.py migrate`

4. Create SuperUser(using the **terminal**):
`python manage.py createsuperuser`

	#### Enter the details below:
>username: admin
>password: admin123456

# Run Project
1. Open **XAMPP Control Panel**
	>Apache -> Start
	>MySQl -> Start

1. Run the project in the **VS Code** terminal:
	 ` python manage.py runserver`

2. Open the project in your web browser:
	>127.0.0.1:8000/user/login
	
	>127.0.0.1:8000/user/register
	
	>127.0.0.1:8000/admin