from quart import Quart, render_template, request
#Creating a quart instancy named app
app = Quart (__name__)

# Main app route
@app.get('/')
async def home():
    return await render_template('home.html')

# About us
@app.get('/about')   
async def about():
    return await render_template('about.html')

# Contact
@app.get('/contact')
async def contact():
    return await render_template('contact.html')

# Greetings with name using query string
@app.get('/hello')
async def greetings():
    name = request.args.get('name')  # Get name parameter from the URL
    return await render_template('hello.html', name=name)

# Product by ID using rute parameters
@app.get('/products/<int:product_id>')
async def products(product_id):
    return f"El id del producto que buscas es: {product_id}"


# To run the server
if __name__ == '__main__':
    app.run(debug=True)
