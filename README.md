# CEE Alumni Social Media (Challenge 2 of CEE w/ Gift the Code Hackathon)

Currently, tracking staff and alumni activity and staying in contact with them is a very manual process. 
Through social media platforms (Instagram, Facebook, Twitter, Snapchat, etc.),
staff are able to stay connected with alumni, stay up-to-date on how they’re doing and what they’re involved in.

# Solution

We provide a flask app backed by a Google sheet which allows staff to track and be up to date with their alumni.

![](/static/demo.png)

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
