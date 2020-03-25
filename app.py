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

@app.route('/api/v1/publish', methods=['POST'])
def publish():
    # generate random data
    data = transaction_generator.generate_data()
    #publish data to stream
    publish_response = stream.publish_message(data)
    if publish_response == 0:
        return jsonify(status=201, data=data)
    else:
        # return error status
        return jsonify(status=400)


if __name__ == '__main__':
    app.run(host=HOST,
            debug=True,
            port=PORT)
