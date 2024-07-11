import requests

weather = requests.get('https://wttr.in/Armagh?format=%C|%p|%t|%w')
true_weather = weather.text

split_weather = true_weather.split("|")
condition = split_weather[0]
precipitation = split_weather[1]
temperature = split_weather[2] 
wind_speed = split_weather[3] 

print("Condition:", condition)
print("Precipitation:", precipitation)
print("Temperature:", temperature)
print("Wind speed:", wind_speed)