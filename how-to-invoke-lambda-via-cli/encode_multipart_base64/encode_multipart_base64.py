import urllib3
from base64 import b64encode


def encode_csv_as_multipart(file_path, field_name='file', custom_boundary='----WebKitFormBoundaryRSqJpulfCtjoOsXB'):
    # Open the CSV file and read its content
    with open(file_path, 'r') as file:
        file_data = file.read()

    # Create a dictionary with the file data
    files = {field_name: ('file.csv', file_data, 'text/csv')}

    # Encode the file as multipart form data
    encoder = urllib3.encode_multipart_formdata(files, boundary=custom_boundary)
    a = encoder[0]
    b = encoder[1]
    # Convert the request body to Base64
   # decoded_string = a.encode()
    # converting
  #  output = a.decode()
    request_body_base64 =  b64encode(a)
    # Return the Content-Type header and the encoded request body
    return request_body_base64


if __name__ == "__main__":
    csv_file_path = 'path/to/your/file.csv'
    request_body = encode_csv_as_multipart(csv_file_path)

    # Print the Content-Type header and the encoded request body
    print("\nRequest Body:", request_body.decode('utf-8'))
