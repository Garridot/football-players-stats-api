# Football Players Stats API

**Football Players Stats is a project designed to manage the extraction, cleaning, saving, and visualization of data on athletes' performance to illustrate their impact and goal contributions in their careers.**

---
<br>

It consists of three modules: **API**, **web scraping**, and **website**, which operate independently and communicate with each other.

- The core **API** manages the project logic, authentication, and database connection. It was developed using **Django Rest Framework**.

- Data extraction is performed using **BeautifulSoup (bs4)** and **Pandas**. **GitHub actions** are utilized for automation. You can see the web scraping [here](https://github.com/Garridot/football_players_web_sraping).

- The website was built using **Flask**, **JavaScript**, and **Charts js**. You can see the website [here](https://github.com/Garridot/football_players_charts).

<br>

### Table of Contents

- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)	
- [Examples](#examples)	
- [Web Scraping](#web-scraping)
- [Questions](#questions)
- [Deployment on Render](#deployment-on-render)

---


## Getting Started

### Prerequisites

Ensure that you have Python 3.8.x installed on your system. If not, you can download it from the official [Python website](https://www.python.org/downloads/). 

1. Clone the project repository:

```bash
git clone https://github.com/Garridot/football-players-stats-api
```

2. Create a virtual environment:
```bash
virtualenv env
source env/bin/activate
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

4. Configure the database and run migrations:
```
python manage.py migrate.
```
5. Start the development server: 
```
python manage.py runserver.
```
## API Endpoints
- ### Players:
    - **GET /players/**: Get a list of players.
    - **GET /players/{id}/**: Get the player.
    - **POST /players/**: Create a new player. (Authentication required).
    - **PUT /players/{id}/**: Update a player. (Authentication required).
    - **DELETE /players/{id}**/: Delete a player. (Authentication required).

- ### Player Statistics:
    - **GET /player_stats/**: Get a list of player statistics.
    - **GET /player_stats/{id}/**: Get the player statistics.
    - **POST /api/player_stats/**: Create new player statistics. (Authentication required).
    - **PUT /player_stats/{id}/**: Update player statistics. (Authentication required).
    - **DELETE /player_stats/{id}/**: Delete player statistics. (Authentication required).

- ### Player Stats by Position  
    - **GET /player_stats_by_position/**: Get a list of player statistics by position.  

- ### Authentication:
    - **POST /authentication/**: Get token authentication. 
    - **POST /register/**: Register a new user. 

        

## Authentication
The API uses Json Web Token authentication. 

Include the token in the header for authenticated requests:
```
curl -H "Authorization: Token your_access_token" http://127.0.0.1:8000/
```

Replace **your_access_token** with the actual token obtained during authentication.

**Note**: Authentication is required for **POST**, **PUT**, and **DELETE** operations. Ensure that you include the authentication token in the request header for these actions.

## Examples

### Function to retrieve players data from the API 

``` python
def get_list_players():  
    
    try:        
        headers = {"Content-Type": "application/json"} # set headers to indicate JSON content         
        response = requests.get(URL_PLAYERS, headers)
        response.raise_for_status()  # Raises an exception for non-successful HTTP responses
        return response.json()
    except requests.exceptions.RequestException as e:
        # Handle the request exception, for example, logging an error message
        return print(f"Error during request: {e}")
```

#### **Result:**

```
[
    {'id': 1, 'name': 'Lionel Messi', 'age': 36, 'date_of_birth': '1987-06-24', 'nationality': 'Argentina', 'position': 'Right Winger', 'current_club': 'Miami'},
    {'id': 2, 'name': 'Kylian Mbappé', 'age': 24, 'date_of_birth': '1998-12-20', 'nationality': 'France', 'position': 'Left Winger', 'current_club': 'Paris SG'}, 
    {'id': 3, 'name': 'Erling Haaland', 'age': 23, 'date_of_birth': '2000-07-21', 'nationality': 'Norway', 'position': 'Centre-Forward', 'current_club': 'Man City'}, 
    {'id': 4, 'name': 'Vinicius Junior', 'age': 23, 'date_of_birth': '2000-07-12', 'nationality': 'Brazil', 'position': 'Left Winger', 'current_club': 'Real Madrid'}, 
    {'id': 5, 'name': 'Robert Lewandowski', 'age': 35, 'date_of_birth': '1988-08-21', 'nationality': 'Poland', 'position': 'Centre-Forward', 'current_club': 'Barcelona'},
    ... 
]
```


### Function to retrieve player details from the API based on player ID
```
data = {'player': 1} # Filter player data by id
```

``` python
def get_player(data):  
    try:        
        headers = {"Content-Type": "application/json"} # set headers to indicate JSON content 
        response = requests.get(f"{URL_PLAYERS}{data['player']}", headers=headers)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        return print(f"Error during request to stats API: {e}")
```

#### **Result:**

```
[
    {'id': 1, 'name': 'Lionel Messi', 'age': 36, 'date_of_birth': '1987-06-24', 'nationality': 'Argentina', 'position': 'Right Winger', 'current_club': 'Miami'},    
]
```
        
### Function to retrieve player stats from the API based on player data 

```
data = {'player': 1, 'competition': 'UEFA Champions League'} # Filter stats by player and competition
```

``` python
def get_stats(data): 
    try:
        data_json = json.dumps(data)  # convert data to JSON format 
        headers = {"Content-Type": "application/json"} # set headers to indicate JSON content 
        response = requests.get(URL_PLAYERS_STATS, data=data_json, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return print(f"Error during request to stats API: {e}")               
``` 

#### **Result:**

```
[
    {'id': 11, 'team': 'FC Barcelona', 'competition': 'UEFA Champions League', 'goals': 5, 'assists': 2, 'games': 6, 'wins': 3, 'draws': 1, 'defeats': 0, 'team_goals': 11, 'minutes_played': 540, 'season': '2020-2021', 'player': 1}, 
    {'id': 17, 'team': 'FC Barcelona', 'competition': 'UEFA Champions League', 'goals': 3, 'assists': 4, 'games': 8, 'wins': 4, 'draws': 3, 'defeats': 0, 'team_goals': 13, 'minutes_played': 661, 'season': '2019-2020', 'player': 1}, 
    {'id': 23, 'team': 'FC Barcelona', 'competition': 'UEFA Champions League', 'goals': 12, 'assists': 3, 'games': 10, 'wins': 7, 'draws': 2, 'defeats': 0, 'team_goals': 23, 'minutes_played': 837, 'season': '2018-2019', 'player': 1}, 
    {'id': 28, 'team': 'FC Barcelona', 'competition': 'UEFA Champions League', 'goals': 6, 'assists': 2, 'games': 10, 'wins': 6, 'draws': 3, 'defeats': 0, 'team_goals': 17, 'minutes_played': 783, 'season': '2017-2018', 'player': 1},
    ... 
]
```

### Function to retrieve player stats by position from the API
```
data = {'player': 1, 'season': '2022-2023'} # Filter stats by player and season
```

``` python
def get_stats_by_position(data): 
    try:
        data_json = json.dumps(data)  # convert data to JSON format 
        headers = {"Content-Type": "application/json"} # set headers to indicate JSON content 
        response = requests.get(URL_STATS_BY_POSITION, data=data_json, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return print(f"Error during request to stats API: {e}") 
``` 

#### **Result:**

```
[
    {'id': 319, 'position': 'Centre-Forward', 'goals': 11, 'assists': 14, 'games': 26, 'season': '2022-2023', 'player': 1}, 
    {'id': 320, 'position': 'Right Winger', 'goals': 15, 'assists': 7, 'games': 19, 'season': '2022-2023', 'player': 1}, 
    {'id': 321, 'position': 'Second Striker', 'goals': 4, 'assists': 3, 'games': 5, 'season': '2022-2023', 'player': 1}, 
    {'id': 322, 'position': 'Attacking Midfield', 'goals': 2, 'assists': 1, 'games': 5, 'season': '2022-2023', 'player': 1
    ... 
]
```


### Function to get your authentication token

```
data = { "email": YOUR_EMAIL, "password": YOUR_PASSWORD}
```
``` python
def get_auth_token(data):     
    data_json = json.dumps(data) # convert data to JSON format    
    headers = {"Content-Type": "application/json"} # set headers to indicate JSON content    
    response = requests.post(API_AUTH_URL, data=data_json, headers=headers) # make a POST request to the authentication API
    
    if response.status_code == 200:  # check the response status code        
        token = response.json()['access'] # Extract and return the access token from the response
        return token
    else:        
        raise Exception(f"Error during request to stats API. Status code: {response.status_code}")        
```

### Function to create a new player 


``` 
data = {
        'name': 'Vinicius Junior', 
        'age': 23, 
        'date_of_birth': '2000-07-12', 
        'nationality': 'Brazil', 
        'position': 'Left Winger', 
        'current_club': 'Real Madrid' 
    } 
``` 
``` python
def create_player(data):             
    
    token = get_auth_token() # get the authentication token    
    data_json = json.dumps(data) # convert data to JSON format

    # set headers to indicate JSON content and include the authentication token
    headers = { "Content-Type": "application/json", "Authorization": f"Bearer {token}"}    

    # Make a POST request to add new data
    response = requests.post(API_PLAYERS_URL, data=data_json, headers=headers)
    
    if response.status_code == 200: 
        print(f"Player added successfully: {response.json()}")
    else:
        print(f"Failed to add the player: {response.json()}")
``` 

#### **Result:**
``` 
Player added successfully:
{'id': 1, 'name': 'Vinicius Junior', 'age': 23, 'date_of_birth': '2000-07-12', 'nationality': 'Brazil', 'position': 'Left Winger', 'current_club': 'Real Madrid'}, 
``` 
## Web Scraping

This API uses an automated process called web scraping to collect data. It then stores and updates this information regularly to ensure it remains accurate and up-to-date. 

This Python web scraping project focuses on extracting football player statistics from the Transfermarkt website. The main script, main.py, uses the BeautifulSoup library to parse the HTML content of web pages and extract the necessary information. The schedule to run this script is configured using GitHub Actions.

You can see the [Web Scraping Project here.](https://github.com/Garridot/football_players_web_sraping)

## Questions
Feel free to explore and modify the code to suit your specific requirements. If you encounter any issues or have questions, please [open an issue](https://github.com/Garridot/football-players-stats-api/issues).
## Deployment on Render

This project is set up for deployment on Render Cloud Hosting. Follow these steps to deploy:

1. Create an account on [Render](https://render.com/).

2. Click the button below to automatically deploy on Render:

   [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

3. Follow the instructions to configure your deployment. You can customize the service name, environment settings, and more.

4. Once deployed, your API will be available at the URL provided by Render.
