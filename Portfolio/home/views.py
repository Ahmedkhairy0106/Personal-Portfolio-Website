from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return render(request, 'home/homePage.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

def projects(request):
    projects = [
        {
            "title": "Cinema Ticket Booking System",
            "description": "This project allows users to easily and quickly book cinema tickets. The system features a simple user interface where users can browse available movies, select a specific showtime, and book tickets.",
        },        
        {
            "title": "Cinema Ticket Booking System",
            "description": "This project allows users to easily and quickly book cinema tickets. The system features a simple user interface where users can browse available movies, select a specific showtime, and book tickets.",
        },
        {
            "title": "Cinema Ticket Booking System",
            "description": "This project allows users to easily and quickly book cinema tickets. The system features a simple user interface where users can browse available movies, select a specific showtime, and book tickets.",
        },
        {
            "title": "Cinema Ticket Booking System",
            "description": "This project allows users to easily and quickly book cinema tickets. The system features a simple user interface where users can browse available movies, select a specific showtime, and book tickets.",
        },
    ]
    return render(request, 'home/projects.html', {"projects": projects} )

def all_projects(request):
    features = [
        {
            "title": "1. Ticket Booking:",
            "description": [
                "• Allows users to easily book tickets for their favorite movies through a user-friendly interface.",
                "• Provides various options for films, including showtimes and available seats."
            ]
        },
        {
            "title": "2. User Registration and Login:",
            "description": [
                "• Users can create personal accounts to store their information, making future bookings easier.",
                "• Offers a secure login system to protect user data."
            ]
        },
        {
            "title": "3. Show Management:",
            "description": [
                "• Administrators can add and update new films and their showtimes, ensuring users have access to the latest information.",
                "• Enables management of available seats and displays them dynamically."
            ]
        },
        {
            "title": "4. Multiple Payment Methods:",
            "description": [
                "• Supports various secure payment methods, making it convenient for users to pay for their tickets online."
            ]
        },
        {
            "title": "5. Booking Confirmations:",
            "description": [
                "• After completing a booking, users receive confirmations via email or text messages, ensuring they are aware of their booking status."
            ]
        },
    ]
    
    return render(request, 'home/all_projects.html', {'features': features})