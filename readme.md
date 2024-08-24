- [X] Display weather
    - [X] Ask api for: Condition, Temperature, Precipitation & Wind
        - command: curl 'wttr.in/Armagh?format=%C|%p|%t|%w'
        - response: Partly cloudy|0.0mm|+14°C|↓24km/h


- [ ] Store weather data
    - [X] Parse data
        - [X] Name each condition, and print it out
    - [X] Create SQLite database
    - [X] Create table
    - [ ] Store data

- [ ] Ignore db file in git