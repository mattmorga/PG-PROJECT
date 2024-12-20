# PG-PROJECT
web based movie suggestion system

# Web-Based Movie Suggestion System

## Project Overview
This project is a **Web-Based Movie Suggestion System** developed using Python, MySQL, HTML, and CSS. It is designed to recommend movies based on user input and preferences. The application utilizes a simple web interface for interaction and a backend built with Python and MySQL to handle user requests and data storage.

### Key Features:
- **User-Friendly Web Interface**: Built using HTML and CSS, the system provides an intuitive platform for users to search and receive movie recommendations.
- **Dynamic Movie Suggestions**: The backend uses Python to process user queries and fetch relevant movie suggestions from the database.
- **Real-Time Data**: A real-time Python script fetches movie data and updates the suggestions accordingly.
- **Database Integration**: MySQL is used to store movie data, user preferences, and search history.

---

## Technologies Used:
- **Frontend**: HTML, CSS
- **Backend**: Python (Flask)
- **Database**: MySQL
- **Text Editor/IDE**: Visual Studio Code

---

## Project Files:
1. **`search.html`**: The HTML file that provides the structure for the user interface where users can search for movies.
2. **`app.py`**: The main Python application file that runs the web server and handles requests, interacting with the database to provide movie suggestions.
3. **`realtime.py`**: A Python script that updates movie data in real-time, ensuring that the system provides the most current suggestions.
4. **`requirements.txt`**: The file to list all Python dependencies needed for the project, such as Flask, MySQL connector, etc.
5. **`README.md`**: This file, providing an overview and documentation for the project.

---

## Setup Instructions:
### Prerequisites:
- Python 3.x
- MySQL database server
- Visual Studio Code (or any preferred IDE)

### Steps to Run the Project:
1. **Clone the Repository:**
   ```bash
   git clone <repository-link>
   cd <project-folder>
   ```

2. **Install Required Dependencies:**
   - Make sure Python is installed, then install necessary dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up the Database:**
   - Create a MySQL database and import the required schema for the movie data.
   - Update the database connection settings in `app.py` and `realtime.py` to match your local MySQL configuration.

4. **Run the Application:**
   - Start the application using the following command:
   ```bash
   python app.py
   ```
   - Visit `http://127.0.0.1:5000` in your web browser to interact with the Movie Suggestion System.

---

## How It Works:
1. The user enters a query or preferences in the `search.html` page.
2. The **`app.py`** file receives the input, processes it, and queries the MySQL database for relevant movie suggestions.
3. **`realtime.py`** ensures the data remains updated by retrieving real-time information from external sources or APIs.
4. The system displays the movie recommendations on the frontend, providing users with a list of movies based on their search criteria.

---

## Future Enhancements:
- **User Profile System**: Implement user login and save preferences for personalized suggestions.
- **Advanced Recommendation Algorithm**: Incorporate machine learning algorithms for more accurate movie recommendations.
- **Integration with APIs**: Use movie data APIs (e.g., TMDb or OMDB) for dynamic movie information.

---

## License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
