#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class HTTPserver(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            json_response  = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(json_response).encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            json_response  = {b"OK"}
            self.wfile.write(json.dumps(json_response).encode("utf-8"))

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            json_response  = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(json_response).encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error_response = {b"Endpoint not found"}
            self.wfile.write(json.dumps(error_response).encode("utf-8"))

def run_server(port=8000):
    server_address = ("", port)
    httpd = HTTPServer(server_address, HTTPserver)
    print("Server running on http://localhost:{}".format(port))
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()