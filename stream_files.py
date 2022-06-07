import sys
import http.server
import socketserver

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = "." + self.path
        print(self.path)
        
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

handler_object = MyHttpRequestHandler

PORT = 7000
my_server = socketserver.TCPServer(("", PORT), handler_object)

try:
    my_server.serve_forever()
except KeyboardInterrupt:
    pass
my_server.server_close()