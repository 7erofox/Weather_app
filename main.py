import requests
import sqlite3
from datetime import datetime

create_table_query = """CREATE TABLE IF NOT EXISTS weather (
  id INTEGER PRIMARY KEY, 
  created_at TEXT NOT NULL,
  condition TEXT NOT NULL,
  precipitation TEXT NOT NULL,
  temperature TEXT NOT NULL,
  wind_speed TEXT NOT NULL 
);"""

insert_row_query = """insert into weather ( 
created_at,
condition,
precipitation,
temperature,
wind_speed
) VALUES (
"{}","{}","{}","{}","{}");
"""

weather = requests.get('https://wttr.in/Armagh?format=%C|%p|%t|%w')
true_weather = weather.text
print(true_weather)
print(weather.status_code)

split_weather = true_weather.split("|")
condition = split_weather[0]
precipitation = split_weather[1]
temperature = split_weather[2] 
wind_speed = split_weather[3]
created_at = datetime.now()


conn = sqlite3.connect("weather.db")
cursor = conn.cursor()
cursor.execute(create_table_query)
conn.commit()
cursor.execute(insert_row_query.format(created_at, condition, precipitation, temperature, wind_speed))
conn.commit()
conn.close()