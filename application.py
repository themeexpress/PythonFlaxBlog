from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '4629c8cd6e0a2bdcd746587bf987093e'

posts = [
    {
        'author': "Kamrul Islam",
        'title': "First Blog post",
        'content': "Extra Virgin Coconut Oil can be used both internally, adding it to dishes and using it for cooking, as well as externally on your hair and skin. No matter how you use it",
        'date_posted': 'April 20, 2018'
    },
{
        'author': "Corey Schafer",
        'title': "Second Blog post",
        'content': "Extra Virgin Coconut Oil can be used both internally, adding it to dishes and using it for cooking, as well as externally on your hair and skin. No matter how you use it",
        'date_posted': 'April 20, 2021'
    },
{
        'author': "Bod dilan",
        'title': "Third Blog post",
        'content': "Extra Virgin Coconut Oil can be used both internally, adding it to dishes and using it for cooking, as well as externally on your hair and skin. No matter how you use it",
        'date_posted': 'April 20, 2021'
    },
{
        'author': "Willam Thomas",
        'title': "Forth Blog post",
        'content': "Extra Virgin Coconut Oil can be used both internally, adding it to dishes and using it for cooking, as well as externally on your hair and skin. No matter how you use it",
        'date_posted': 'April 20, 2022'
    },
]
@app.route('/')
def home():
    return render_template('home.html', posts=posts, title="MyFlaskBlog")

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title="Register", form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title="Login", form=form)

if __name__ == '__main__':
    app.run()