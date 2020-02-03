from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if (request.method== 'POST'):
        add_json = request.get_json()
        return jsonify ({"sent": add_json}), 201
    else:
        return jsonify ({"company": "{{ company_name }}"})

@app.route('/prime/<int:num>', methods=['GET'])
def get_prime(num):
    if num>1:
        for i in range(2,num):
            if (num % i)== 0:
                return jsonify({"result": "this number is not prime"})
                break
        else:
            return jsonify({"result":"this number is prime"})
    else:
        return jsonify({"result":"this number is not prime"})


if __name__ == "__name__":
    app.run(host="0.0.0.0", port=5000, reloader=True, debug=True)
