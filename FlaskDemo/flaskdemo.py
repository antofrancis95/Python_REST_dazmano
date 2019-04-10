from flask import Flask,render_template,url_for #importing flask class
app = Flask(__name__)


#List of dictionary
posts=[
{
	'title':'PYTHON FLASK',
	'author':'Anto Francis',
	'Date':'2019-04-09'
	
	}
]
@app.route("/")       # "/" - means-> root page of the website
   
@app.route("/home")                	 	
def home():
    return render_template('home.html', posts=posts)


#----------------------Andaconda command promt using Environment variables------------------------------ 
#set FLASK_APP=flaskdemo.py 
#set FLASK_DEBUG=1 --> for making changes in the script that reflects on server also.
#flask run --> Starting the server 127.0.0.1:5000

if __name__ == '__main__':  # to run directly --> python <file_name.py>	
   app.run(debug=True) 


