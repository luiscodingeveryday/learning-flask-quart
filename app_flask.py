from flask import Flask, request, render_template
# Creating a flask instancy named app
app = Flask(__name__)

# Main app route
@app.route ('/')
def home():
    return render_template('home.html')
    
# About us
@app.route ('/about')   
def about():
    return render_template('about.html')

# Contact
@app.route ('/contact')
def contact():
    return render_template('contact.html')

# Greetings with name using query string
@app.route('/hello')
def greetings():
    name = request.args.get('name')  # Get name parameter from the URL
    return render_template('hello.html', name=name)

# Product by ID using rute parameters
@app.route('/products/<int:product_id>')
def products(product_id): # Get id parameter from the URL
    return f"El id del producto que buscas es: {product_id}"

# To run the server
if __name__ == '__main__':
    app.run(debug=True)
    
