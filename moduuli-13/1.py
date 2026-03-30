from flask import Flask, jsonify

app = Flask(__name__)


def is_prime(luku):
    if luku > 1:
        for i in range(2, luku):
            if luku % i == 0:
                return False
        else:
            return True
    else:
        return False


@app.route('/alkuluku/<int:luku>', methods=['GET'])
def check_prime(luku):
    return jsonify({"Number": luku, "isPrime": is_prime(luku)})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)