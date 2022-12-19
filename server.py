import http.server
import socketserver

PORT = 8099

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Server started at localhost:{PORT}")
    httpd.serve_forever()