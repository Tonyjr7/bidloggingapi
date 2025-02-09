# Bid Tracking API

## Overview
This API allows users to log, retrieve, and delete job bids. It provides endpoints to record bids, fetch all bids or filter them by company and position, and delete specific bids.

## Installation
1. Clone the repository:
   ```sh
   git clone <repo_url>
   ```
2. Navigate to the project directory:
   ```sh
   cd bidapp
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```sh
   python manage.py migrate
   ```
5. Run the development server:
   ```sh
   python manage.py runserver
   ```

## API Endpoints
### 1. Log a Bid
- **Endpoint:** `/api/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "position": "Software Engineer",
    "company": "Tech Corp",
    "link": "https://example.com/job",
    "resume": "https://example.com/resume.pdf"
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "position": "Software Engineer",
    "company": "Tech Corp",
    "link": "https://example.com/job",
    "resume": "https://example.com/resume.pdf",
    "created_at": "2025-02-09T12:00:00Z"
  }
  ```

### 2. Retrieve Bids
- **Endpoint:** `/api/check/`
- **Method:** `GET`
- **Response:**
  ```json
  [
    {
      "id": 1,
      "position": "Software Engineer",
      "company": "Tech Corp",
      "link": "https://example.com/job",
      "resume": "https://example.com/resume.pdf",
      "created_at": "2025-02-09T12:00:00Z"
    }
  ]
  ```

### 3. Filter Bids by Company and Position
- **Endpoint:** `/api/check/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "position": "Software Engineer",
    "company": "Tech Corp"
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "position": "Software Engineer",
    "company": "Tech Corp",
    "link": "https://example.com/job",
    "resume": "https://example.com/resume.pdf",
    "created_at": "2025-02-09T12:00:00Z"
  }
  ```

### 4. Delete a Bid
- **Endpoint:** `/api/check/<id>/`
- **Method:** `DELETE`
- **Response:**
  ```json
  {
    "message": "Bid deleted successfully"
  }
  ```

## Model Structure
The API uses a `Bid` model with the following fields:
- `position` (CharField): Job position title
- `company` (CharField): Company name
- `link` (URLField): Job posting link
- `resume` (URLField): Resume link
- `created_at` (DateTimeField): Timestamp of bid creation

## License
MIT License
