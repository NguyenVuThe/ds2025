import xmlrpc.client 

def upload(server_url, file_path, remote_filename):
    try:
        with open(file_path, "rb") as file:
            file_data = file.read()

        proxy = xmlrpc.client.ServerProxy(server_url)

        response = proxy.upload(remote_filename, xmlrpc.client.Binary(file_data))
        return response
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return "Error"
    
def download(server_url, remote_filename, local_filename):
    try:
        proxy = xmlrpc.client.ServerProxy(server_url)

        file_data = proxy.download(remote_filename)

        if isinstance(file_data, xmlrpc.client.Binary):
            with open(local_filename, "wb") as file:
                file.write(file_data.data)
            return "File {remote_filename} downloaded succesfully as {local_filename}"
        else:
            return file_data
    except Exception as e:
        return "Error"
    
if __name__ == "__main__":
    server_url = "http://127.0.0.1:8080/"

    file_path = "client_file.txt"

    remote_filename = "upload_file.txt"

    download_filename = "download_file.txt"

    upload_response = upload(server_url, file_path, remote_filename)
    print(upload_response)

    download_response = download(server_url, remote_filename, download_filename)

