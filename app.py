from flask import Flask, jsonify, request
import hashlib

VERIFICATION_TOKEN = 'PEHNqXDasD9emSeGQmSX2Tb_Q5FYnGG-mpPXwXTKuna_rHzmPmbvsWzN'
ENDPOINT = 'https://ec2-54-200-99-38.us-west-2.compute.amazonaws.com/'

app = Flask(__name__)


@app.route('/ebay-delete-closure')
def challenge_code_verification():
    challenge_code = request.args.get('challenge_code')
    challenge_code = challenge_code + VERIFICATION_TOKEN + ENDPOINT
    challenge_code = challenge_code.encode('utf-8')
    challenge_code = hashlib.sha256(challenge_code)
    challenge_code = challenge_code.hexdigest()
    verification = {"challengeResponse": challenge_code}
    return jsonify(verification), 200

if __name__ == '__main__':
    app.run(debug=True)
