import http.server
import ssl
import socketserver
import os
from urllib.parse import urlparse

# Get port from environment variable (for cloud platforms) or use default
PORT = int(os.environ.get('PORT', 19293))

# Create self-signed certificate if it doesn't exist
def create_self_signed_cert():
    if not os.path.exists('server.crt') or not os.path.exists('server.key'):
        print("Creating self-signed certificate...")
        try:
            os.system('openssl req -x509 -newkey rsa:4096 -keyout server.key -out server.crt -days 365 -nodes -subj "/C=US/ST=State/L=City/O=Organization/CN=localhost"')
            print("Certificate created successfully!")
        except:
            print("Could not create certificate automatically. Using HTTP instead.")
            return False
    return True

# Check if we're in a cloud environment
is_cloud = os.environ.get('RAILWAY_ENVIRONMENT') or os.environ.get('HEROKU_APP_NAME') or os.environ.get('VERCEL')

if is_cloud:
    print(f"🌐 Cloud deployment detected! Using port: {PORT}")
    # In cloud environments, we'll use HTTP (they provide SSL termination)
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), Handler)
    print(f"🚀 HTTP Server running on port {PORT}")
    print("📝 Note: SSL is handled by the cloud platform")
else:
    # Local development with HTTPS
    if create_self_signed_cert():
        Handler = http.server.SimpleHTTPRequestHandler
        httpd = socketserver.TCPServer(("", PORT), Handler)
        
        # Wrap socket with SSL
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain('server.crt', 'server.key')
        httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
        print(f"🔒 HTTPS Server running on https://localhost:{PORT}")
    else:
        # Fallback to HTTP
        Handler = http.server.SimpleHTTPRequestHandler
        httpd = socketserver.TCPServer(("", PORT), Handler)
        print(f"🌐 HTTP Server running on http://localhost:{PORT}")

print("🛑 Press Ctrl+C to stop the server")

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\n🛑 Server stopped.")
    httpd.shutdown() 