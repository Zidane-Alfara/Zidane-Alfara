from flask import Flask, request, jsonify
from flask_cors import CORS
from db import create_table_news
import news_models
from flask_bcrypt import Bcrypt
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
CORS(app)

user = HTTPBasicAuth()
auth = HTTPBasicAuth()
bcrypt = Bcrypt(app)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def check():
    ver_password = bcrypt.generate_password_hash('admin').decode('utf-8')

    return str(ver_password)

@app.route('/auth/<username>')
def check_password(hash_password, password):
    return bcrypt.check_password_hash(hash_password, password)


@auth.verify_password
def authentication(username, password):

    ver_password = bcrypt.generate_password_hash('admin').decode('utf-8')

    dehash_password = check_password(ver_password, password)

    if username and password:
        if username == 'admin' and dehash_password:
            return True
        else:
            return False

    return False

@user.verify_password
def authentication(username, password):

    ver_password = bcrypt.generate_password_hash('user').decode('utf-8')

    dehash_password = check_password(ver_password, password)

    if username and password:
        if username == 'user' and dehash_password:
            return True
        else:
            return False

    return False

@app.route('/news', methods=['GET'])
def get_news():
    result = news_models.get_news()
    
    data = {
            
            'status': 200,
            'data': result
        
        }
    
    resp = jsonify(data)
    resp.status_code = 200
    
    return resp


@app.route('/news/<news_id>', methods=['GET'])
@auth.login_required
def get_news_by_id(news_id):
    try:
        result = news_models.get_news_by_id(news_id)
        data = {
                
                'status': 200,
                'data': result
            
            }
        
        resp = jsonify(data)
        resp.status_code = 200
        
        return resp
    except:
        data = {
                
                'status': 404,
                'message': "Data Not Found"
            
            }
        
        resp = jsonify(data)
        resp.status_code = 404
        
        return resp


@app.route('/news', methods=['POST'])
@auth.login_required
def insert_news():
    
    news_details = request.json
    title = news_details['title']
    content = news_details['content']
    datetime = news_details['datetime']
    flag = news_details['flag']
    result = news_models.insert_news(title, content, datetime, flag)
    
    data = {
        
            'status': 201,
            'message': 'Success!'
        
        }
    
    resp = jsonify(data)
    resp.status_code = 201
    
    return resp


@app.route('/news/<news_id>', methods=['PUT'])
@auth.login_required
def update_news(news_id):
    
    news_details = request.json
    news_id = news_details['news_id']
    title = news_details['title']
    content = news_details['content']
    datetime = news_details['datetime']
    flag = news_details['flag']
    result = news_models.update_news(news_id, title, content, datetime, flag)
    
    data = {
        
            'status': 200,
            'message': 'Success!'
        
        }
    
    resp = jsonify(data)
    resp.status_code = 200
    
    return resp


@app.route('/news/<news_id>', methods=['PATCH'])
@user.login_required
def patch_news(news_id):
    news_details = request.json
    news_id = news_details['news_id']
    flag = news_details['flag']
    result = news_models.patch_news(news_id, flag)

    data = {

        'status': 200,
        'message': 'Success!'

    }

    resp = jsonify(data)
    resp.status_code = 200

    return resp

@app.route('/news/<news_id>', methods=['DELETE'])
@auth.login_required
def delete_news(news_id):
    result = news_models.delete_news(news_id)
    
    data = {
            
            'status': 200,
            'message': "Success!"
        
        }
    
    resp = jsonify(data)
    resp.status_code = 200
    
    return resp


@app.errorhandler(404)
def not_found(error=None):
    message = {
        
            'status': 404,
            'message': 'Not Found: ' + request.url
        }
    
    resp = jsonify(message)
    resp.status_code = 404
    
    return resp


if __name__ == "__main__":
    #create_table_news()
    #print(get_data())
    app.run(debug=True)