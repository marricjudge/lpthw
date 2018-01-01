from nose.tools import *
from app import app
from tools import assert_response

client = app.test_client() # create a testing client (a fake browser)
client.testing = True # enable this so that exceptions in your code bubble up to the test client

def test_index():
    global client
    resp = client.get('/') # with this client you can do all kinds of stuff
    assert_response(resp, status=302) # the root url should give back a redirect

    resp = client.get('/game')
    assert_response(resp) # just make sure we got a valid response

    resp = client.post('/game') # use POST, but provide no data
    assert_response(resp, contains="You Died!")

    # Go to another scene in the game
    testdata = {'userinput': 'tell a joke'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Laser Weapon Armory")

    # From there, go to yet another scene
    testdata = {'userinput': '132'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="The Bridge")


# from flask import Flask, session, request
# from flask import url_for, redirect, render_template
# import map
#
# app = Flask(__name__)
#
# @app.route('/game', methods=['GET'])
# def game_get():
#     if 'scene' in session:
#         thescene = map.SCENES[session['scene']]
#         return render_template('show_scene.html', scene=thescene)
#     else:
#         # The user doesn't have a session...
#         # What should your code do in response?
#     return render_template('you_died.html')
#
# @app.route('/game', methods=['POST'])
# def game_post():
#     userinput = request.form.get('userinput')
#     if 'scene' in session:
#         if userinput is None:
#             # Weird, a POST request to /game with no user input... what should your code do?
#             return render_template('you_died.html')
#         else:
#             currentscene = map.SCENES[session['scene']]
#             nextscene = currentscene.go(userinput)
#             if nextscene is None:
#                 # There's no transition for that user input.
#                 # what should your code do in response?
#                 return render_template('you_died.html')
#             else:
#                 session['scene'] = nextscene.urlname
#                 return render_template('show_scene.html', scene=nextscene)
#     else:
#         # There's no session, how could the user get here?
#         # What should your code do in response?
#         return render_template('you_died.html')
#
# # This URL initializes the session with starting values
# @app.route('/')
# def index():
#     session['scene'] = map.START.urlname
#     return redirect(url_for('game_get')) # redirect the browser to the url for game_get
#
# app.secret_key = 'replace this with your secret key'
#
# if __name__ == "__main__":
#     app.run()




# from nose.tools import *
# from app import app
# from tools import assert_response
#
# client = app.test_client() # create a testing client (like a fake web browser)
# client.testing = True # enable this so that errors in your web app bubble up to the testing client
#
# def test_index():
#     global client # let python know you want to use the global client variable in this function
#     # Check that we get a 404 on the / URL
#     resp = client.get('/')
#     assert_response(resp, status=404)
#     # test to make sure a GET request to /hello works (returns a 200 status code)
#     resp = client.get('/hello')
#     assert_response(resp)
#     # make sure the default values work when POST has no data
#     resp = client.post('/hello')
#     assert_response(resp, contains="Nobody")
#     # test that we get an expected response for specific input data
#     testdata = {'name': 'Jon', 'greet': 'Hola'}
#     resp = client.post('/hello', data=testdata)
#     assert_response(resp, contains="Jon")
