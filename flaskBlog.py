from flask import Flask, render_template, url_for
from form import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'b8b227996c56e1386e49c0408412313e' #usually as random number. Can use python3. Import secret, secrets.token_hex(16)

posts =[
	{
		'author': 'ni mei',
		'title': 'how to become a god',
		'content': 'idk',
		'date_posted': 'April 1, 2020'
	},
	{
		'author': 'keng si ni',
		'title': 'how to troll your teammate',
		'content': 'inting in early 20 mins',
		'date_posted': 'April 1, 2020'
	}
]

@app.route("/") # "/" means the web root page

def hello():
	return render_template('home.html', userPosts=posts)

@app.route("/about")

def about():
	return render_template('about.html', title='About Page')

@app.route("/register")

def register():
	form = RegistrationForm()
	return render_template('register.html', title="Registration Page", form = form)


if __name__ == '__main__':
	app.run(debug=True) #the webpage will run as debug mode
