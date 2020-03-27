from flask import Flask, request, jsonify
import transaction_generator
from stream_api import StreamAPI
from stream_config import CONFIG_FILE, SERVICE_ENDPOINT, STREAM_ID

# declare constants for flask app
HOST = '0.0.0.0'
PORT = 5001

# initialize flask application
app = Flask(__name__)

# initialize oci stream api
stream = StreamAPI(CONFIG_FILE, SERVICE_ENDPOINT, STREAM_ID)

def stream_data(orderType, amount):
    for i in range(int(amount)):
        data = transaction_generator.generate_data(orderType)
        publish_response = stream.publish_message(data)
        if publish_response != 0:
            return jsonify(status=400)
    return jsonify(status=201, streamed=amount)

@app.route('/api/v1/publish/test', methods=['POST'])
def publish_test():
    # generate random data
    data = transaction_generator.generate_data('online')
    #publish data to stream
    publish_response = stream.publish_message(data)
    if publish_response == 0:
        return jsonify(status=201, data=data)
    else:
        # return error status
        return jsonify(status=400)

@app.route('/api/v1/publish', methods=['POST','OPTIONS'])
def publish():
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST, OPTIONS',
            'Access-Control-Max-Age': 1000,
            'Access-Control-Allow-Headers': 'origin, x-csrftoken, content-type, accept',
        }
        return '', 200, headers
    # get data from post request
    data = request.get_json()
    if data.keys() >= {'orderType', 'amount'}:
        # return success status and new order
        stream_data(data['orderType'], data['amount'])
        return jsonify(status=201)
    else:
        # return error status
        return jsonify(status=400, error='orderType and amount keys are missing')

if __name__ == '__main__':
    app.run(host=HOST,
            debug=True,
            port=PORT)
