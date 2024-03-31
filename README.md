# CineInsight : Movie Recommender System

## Introduction
This Movie Recommender System is a Python application built using Streamlit. It recommends movies based on either selected movies or genres chosen by the user. The recommendation algorithm is implemented using K Nearest Neighbors (KNN).

## Features
- **Two Recommendation Types**: Users can choose between recommending movies based on a selected movie or based on selected genres.
- **Interactive Interface**: The web application provides an intuitive interface for users to interact with and receive movie recommendations.
- **Data Source**: The system uses data sourced from the top 1000 movies from IMDb.
- **Movie Details**: Recommendations include details such as the movie's release year, duration, number of votes, and IMDb rating.
- **Customization**: Users can customize the number of movies to be recommended.

## Installation
1. Clone the repository:

    ```
    git clone <repository_url>
    ```
   
2. Install the required Python packages:

    ```
    pip install -r requirements.txt
    ```

3. Run the application:

    ```
    streamlit run app.py
    ```

## Usage
- Upon running the application, users are presented with a graphical user interface where they can choose the type of recommendation they desire.
- If selecting movies, users can choose a specific movie from a dropdown menu and customize the number of recommended movies.
- If selecting genres, users can select one or multiple genres, set an IMDb score threshold, and choose the number of recommended movies.
- After making selections, the system displays recommended movies along with their details such as release year, duration, votes, and IMDb rating.

## File Structure
- **app.py**: Main Python script containing the Streamlit application code.
- **Classifier.py**: Python module containing the implementation of the K Nearest Neighbors algorithm.
- **Data**: Directory containing JSON files with movie data, titles, and details.
- **Images**: Directory containing images used in the application interface.
- **README.md**: Documentation file.

## Technologies
- **Streamlit**: Web application framework used for building the interactive interface.
- **PIL (Python Imaging Library)**: Library used for image processing and display.
- **BeautifulSoup**: Library used for web scraping.
- **Requests**: Library used for making HTTP requests.
- **JSON**: Library used for handling JSON data.
