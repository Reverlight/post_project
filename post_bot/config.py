import string

# Main bot settings
NUMBER_OF_USERS = 3
MAX_POSTS_PER_USER = 3
MAX_LIKES_PER_USER = 4

# GENERATION
SENTENCES_PER_POST = 10
PASSWORD_CHARACTERS = string.ascii_letters+string.digits
PASSWORD_LENGTH = 8
EMAIL_DOMAINS = ['@gmail.com', '@yahoo-inc.com']
RANDOM_SENTENCES_PATH = 'random_sentences'
RANDOM_NAMES_PATH = 'random_names'

# REQUESTER
APP_LINK = 'http://127.0.0.1:8000'
USER_SIGNUP = f'{APP_LINK}/user/signup/'
POST_LIST_API = f'{APP_LINK}/posts/api/'
USER_SIGNUP_API = f'{APP_LINK}/user/signup/api/'
USER_LOGIN_API = f'{APP_LINK}/user/login/api/'
USER_LOGIN_PAGE = f'{APP_LINK}/user/login/'
POSTS_VIEW = f'{APP_LINK}/posts/'
POSTS_CREATION = f'{APP_LINK}/post/creation/'
POST_DETAIL = f'{APP_LINK}/post/{{id}}/'
LIKE_API = f'{POST_DETAIL}like/'
