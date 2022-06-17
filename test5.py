"""import mechanize
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
browser.set_handle_refresh(False)

url = 'http://www.facebook.com/login.php'
browser.open(url)
browser.select_form(nr = 0)       #This is login-password form -> nr = number = 0
browser.form['email'] = "truongjae@gmail.com"
browser.form['pass'] = "tumotdentam2k1"
response = browser.submit()
print (response.read())"""
#import robobrowser

"""from robobrowser import RoboBrowser
from .browser import RoboBrowser

class Facebook(robobrowser.RoboBrowser):

    url = 'https://facebook.com'

    def __init__(self, email, password):
        self.email = email
        self.password = password
        super().__init__()
        self.login()

    def login(self):
        self.open(self.url)    
        login_form = self.get_form(id='login_form')
        login_form['email'] = self.email
        login_form['pass'] = self.password
        self.submit_form(login_form)
a = Facebook('truongjae@gmail.com','tumotdentam2k1')
a.login()"""
# https://gist.github.com/UndergroundLabs/fad38205068ffb904685
# this github example said tokens are also necessary, but I found 
# they were not needed
import requests

USERNAME = 'truongjae@gmail.com'
PASSWORD = 'tumotdentam2k1'
PROTECTED_URL = 'https://m.facebook.com/login.php'

def login(session, email, password):

    response = session.post('https://m.facebook.com/login.php', data={
        'email': email,
        'pass': password
    }, allow_redirects=False)
    if 'c_user' in response.cookies:
   		print('co')
    return response.cookies
    # assert response.status_code == 302
    


if __name__ == "__main__":
    session = requests.session()
    cookies = login(session, USERNAME, PASSWORD)
    response = session.get(PROTECTED_URL, cookies=cookies, 
allow_redirects=False)
    #print(response.text.find('Home') != -1)
    #print(response.text)