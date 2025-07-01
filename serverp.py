from http.server import HTTPServer,BaseHTTPRequestHandler
HOST = "192.168.0.120"
PORT = 9999
class MyHTTPServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><body><h1>THIS IS TIA'S SERVER HAHAHAHAHA </h1></body></html>","utf-8"))

server = HTTPServer((HOST,PORT),MyHTTPServer)
print(f"Server now running......")
server.serve_forever()
server.close()
print(f"Server Stopped......")