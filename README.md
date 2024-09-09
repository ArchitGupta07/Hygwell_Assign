To build docker image
docker build -t fastapi-docker .

to build docker container
docker run -d --name fastapi-docker-container -p 80:80 fastapi-

# Store Monitoring FastAPI Project

This project is a FastAPI-based web application that give you access to three APIs for content extraction and find you relevant content to your chat query.

## Features

- Provides content extraction from urls.
- Provides text extraction from pdfs.
- Finds relevant content to an input query

## Project Structure

The project consists of the following main components:

- `main.py`: FastAPI application entry point
- `models.py`: SQLAlchemy ORM models
- `db.py`: Database connection setup

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/Hygwell_Assign.git
   cd Hygwell_Assign
   ```

2. Create a virtual environment and activate it:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

Ensure you have set up your database connection string in `.env` file as DATBASE_URL. The project uses SQLAlchemy, so you can configure it to work with various database backends.

## Usage

1. Start the FastAPI server:

   ```
   uvicorn main:app --reload
   ```

2. Access the API at `http://localhost:8000`

## API Endpoints

### POST /url

Extract data from a URL and store it in a Database.

**Response:**

```json
{
  "chat_id": "uuid-of-the-url",
  "message": "url page content"
}
```

### POST /pdf

Extracts data from a uploaded pdf file and store it in database.

**Response:**

```json
{
  "chat_id": "uuid-of-the-pdf",
  "message": "pdf text content"
}
```

### POST /chat

Find relevant content to the input query using TF-IDF and cosine similary from uploaded url and pdf content.

**Response:**

````json
{
  "message": "most relevant pdf/url content"
}

// ## Data Models

// - `Store`: Represents a store with its timezone information
// - `StoreStatus`: Represents the status of a store at a given timestamp
// - `BusinessHours`: Represents the business hours of a store
// - `Report`: Represents a generated report

// ## Report Generation Process

// The report generation process is handled by the `generate_report` function in `utils.py`. It performs the following steps:

// 1. Fetches all necessary data from the database
// 2. Converts data to pandas DataFrames for efficient processing
// 3. Merges and processes the data to calculate uptime and downtime
// 4. Filters data based on business hours
// 5. Calculates metrics for different time ranges (last hour, day, and week)
// 6. Saves the report as a CSV file

// ## Error Handling

// The application includes basic error handling:

// - 404 errors for reports not found
// - Exception handling for timezone conversion issues
// ```
````
