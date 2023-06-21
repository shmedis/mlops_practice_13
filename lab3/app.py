from flask import Flask, request
import hashlib

app = Flask(__name__)

@app.route('/hash', methods=['POST'])
def hash_string():
    data = request.get_json()
    string_to_hash = data['string']
    
    hashed_string = hashlib.sha256(string_to_hash.encode()).hexdigest()
    
    return {'hashed_string': hashed_string}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)