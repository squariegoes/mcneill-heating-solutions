from flask import *

app = Flask(__name__)
app.secret_key = 'my precious'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/boiler_fitting')
@app.route('/boiler_servicing')
@app.route('/plumbing')
@app.route('/bathroom_fitting')
def services():
    modes = {
        "/boiler_fitting": "boiler_fitting",
        "/boiler_servicing": "boiler_servicing",
        "/plumbing": "plumbing",
        "/bathroom_fitting": "bathroom_fitting",
    }

    return render_template('services.html', mode=modes.get(request.url_rule.rule))

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(e):
    return home()

if __name__ == '__main__':
    app.debug = True
    app.run()