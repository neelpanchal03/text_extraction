
# Text Extraction Project

This project handles the extraction of text from uploaded document and public URL from google drive and google docs.

## Prerequisites

1. **Git** – Make sure Git is installed on your machine.
2. **Docker** – Ensure Docker is installed and running on your PC.

## Setup Instructions

### Step 1: Clone the Repository  
Open a terminal and run the following command to clone the project:

```bash
git clone https://github.com/neelpanchal03/text_extraction.git
cd text_extraction
```

### Step 2: Build Docker Containers  
Build the Docker containers by running:

```bash
docker compose build
```

### Step 3: Start the Application  
Once the build completes, start the containers:

```bash
docker compose up
```

The project will be accessible at `http://localhost:8000`.

### Step 4: Troubleshooting  


- **Database-related Errors**:  
  If you see errors like **"Database does not exist"** or **"Connection refused"**, it might be because the web container started before the database was ready. In that case:

  1. Stop the containers using `Ctrl + C` in the terminal.
  2. Restart the containers:

     ```bash
     docker compose up
     ```

> **Note**: The containers have been configured with `depends_on` to ensure order, but some machines may still experience timing issues. Restarting usually resolves this.

### Step 5: Dependencies  
All required dependencies will be installed automatically inside the containers during the build process.

### Step 6: Open the Upload Page  
- Once the application is running, open your web browser and navigate to the `/upload_file/` endpoint.


- This will open a basic HTML page that allows you to upload a file and enter your email address for notifications.
