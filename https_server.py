import http.server
import ssl
import socketserver
import os

# Create self-signed certificate if it doesn't exist
def create_self_signed_cert():
    if not os.path.exists('server.crt') or not os.path.exists('server.key'):
        print("Creating self-signed certificate...")
        os.system('openssl req -x509 -newkey rsa:4096 -keyout server.key -out server.crt -days 365 -nodes -subj "/C=US/ST=State/L=City/O=Organization/CN=localhost"')
        print("Certificate created successfully!")

# Create certificate
create_self_signed_cert()

# Server configuration
PORT = 19293
Handler = http.server.SimpleHTTPRequestHandler

# Create HTTP server
httpd = socketserver.TCPServer(("", PORT), Handler)

# Wrap socket with SSL
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('server.crt', 'server.key')
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print(f"HTTPS Server running on https://localhost:{PORT}")
print("Note: You'll see a security warning in your browser due to self-signed certificate")
print("Press Ctrl+C to stop the server")

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")
    httpd.shutdown() 