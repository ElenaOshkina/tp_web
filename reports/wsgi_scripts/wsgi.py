from wsgiref.simple_server import make_server

def app(environ, start_response):
  data = "Hello, World   !\nGET parameters:\n"
  # Getting GET params 
  #Returns a dictionary in which the values are lists
  request_params = environ['QUERY_STRING']
  data += parse_params(request_params)

  # Getting POST params
  data += "POST parameters:\n"

  # the environment variable CONTENT_LENGTH may be empty or missing
  try:
      request_body_size = int(environ.get('CONTENT_LENGTH', 0))
  except (ValueError):
      request_body_size = 0

  # When the method is POST the variable will be sent
  # in the HTTP request body which is passed by the WSGI server
  # in the file like wsgi.input environment variable.
  request_body = environ['wsgi.input'].read(request_body_size)
  data += parse_params(request_body)

  # Forming response headers
  status = '200 OK'
  response_headers = [
      ('Content-type','text/plain'),
      ('Content-Length', str(len(data)))
  ]
  start_response(status, response_headers)
  return iter([data])

def parse_params(params):
  res = "";
  for param in params.split('&'):
    res += param + "\n"

  return res

#httpd = make_server('localhost', 8081, app)
#httpd.serve_forever()
