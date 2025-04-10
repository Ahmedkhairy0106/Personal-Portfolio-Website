# Personal Portfolio Website

A dynamic and responsive portfolio website built to showcase my projects, skills, and achievements as a software engineer. This project demonstrates my expertise in backend development with **Django** and database management with **PostgreSQL**, combined with a clean front-end interface using **HTML**, **CSS**, and **JavaScript**.

## Features
- **Dynamic Content**: Displays project details and personal information fetched from a PostgreSQL database.
- **Responsive Design**: Adapts seamlessly to different screen sizes using custom CSS.
- **Interactive Elements**: Includes basic JavaScript for enhanced user experience.
- **Backend Management**: Powered by Django with templates and views for rendering content.
- **Database Integration**: Utilizes PostgreSQL to store and manage portfolio data.

## Technologies Used
- **Backend**: Django, Python
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript
- **Tools**: Git, GitHub, VS Code

## Prerequisites
Before running the project, ensure you have the following installed:
- Python 3.8+
- PostgreSQL
- Git

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Ahmedkhairy0106/Personal-Portfolio-Website.git
   cd Personal-Portfolio-Website
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows:
   venv\Scripts\activate
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure PostgreSQL**:
	•	Create a PostgreSQL database:
   ```bash
   psql -U postgres
   CREATE DATABASE portfolio_db;
   ```
   
	•	Update the DATABASES setting in settings.py with your PostgreSQL 

	4.	Apply Migrations:
python manage.py makemigrations
python manage.py migrate

	5.	Run the Server:
python manage.py runserver

	•	Open your browser and go to http://127.0.0.1:8000/ to view the website.

## Usage

•	Add your projects and personal details via the Django admin panel:
•	Create a superuser:
python manage.py createsuperuser

- Access the admin panel at http://127.0.0.1:8000/admin.

## Contributing

Feel free to fork this repository, submit issues, or send pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
