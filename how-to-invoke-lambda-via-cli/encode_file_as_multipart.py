import urllib3

def encode_file_as_multipart(file_path, field_name='file'):
    # Open the file and read its content
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Create a dictionary with the file data
    files = {field_name: (file_path, file_data)}

    # Encode the file as multipart form data
    encoder = urllib3.encode_multipart_formdata(files)
    
    # Return the Content-Type header and the encoded request body
    return encoder.content_type, encoder.request_body

if __name__ == "__main__":
    file_path = 'path/to/your/file.txt'
    content_type, request_body = encode_file_as_multipart(file_path)

    # Print the Content-Type header and the encoded request body
    print("Content-Type:", content_type)
    print("\nRequest Body:", request_body.decode('utf-8'))
