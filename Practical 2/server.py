from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client 
import os

def upload(filename, file_data):
    try:
        with open(filename,"wb") as file:
            file.write(file_data.data)
        return f"File {filename} uploaded successfully!"
    except Exception as e:
        return "Error"
    
def download(filename):
    try:
        if os.path.exists(filename):
            with open(filename,"rb") as file:
                file_data = file.read()
            return xmlrpc.client.Binary(file_data)
        else:
            return "File not found"
    except Exception as e:
        return "Error"

if __name__ == "__main__":
    server = SimpleXMLRPCServer(("127.0.0.1", 8080))
    print("Server is running on port 8080...")

    server.register_function(upload, "upload")
    server.register_function(download, "download")
    print("Registered method: UPLOAD, DOWNLOAD")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Server stopped.")