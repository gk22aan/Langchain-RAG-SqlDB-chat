from flask import Flask, jsonify
from ChatSQL import ChatWithSql
app = Flask(__name__)
obj = ChatWithSql("root","12345","127.0.0.1","student_grade")
@app.route('/send-message', methods=['GET'])
def send_message():
    # message = "Hello, this is a message from the Flask API!"
    message = obj.message("How many rows do we have in names table ?")
    return jsonify({"message": message})

if __name__ == '__main__':
    app.run(debug=True)