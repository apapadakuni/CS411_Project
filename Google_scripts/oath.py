from __future__ import print_function # In python 2.7
from flask import Flask, redirect, url_for, session
from flask_oauth import OAuth
import ast
import sys
from flask import Blueprint

# You must configure these 3 values from Google APIs console
# https://code.google.com/apis/console
GOOGLE_CLIENT_ID = '279331729673-1187c5t7eja4tao5lmcikbnf443fj040.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = 'aNuew-vKzjQxUz1pZLLigQ-w'
REDIRECT_URI = '/oauth2callback'  # one of the Redirect URIs from Google APIs console

SECRET_KEY = 'development key'
DEBUG = True

app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY
oauth = OAuth()
email = ''
first_name = ''
google = oauth.remote_app('google',
                          base_url='https://www.google.com/accounts/',
                          authorize_url='https://accounts.google.com/o/oauth2/auth',
                          request_token_url=None,
                          request_token_params={'scope': 'https://www.googleapis.com/auth/userinfo.email',
                                                'response_type': 'code'},
                          access_token_url='https://accounts.google.com/o/oauth2/token',
                          access_token_method='POST',
                          access_token_params={'grant_type': 'authorization_code'},
                          consumer_key=GOOGLE_CLIENT_ID,
                          consumer_secret=GOOGLE_CLIENT_SECRET)

@app.route('/sign-in')
def index():
    #Displayed data in the end
    print('at index', file = sys.stderr)
    access_token = session.get('access_token')
    if access_token is None:
        return redirect(url_for('login'))

    access_token = access_token[0]
    from urllib2 import Request, urlopen, URLError

    headers = {'Authorization': 'OAuth '+access_token}
    req = Request('https://www.googleapis.com/oauth2/v1/userinfo',
                  None, headers)
    try:
        res = urlopen(req)

    except URLError, e:
        if e.code == 401:
            # Unauthorized - bad token
            session.pop('access_token', None)
            return redirect(url_for('login'))
        return res.read()

    a = res.read()
    #Need to capitalize True or Flase in order to conert to dictionary


    user_info_str = a.replace('true', 'True')
    user_info_str = user_info_str.replace('false', 'False')
    user_info = ast.literal_eval(user_info_str)
    user_email = user_info['email']
    user_first_name = user_info['given_name']

    # #Printing just for checking
    print('yoooo', file = sys.stderr)
    print(user_email, file = sys.stderr)
    print(user_first_name, file = sys.stderr)
    return res.read()


@app.route('/login')
def login():
    print('at login', file=sys.stderr)
    callback=url_for('authorized', _external=True)
    return google.authorize(callback=callback)



@app.route(REDIRECT_URI)
@google.authorized_handler
def authorized(resp):
    print('at authorized', file=sys.stderr)
    access_token = resp['access_token']
    session['access_token'] = access_token, ''
    return redirect(url_for('index'))


@google.tokengetter
def get_access_token():
    print('at get_access_token', file=sys.stderr)
    return session.get('access_token')


def main():
    app.run()


if __name__ == '__main__':
    main()
