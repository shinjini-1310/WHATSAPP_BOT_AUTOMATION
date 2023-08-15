# WHATSAPP_BOT_AUTOMATION

Pre-requisites:
1)Python should be installed and its path should be added to environment variable 
2)Requires installation and import of Python packages
3)Webdriver installation based on browser choice
4)A steady Internet connection
5)WhatsApp account at both sender and receiver ends

SUMMARY
Developed a WhatsApp bot that runs with minimal manual intervention. It needs WhatsApp installed at both sender and receiver ends. On triggering the bot, it opens browser, asks for QR code scan to connect with sender's WhatsApp account, searches for the receiver's name in contact list, visits receiver's profile and sends him the message provided by sender. We assure that the action is executed optimally by ensuring that the bot performs each run within time constraint and by comparing expected and observed elapsed time

TECHNOLOGIES USED
Backend: Python, Selenium
Frontend: Shell Scripting,Website - https://web.whatsapp.com/

ACHIEVEMENTS
1)Simple Setup : All we need are active whatsapp accounts at both nodes of this communication, and Python with its libraries installed in the sender's machine.
2)Minimal Execution Time : Since its helpful for beginners to see the step-by-step execution of bot, some sleeping time is allowed between each step. Even then, each run is elapsed within or very close to the expected time.
3)Automatic Snapshotting : Photographic evidences with personalized titles are automatically captured at each step of each run, ensuring that consolidated proofs are available to support the execution status of each bot run.
4)Elimination of Manual Effort : Other than scanning of QR code,passing message and receiver names in the trigger command, no other manual effort is required in this project. The bot automates the entire process.
5)Authentic Learning Opportunity : We worked with an actual live website in this project, not a manufactured, simplified website. In-depth knowledge of web elements was acquired by extensive research on formulating locators for complex element location in the webpage of WhatsApp.
6)Error Handling : We devised the bot in a way that eliminates the requirement to dive into wordy,lengthy traceback errors/ exceptions. A one-liner message will be displayed with the exact observed error.

TRIGGER COMMAND:
python [PYTHON_FILENAME_WITH_LOCATION] [COMMA_DELIMITED_RECEIVER_NAME_LIST] [DOUBLE QUOTED MESSAGE]
