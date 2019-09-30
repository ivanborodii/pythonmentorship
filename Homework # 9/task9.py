import cgi, base64
from wsgiref.simple_server import make_server
from functools import partial

def dispatch(routes, default_route, environ, start_response):
    path = environ['PATH_INFO']
    params = cgi.FieldStorage(environ['wsgi.input'],
                              environ=environ)
    method = environ['REQUEST_METHOD'].lower()
    environ['params'] = params
    handler = routes.get((method, path), default_route)
    return handler(environ, start_response)

def compile_routes(routes_list):
    return dict([
        ((method, path), handler)
        for method, path, handler in routes_list]
    )

def notfound_404(environ, start_response):
    start_response('404 Not Found', [('Content-type', 'text/plain')])
    return [b'Not Found']

def image_load(environ, start_response): # was created this fuction for showing an image on the home page of localhost
    try:
        start_response('200 OK', [('Content-type', 'text/html')])
        img_url = base64.b64encode(open(r"angry_rocket.jpg","rb").read()).decode('utf-8')
        _image_resp = (
            """   <html>
                       <head>
                         <title>Advanced task #9</title>
                       </head>
                       <body>
                        <center><img src="data:image/jpg;base64,{}" /></center>
                       </body>
                 </html>""".format(img_url))
        yield _image_resp.encode('utf-8')
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    try:
        routes = [('get', '/', image_load)]
        # Создаем диспетчер и регистрируем функции
        dispatcher = partial(
            dispatch,
            compile_routes(routes),
            notfound_404)
        # Запускаем базовый сервер
        httpd = make_server('', 8080, dispatcher)
        print('Serving on port 8080...')
        httpd.serve_forever()
    except Exception as e:
        print(str(e))

