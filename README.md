# IISMA-Dashboard

# Data and Website Description
The data was gathered from https://iisma.kemdikbud.go.id/info/host-universities-list/ before the IISMA 2024 website maintenance. Data such as requirements and intakes from each university was taken to be made into a website. The website is used display all the requirements and intakes from the universities with the choice to filter the results.

# Program Spesification

### Project Steps
This project is divided into 5 steps, Data Scraping, Preprocessing, JSON Creation, SQL Dumping, and Website Creation
1. The first step is to scrape the data using python libraries such as BeautifulSoup and Selenium
2. After the data is acquired, some pre-processing is applied to the data to simplify the analysis and website creation process
3. The data is then converted into a JSON structure
4. The JSON is then created into an SQL dump to be used in the website's database
5. The website is then created using Flask and SQLite as the database.

# How to Use the Program
### Data Scraping
```
git clone https://github.com/Wentonn/IISMA-Dashboard
```
Open the Data Scraping Directory
Open the iisma.ipynb
Run All

**Note : It is probably not runable as the website is currently under maintenance and might have changes when it is done.**

### SQL
```
git clone https://github.com/Wentonn/IISMA-Dashboard
cd IISMA-Dashboard/"Data Scraping"
psql -U {username} -d {database_name} < iisma.sql
```

### Web App
```
git clone https://github.com/Wentonn/IISMA-Dashboard
cd IISMA-Dashboard/Web
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
echo "FLASK_DATABASE=board.sqlite" > .env
python -m flask --app board init-db
python -m flask --app board run --port 8000 --debug
```

# JSON Structure 
From the scraped data, the data is converted into a JSON format,
IISMA Intake :
```json
{
    "GPA Min": 3.39,
    "GPA Max": 3.96,
    "TOEFL Score Min": null,
    "TOEFL Score Max": null,
    "IELTS Score Min": "8.5",
    "IELTS Score Max": "8.5",
    "Duolingo English Test Score Min": 140.0,
    "Duolingo English Test Score Max": 155.0,
    "Total Students": 20,
    "Uni Name": "Boston University",
    "Type": "Awardees",
    "Year": "2022"
}
```

IISMA University :
```json
{
    "University": "Boston University",
    "Location": "United States of America",
    "Images": "https://i0.wp.com/iisma.kemdikbud.go.id/info/wp-content/uploads/2022/02/Boston-Univ.png?fit=300%2C300&ssl=1",
    "Region": "America & Canada"
}
```

IISMA Requirements : 
```json
{
    "Uni Name": "Boston University",
    "GPA": 3.0,
    "IELTS": 6.5,
    "TOEFL": 84.0,
    "Duolingo English Test": 110.0
}
```

# Screenshots
Here are some screenshots from the scraping process.
![alt text](https://github.com/Wentonn/IISMA-Dashboard/blob/main/Data%20Scraping/pandas/intake_table.jpg)
![alt text](https://github.com/Wentonn/IISMA-Dashboard/blob/main/Data%20Scraping/pandas/requirements_table.jpg)
![alt text](https://github.com/Wentonn/IISMA-Dashboard/blob/main/Data%20Scraping/pandas/university_table.jpg)
