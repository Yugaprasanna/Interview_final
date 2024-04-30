from flask import Flask, request, jsonify
from flask_cors import CORS
from azure.storage.blob import BlobServiceClient
# import speech_recognition as sr
 
app = Flask(__name__)
CORS(app)
 
# Azure Blob Storage connection string
CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=avatarstore0409;AccountKey=VDvHhQ41yKp2rn1TmSvow0DpnEt9sP3XGbpo5ksGbQfonuXIO9EfQOyrDgxNf9ciUNJQpnexRImw+AStGWGgkA==;EndpointSuffix=core.windows.net"
container_name = "test0904"
 
@app.route('/upload', methods=['POST'])
def Videocall():
    try:
        # Get the uploaded file from the request
        file = request.files['file']
 
        # Create a blob service client
        blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
        container_client = blob_service_client.get_container_client(container_name)
 
        # Upload the file to Azure Blob Storage
        blob_client = container_client.upload_blob(name=file.filename, data=file.stream, overwrite=True)
 
        return jsonify({"message": "File uploaded successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})
 
 
if __name__ == '__main__':
    app.run(debug=True)