# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request
from main import *
# creating a Flask app
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods=['GET'])
def home():
    if (request.method == 'GET'):
        data = "You've wandered to an interesting part of the internet"
        return jsonify({'data': data})



@app.route('/<string:stock_name>/<string:disc_type>', methods=['GET'])
def displll(stock_name,disc_type):
    driver = initialize(stock_name)
    new_comments(driver,disc_type)
    a = get_comments(driver)
    return jsonify({'data': a})

@app.route('/<string:stock_name>/<string:disc_type>/replies', methods=['GET'])
def dispel(stock_name,disc_type):
    driver = initialize(stock_name)
    new_comments(driver,disc_type)
    get_replies(driver)
    a = get_comments(driver)
    return jsonify({'data': a})


@app.route('/<string:stock_name>/<string:disc_type>/show/<int:show>', methods=['GET'])
def disspl(stock_name,disc_type,show):
    driver = initialize(stock_name)
    new_comments(driver,disc_type)
    show_more(driver, show)
    a = get_comments(driver)
    return jsonify({'data': a})


@app.route('/<string:stock_name>/<string:disc_type>/show/<int:show>/replies', methods=['GET'])
def disfpl(stock_name,disc_type,show):
    driver = initialize(stock_name)
    new_comments(driver,disc_type)
    show_more(driver, show)
    get_replies(driver)
    a = get_comments(driver)
    return jsonify({'data': a})





@app.route('/<string:stock_name>/<string:disc_type>/lim/<int:limit>', methods=['GET'])
def displell(stock_name,disc_type,limit):
    driver = initialize(stock_name)
    new_comments(driver,disc_type)
    a = get_comments(driver,limit)
    return jsonify({'data': a})


@app.route('/<string:stock_name>/<string:disc_type>/replies/lim/<int:limit>', methods=['GET'])
def diespel(stock_name,disc_type,limit):
    driver = initialize(stock_name)
    new_comments(driver,disc_type)
    get_replies(driver)
    a = get_comments(driver,limit)
    return jsonify({'data': a})


@app.route('/<string:stock_name>/<string:disc_type>/show/<int:show>/lim/<int:limit>', methods=['GET'])
def diseespl(stock_name,disc_type,show,limit):
    driver = initialize(stock_name)
    new_comments(driver,disc_type)
    show_more(driver, show)
    a = get_comments(driver,limit)
    return jsonify({'data': a})


@app.route('/<string:stock_name>/<string:disc_type>/show/<int:show>/replies/lim/<int:limit>', methods=['GET'])
def disfeeepl(stock_name,disc_type,show,limit):
    driver = initialize(stock_name)
    new_comments(driver,disc_type)
    show_more(driver, show)
    get_replies(driver)
    a = get_comments(driver,limit)
    return jsonify({'data': a})



# driver function
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)