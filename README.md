
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
keep ```.env``` file in root directory of project
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

### Step 6: Run Migrations  
Run the following command to apply the migrations:

```bash
docker exec -it e2m_practical_interview-web-1 bash
```

This will open a bash shell inside the web container. Run the following commands to apply the migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Open the Upload File Page  
- Once the application is running, open your web browser and navigate to the `/upload_file/` endpoint.


- This will open a basic HTML page that allows you to upload a file and enter your email address for notifications.

### Step 7: Open the Upload via URL Page  
- Once the application is running, open your web browser and navigate to the `/upload_url/` endpoint.


- This will open a basic HTML page that allows you to upload a url and enter your email address for notifications.

### here are some of link you can use to test the application

- [Google Docs Public URL] https://docs.google.com/document/d/1nDdhZ2dLEflbg9x_xwqm2BrThuSAEAqnq8r0qVwU0-A/edit?usp=sharing
- [Google Drive Public URL] https://drive.google.com/file/d/1zlll8cRMoxmsHN9HVxI7Es4ZbLBrfyHn/view?usp=sharing
- [S3 Public URL .docx] https://yhyl.s3.amazonaws.com/users/623/mydocuments/doc.docx
- [S3 Public URL .pdf] https://yhyl.s3.amazonaws.com/users/623/mydocuments/pdf.pdf