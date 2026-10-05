# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build and Run Commands
- **Run Application**: `python app.py` (Runs on port 5001 by default)
- **Install Dependencies**: `pip install -r requirements.txt`
- **Run Tests**: `pytest`
- **Run Single Test**: `pytest tests/test_file.py` (or specify function `pytest tests/test_file.py::test_function`)

## Architecture and Structure
The project is a Flask-based Expense Tracker application.

- `app.py`: Main application entry point containing routes and Flask configuration.
- `database/`: Database management layer.
    - `db.py`: Intended to house database connection logic (`get_db`), initialization (`init_db`), and seeding (`seed_db`) using SQLite.
- `templates/`: Jinja2 HTML templates for the frontend.
- `static/`: Static assets (CSS/JS).
- `requirements.txt`: Python dependency list.

The application currently consists of landing, registration, and login pages, with several placeholder routes for core functionality (logout, profile, and expense CRUD operations) that are intended to be implemented incrementally.
