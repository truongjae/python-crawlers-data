import requests
USERNAME = 'truongjae@gmail.com'
PASSWORD = 'tu1den82001'
PROTECTED_URL = 'https://m.facebook.com/groups/318395378171876?view=members'
def login(session, email, password):
    '''
    Attempt to login to Facebook. Returns cookies given to a user
    after they successfully log in.
    '''

    # Attempt to login to Facebook
    response = session.post('https://m.facebook.com/login.php', data={
        'email': email,
        'pass': password
    }, allow_redirects=False)

    assert response.status_code == 302
    #assert 'c_user' in response.cookies
    return response.cookies

if __name__ == "__main__":
    session = requests.session()
    cookies = login(session, USERNAME, PASSWORD)
    response = session.get(PROTECTED_URL, cookies=cookies,allow_redirects=False)
    #assert response.text.find('Home') != -1
    print(cookies)
    print(response)
