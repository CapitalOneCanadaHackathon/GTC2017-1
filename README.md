# CEE Alumni Social Media (Challenge 2 of CEE w/ Gift the Code Hackathon)

Currently, tracking staff and alumni activity and staying in contact with them is a very manual process. 
Through social media platforms (Instagram, Facebook, Twitter, Snapchat, etc.),
staff are able to stay connected with alumni, stay up-to-date on how they’re doing and what they’re involved in.

# Solution

We started by exploring the possibility of automated solutions using Facebook, Instagram and Twitter APIs, but found that these would not be possible due to the security and privacy restrictions that Facebook and Instagram place on their platforms. (We could have made an automated notification system that tracked hashtags on Twitter, but we spoke to Adanna from CEE on Saturday and learned that few of their alumni use twitter and that this wouldn't be that helpful.) 

We've responded to the challenge by creating a web app that supports the process of keeping up with CEE program alumni on social media. The web app provides a directory of all CEE program alumni, along with links to their various social media accounts, and presents the information according to how recently a staff member has reviewed their posts. We asked Adanna how regularly CEE tries to keep up with alumni, and she said about once a month. To support this rhythm within CEE's team, the app allows staff members to mark alumni as 'reviewed', which updates their next review date to the next month. The app consists of a web interface, which could be password protected, and a google sheet for entering and editing alumni contact info. 


### Flask App
![frontend flask app](/static/demo.png)

### Backend: Google Sheet
![backend is a google sheet](/static/demo_sheet.png)

## Requirements

```
pip install pandas
pip install flask
pip install oauth2client
pip install gspread
```

After installing the required packages, follow the tutorial on gspread to [set up Google Sheets API](http://gspread.readthedocs.io/en/latest/oauth2.html)
and create a file in this directory called `secret.py`.

```
# filename:secret.py

secret_file = "path/to/credentials.json"
```

A product pipeline will have to have their own google account and sheets to manage the contacts. Once the sheets credientials
and sheet file is organized. simply run the flask on your host of choice to get things up an running. Locally we can run

```
FLASK_APP=app.py flask run
```
