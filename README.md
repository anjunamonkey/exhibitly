# A/Bite

A/Bite — menu optimisation and A/B testing for restaurants.

## Features

- AI-driven dynamic pricing
- A/B testing for pricing, images, copy and menu order
- Personalised menus via a conversational assistant
- Automated promotions and waste reduction tools
- Dashboard with charts, experiments and recommendations

## Setup Instructions

### Prerequisites
- Python 3.8+ installed on your system

### Installation

1. Clone or navigate to the project directory:
   ```bash
   cd /Users/oliverdaniel/ideas/abite
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
abite/
├── core/                 # Main Django app
│   ├── templates/        # HTML templates (core/ and app/)
│   ├── views.py          # View functions
│   └── urls.py           # URL routing
├── abite/                # Project settings
│   ├── settings.py       # Django configuration
│   └── urls.py           # Main URL configuration
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
└── venv/                 # Virtual environment
```

## Development

To edit the public landing page:
- `core/templates/core/abite.html` — main landing page template
- `core/templates/core/header.html` — site header/navigation
- `core/templates/core/footer.html` — site footer

To edit the dashboard and app pages:
- `core/templates/app/*.html` — application templates (dashboard, tests, etc.)
- `core/views.py` — view logic serving dashboard and app pages

## Notes

- The dashboard entrypoint is available at `/dashboard/` in development.
- Pages inside `core/templates/app/` are intentionally kept minimal and can omit the site footer to provide an app-like experience (see template includes).
- Extend the project by adding auth, story/menu models, integrations with POS systems, and production static file handling.
