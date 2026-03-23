from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Shopping cart stored in memory
cart_list = []

@app.route('/')
def index():
    return render_template('index.html', cart=cart_list, total=len(cart_list))

@app.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if item:
        cart_list.append(item)
    return redirect(url_for('index'))

@app.route('/remove', methods=['POST'])
def remove_item():
    item = request.form.get('item')
    if item in cart_list:
        cart_list.remove(item)
    return redirect(url_for('index'))

@app.route('/clear')
def clear_cart():
    cart_list.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)