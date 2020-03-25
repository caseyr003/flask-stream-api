import oci
from base64 import b64decode, b64encode

class StreamAPI:
    def __init__(self, config_file, service_endpoint, stream_id):
        # Configure OCI Config
        config = oci.config.from_file(config_file)
        # Create stream client
        self.stream_client = oci.streaming.StreamClient(config, service_endpoint)
        self.stream_id = stream_id

    def publish_message(self, data):
        # Pushes data to stream
        # Data should be in json format
        value = b64encode(bytes(data, 'utf-8')).decode('utf-8')
        entry = oci.streaming.models.PutMessagesDetailsEntry(value=value)
        put_message_details = oci.streaming.models.PutMessagesDetails(messages=[entry])
        response = self.stream_client.put_messages(self.stream_id, put_message_details)
        return response.data.failures
