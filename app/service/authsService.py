from oauth2client.client import OAuth2WebServerFlow
from oauth2client import tools

def authenticate_youtube(code=None):
    CLIENT_ID = '203023096012-aebrgm0bgfv701lmcru00hqn8c2bibpk.apps.googleusercontent.com'
    CLIENT_SECRET = 'D7A1L_Oj2uGCINDLcdbZ4FOL'

    flow = OAuth2WebServerFlow(client_id=CLIENT_ID,
                               client_secret=CLIENT_SECRET,
                               scope='https://www.googleapis.com/auth/youtube.readonly https://www.googleapis.com/auth/youtube',
                               redirect_uri='http://localhost:10101/auth/google')

    if code:
        credentials = flow.step2_exchange(code)
        print credentials.to_json()
        return credentials
    else:
        auth_uri = flow.step1_get_authorize_url()
        return auth_uri
