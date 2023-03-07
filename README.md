# Posting App

Main features:

- Create post
- View post
- Like post
- Like analytics
- User JWT authorization

## How to install
* Install python 3
* Create virtualenv
* Git clone this repository
* Use following commands for set-up:

```shell
pip install -r requirements
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic

```

## Run Server

```shell
python manage.py runserver
```

## User Guide
Open root url to navigate:

http://localhost:8000/

![Screenshot_1](https://user-images.githubusercontent.com/52380931/159695243-d6cc9696-f2cd-463b-a49e-61bcae9ef91a.png)

# Post Bot
Main features:

- Create posts with random generated content
- Like posts
- Signup, login random generated user


# Main bot settings
Edit config to change behavior according to your requirements
post_bot/config.py

NUMBER_OF_USERS

MAX_POSTS_PER_USER

MAX_LIKES_PER_USER
