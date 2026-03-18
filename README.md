# 🎬 Film Watch Site 🎞️

Welcome to the **Film Watch Site** backend! This is a robust, high-performance Django-based platform designed for movie lovers. It features automated data synchronization with global movie databases, advanced search capabilities, and a fully dockerized infrastructure.

---

## 🚀 Key Features

- **🎞️ Automated Movie Ingestion**: Synchronizes movies, genres, and metadata automatically from **VideoCDN** and **TMDB APIs** using Celery background tasks.
- **🔍 Advanced Search**: Powered by **Elasticsearch** for lightning-fast and relevant movie discovery.
- **👤 User Management**: Custom user accounts with features for "Favorites" and movie "Watch History".
- **💬 Community Interaction**: A built-in comment system where users can share their thoughts (with admin moderation).
- **📦 Fully Dockerized**: Seamless setup for development and production using Docker and Docker Compose.
- **🔄 Task Management**: Efficient background task handling with **Celery** and **RabbitMQ**, monitored via **Flower**.
- **📊 Monitoring & SEO**: Includes **Prometheus** for metrics and automated **Sitemaps** for search engine optimization.
- **☁️ Cloud Ready**: Configured for **AWS S3** file storage and **Nginx** reverse proxying.

---

## 🛠️ Tech Stack

### Backend Core
- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) **Python 3.11**
- ![Django](https://img.shields.io/badge/django-%23092e20.svg?style=for-the-badge&logo=django&logoColor=white) **Django 4.2.1**
- ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white) **PostgreSQL**

### Infrastructure & Services
- ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) **Docker & Docker Compose**
- ![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white) **Redis** (Caching & Celery Backend)
- ![RabbitMQ](https://img.shields.io/badge/RabbitMQ-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white) **RabbitMQ** (Message Broker)
- ![Elasticsearch](https://img.shields.io/badge/elasticsearch-%2303a9f4.svg?style=for-the-badge&logo=elasticsearch&logoColor=white) **Elasticsearch** (Search Engine)
- ![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white) **Nginx** (Reverse Proxy)

### External Integrations
- **TMDB API**: Movie metadata, posters, and translations.
- **VideoCDN API**: Movie stream sources and iframe integration.
- **AWS S3**: Scalable media and static file storage.

---

## 🏗️ Project Structure

The project follows a clean, modular architecture:

```text
├── apps/                 # Django Applications
│   ├── movies/          # Core movie models, views, and documents
│   ├── users/           # User authentication and profiles
│   ├── site_info/       # General site settings and generic pages
│   └── shared/          # Common utilities and Celery tasks
├── compose/              # Docker configuration files
├── root/                 # Project core settings and URL routing
├── static/               # Assets (CSS, JS, Images)
├── templates/            # HTML Templates
├── Makefile              # Automation commands
└── docker-compose.yml    # Infrastructure orchestration
```

---

## ⚙️ Setup & Installation

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)
- (Optional) [Poetry](https://python-poetry.org/) for local development

### 1. Environment Configuration
Create a `.env` file in the root directory and populate it based on your requirements:

```env
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=postgres://user:password@db:5432/film_watch_site

# API Tokens
API_TOKEN_VIDEOCDN=your_videocdn_token
API_TOKEN_TMDB=your_tmdb_token

# AWS S3 (Optional)
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_STORAGE_BUCKET_NAME=your_bucket
```

### 2. Spinning up the infrastructure
Run everything with a single command:

```bash
docker-compose up --build
```

The site will be available at `http://localhost:2022` (via Nginx) or `http://localhost:8000` (Direct Django).

### 3. Database Migrations
Run migrations inside the container:

```bash
docker-compose exec web python manage.py migrate
```

---

## 📋 Useful Commands

Managed via the included `Makefile`:

- `make migrate`: Run all pending database migrations.
- `make del_mig`: **Caution!** Deletes all migration files (useful for clean starts during development).
- `make both`: Refreshes the database state entirely.

---

## 🔍 Monitoring

- **Flower**: Celery task monitoring is available at `http://localhost:5557`.
- **RabbitMQ Admin**: Message broker dashboard at `http://localhost:15672`.
- **Prometheus**: Metrics collection available at `http://localhost:9090` (if configured).

---

## 🤝 Contributing

We welcome contributions!
1. Fork the repo.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

Developed with ❤️ by [Abdurashid Khikmatov](https://github.com/xdido2) 🚀
