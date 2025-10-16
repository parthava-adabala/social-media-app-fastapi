# Social Media API built with FastAPI

A full-featured REST API built with FastAPI, featuring user authentication, posts management, and voting system with PostgreSQL database integration.

## Features

- **User Management**: Registration, login, and authentication with JWT tokens
- **Posts System**: Create, read, update, and delete posts
- **Voting System**: Users can vote on posts (like/dislike)
- **Database Integration**: PostgreSQL with SQLAlchemy ORM
- **Authentication**: JWT-based authentication with bcrypt password hashing
- **API Documentation**: Auto-generated interactive docs with Swagger UI
- **Testing**: Comprehensive test suite with pytest
- **Docker Support**: Containerized development and production environments

## Prerequisites

- Python 3.12+
- Docker and Docker Compose
- Git

## Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd fastapi
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
Create a `.env` file in the root directory:
```bash
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_PASSWORD=password123
DATABASE_NAME=fastapi
DATABASE_USERNAME=postgres
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Start Database with Docker
```bash
docker-compose -f docker-compose-dev.yaml up -d postgres
```

### 6. Run Database Migrations
```bash
alembic upgrade head
```

### 7. Start the Application
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Docker Setup

### Development Environment
```bash
# Start all services
docker-compose -f docker-compose-dev.yaml up -d

# View logs
docker-compose -f docker-compose-dev.yaml logs -f

# Stop services
docker-compose -f docker-compose-dev.yaml down
```

## Testing

### Run All Tests
```bash
pytest -v
```

### Run Specific Test Categories
```bash
# User tests
pytest tests/test_users.py -v
```

## API Documentation

Once the server is running, access the interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Authentication
- `POST /login` - User login
- `POST /users/` - User registration

### Posts
- `GET /posts/` - Get all posts (with pagination and search)
- `GET /posts/{id}` - Get specific post
- `POST /posts/` - Create new post (requires authentication)
- `PUT /posts/{id}` - Update post (requires authentication & ownership)
- `DELETE /posts/{id}` - Delete post (requires authentication & ownership)

### Votes
- `POST /vote` - Vote on a post (requires authentication)

### Users
- `GET /users/me` - Get current user profile (requires authentication)

## Acknowledgments

- Sanjeev Thiyagarajan
