import http.server
import socketserver
from pathlib import Path

PORT = 8000


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=".", **kwargs)

    def translate_path(self, path):
        path = super().translate_path(path)
        if not Path(path).exists():
            if Path(path + ".html").exists():
                path += ".html"
        return path
    
    def send_error(self, code, message=None, explain=None):
        if code == 404:
            self.error_message_format_default = self.error_message_format
            self.error_message_format = Path("404.html").read_text(encoding="utf-8")
        super().send_error(code, message, explain)
        if code == 404:
            self.error_message_format = self.error_message_format_default


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
