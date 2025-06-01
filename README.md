# RAG AI Model - Datasphere Q&A System

This project is a Retrieval-Augmented Generation (RAG) AI model that fetches data from **Datasphere** and answers user queries based on the retrieved information.

## 🚀 Getting Started

Follow these steps to get the project up and running:

### Step 1: Clone the Repository

```bash
git clone <your-repo-url>
```

### Step 2: Open the cloned folder using Visual Studio Code.

### Step 3: Set Up a Virtual Environment
Open a terminal in VS Code and run:
```
python -m venv venv
```
Note: If Python is not installed, install Python and make sure it is added to your global PATH.

### Step 4: Activate the Virtual environment
Open a new terminal in VS Code. It should show that the virtual environment is now active.

### Step 5: Install Dependencies
Run the following command:
```
pip install -r requirements.txt
```
### Step 6: Add Environment Variables
Copy the .env file into the root folder of the project.<br>
📁 The .env file was provided to professors as part of the GitHub Pages upload for this course.

### Step 7: Add Required JSON
- In the root folder, create a new folder called Json.
- Inside the Json folder, add a file named: "metadata_with_comments.json" <br>
📁 This JSON file was also included in the GitHub Pages upload provided to course instructors.

### Step 8: Run the Application
Run the following command:
```
python app.py
```
The app will start running on port 5000.

### Step 9: Test the AI
Try asking the following example question:
- "How many users are called John?"
- "How many users are from Belgium?"

## Troubleshooting
SQLAlchemy Connection Error
If you receive an error related to a failed connection from SQLAlchemy, it may be due to the IP address not being whitelisted by the HANA database. Ensure your current IP is accepted by the database admin.



