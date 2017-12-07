# Info

This project utilizes Python, so if you haven't already, install the most recent version of Python from here: https://www.python.org/downloads/

*_This code should grab the most recent stock prices for Intel every 10 seconds, and then save all fetched data in a table._*

Scraped Site: https://www.investopedia.com/markets/stocks/intc/?ad=dirN&qo=investopediaSiteSearch&qsrc=0&o=40186

Tutorial I followed: https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe

*The setup ALSO requires you to install beautifulsoup, which can be very unreliable. Didn't realise this after I finished the project, so just as a warning beautifulsoup might not install correctly on your machine, especially if its one from school. I'm not sure what the issue is, but if I find a resolution I'll post it ASAP. For now, just run the program without beautifulsoup. You'll get some error code, but I think it still prints the correct information above all the error code. Sorry for the inconvenience!*
# Setup
1. Open your command line (command key + r, then type in cmd and press enter)

2. Activate your virtual environment (SKIP IF YOU ALREADY HAVE ONE READY)
  - Navigate to your python installation folder and pip install virtual environment
  
  ```
  cd C:\Python27\Scripts
  pip install virtualenv
  cd C:\Users\"Username"\Documents\
  mkdir Python
  cd Python
  C:\Python27\Scripts\virtualenv.exe -p C:\Python27\python.exe .lpvenv
  .lpvenv\Scripts\activate
  ```
  
3. Install Beautifulsoup from your command line
  ```
  pip install beautifulsoup4
  
  ```
4. Place web-scraperFINAL.py in your new Python folder under Documents, then navigate to that same folder inside the command line. Run the file by typing in the name and hitting enter, or just tab until you get the right file.

5. While it's running on the command line, it should fetch the current prices for Intel stocks and save it to a table in the same folder that you ran the program out of. If you can't find it, search for index.csv in your file explorer. For easy access, I would suggest creating a shortcut on your desktop to the table.

