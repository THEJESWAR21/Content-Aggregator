
# Content Aggregator

A Django-based RSS Content Aggregator that collects articles from multiple RSS feeds, stores them in a database, and displays them through a web interface.

The goal of this project is to provide a single place to consume content from multiple sources without needing to visit each website individually.

---

## Tech Stack

### Backend
- Python
- Django
- SQLite

### RSS Processing
- Feedparser

### Frontend
- HTML
- CSS
- Django Templates

---

## Database Design

### Source

Stores information about the RSS source.

| Field | Description |
|---------|-------------|
| site_name | Name of the website |
| site_link | Website URL |

Example:

```text
TechCrunch
https://techcrunch.com
```

### Authors

Stores author information and associates authors with a source.

| Field | Description |
|---------|-------------|
| source | RSS Source |
| name | Author name |

### Articles

Stores article metadata.

| Field | Description |
|---------|-------------|
| title | Article title |
| link | Article URL |
| description | Article summary |
| published_at | Publication date |
| all_tags | Comma-separated tags |
| source | Article source |
| author | Article author |

---

## Running the Application

Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create an admin user:

```bash
python manage.py createsuperuser
```

Run the development server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000
```



## Example Data Flow

```text
RSS Feed
    │
    ▼
Feedparser
    │
    ▼
Source
    │
    ├── Authors
    │
    └── Articles
    │
    ▼
Django Database
    │
    ▼
Web Interface
```

---
