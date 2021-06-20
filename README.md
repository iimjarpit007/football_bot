# football_bot
this is a football bot created using RASA NLU framework with web scrapping data and optional bot telegram integration using ngrok

Major requirements and libraries

Tools/Softwares-

visual Studio toolkit
Python 3.7(64bit) or 3.6(64bit)
Pycharm UI-Optional
RASA(Rasa X optional)

Libraries-

tensorflow
Kera
Selenium(optional)
sklearn
scikit-learn
requests
regex
kera-preprocessing
bs4
numpy
datetime
pandas

Note-

Pycharm venv integration should be done with 3.7 or 3.6 path only, it is not working for 3.9 or latest
Telegram integration of bot has been integrated in code but has been commented. you can go to credential file and uncomment the same
Action server should be started as it utilizes action methods to pass the content related to football scores.

Working-
this is a simple football bot which is built under the RASA NLU framwork which understand user language and anticipate the next with help of NLU and RASA core

-through webscrapping football data has been extracted and returned through python file-football.py in form of methods and passed on to RASA action
-forms are integrated to extract customer first name and last name(can be replaced by email to extract the same)
-ngrok framework has been used to integrate bot with telegram with help of creation of tunnel




