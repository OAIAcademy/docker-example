import os
from http.server import BaseHTTPRequestHandler, HTTPServer

import requests

hostName = "0.0.0.0"
serverPort = int(os.environ.get("PORT", 80))


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(requests.get(os.environ.get("FRONT_URL")).content))


if __name__ == "__main__":

    print(os.environ.get("FRONT_URL"))
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
