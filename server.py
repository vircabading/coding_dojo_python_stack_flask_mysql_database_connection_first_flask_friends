from flask import Flask, render_template, session, redirect, request

# import the class from friend.py
from friend import Friend

app = Flask(__name__)
app.secret_key = "TiYSKDNRitA!"                                                     # This is Your Secret Key Do Not Reveal it to Anyone!

@app.route('/')                                                                     # Main Page
def index():
    # //// call the get all classmethod to get all friends ////////
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html")

# @app.route('/increment_by', methods=['POST'])
# def increment_by():
#     return redirect("/")

# **** Ensure that if the user types in any route other than the ones specified, 
#           they receive an error message saying "Sorry! No response. Try again ****
@app.errorhandler(404) 
def invalid_route(e): 
    return "Route is invalid. Try again."

if __name__=="__main__":   
    app.run(debug=True)    