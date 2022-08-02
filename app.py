from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

# # client = MongoClient('localhost', 27017)
# client = MongoClient('mongodb://test:test@localhost', 27017)
# db = client.dbsparta


from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.1gnz510.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

from datetime import datetime

#
# @app.route('/')
# # def home():
# #     return render_template('index.html')


@app.route('/upload', methods=['GET'])
def show_upload():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def save_upload():

    title_receive = request.form['title_give']
    content_receive = request.form['content_give']
    category_receive = request.form['category_give']
    price_receive = request.form['price_give']
    num_receive = request.form['num_give']

    file = request.files["file_give"]

    extension = file.filename.split('.')[-1]
    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')

    filename = f'file--{mytime}'

    save_to = f'static/{filename}.{extension}'
    file.save(save_to)

    doc = {

        'title': title_receive,
        'content': content_receive,
        'category': category_receive,
        'price': price_receive,
        'num': num_receive,
        'file': f'{filename}.{extension}'
    }

    db.upload.insert_one(doc)

    print(title_receive,content_receive,category_receive,price_receive,num_receive)

    return jsonify({'msg': ' 작성 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
