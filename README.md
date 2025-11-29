# StoriApp

A basic Django application with a beautiful landing page for story sharing and creation.

## Features

- 📖 Create and publish stories
- 📚 Discover content from other writers  
- 👥 Connect with fellow readers and writers
- Modern, responsive landing page design

## Setup Instructions

### Prerequisites
- Python 3.8+ installed on your system

### Installation

1. Clone or navigate to the project directory:
   ```bash
   cd /Users/oliverdaniel/storiapp
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Open your browser and visit: http://127.0.0.1:8000/

## Project Structure

```
storiapp/
├── core/                 # Main Django app
│   ├── templates/        # HTML templates
│   ├── views.py         # View functions
│   └── urls.py          # URL routing
├── storiapp/            # Project settings
│   ├── settings.py      # Django configuration
│   └── urls.py          # Main URL configuration
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
└── venv/               # Virtual environment
```

## Development

To make changes to the landing page, edit:
- `core/templates/core/landing.html` - HTML template and styling
- `core/views.py` - View logic and context data

## Next Steps

This is a basic scaffold. You can extend it by:
- Adding user authentication
- Creating story models and forms
- Adding a proper database (PostgreSQL, MySQL)
- Implementing user profiles
- Adding story creation and editing functionality
- Setting up static file handling for CSS/JS
- Adding more sophisticated styling with CSS frameworks
