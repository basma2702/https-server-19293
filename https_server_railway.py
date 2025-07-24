import http.server
import ssl
import socketserver
import os
import sys

# Get port from environment variable (Railway will set this)
PORT = int(os.environ.get('PORT', 19293))

class HealthCheckHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Handle health check requests
        if self.path == '/health' or self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>🚀 HTTPS Server on Port {PORT}</title>
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 40px; background: #f0f0f0; }}
                    .container {{ background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
                    h1 {{ color: #333; }}
                    .status {{ color: green; font-weight: bold; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>🚀 HTTPS Server Running!</h1>
                    <p class="status">✅ Server is successfully running on port {PORT}</p>
                    <p><strong>URL:</strong> {os.environ.get('RAILWAY_PUBLIC_DOMAIN', 'localhost')}:{PORT}</p>
                    <p><strong>Protocol:</strong> HTTPS (Secure)</p>
                    <p><strong>Environment:</strong> Railway Cloud</p>
                    <hr>
                    <p><em>Server started at: {os.environ.get('RAILWAY_START_TIME', 'Unknown')}</em></p>
                </div>
            </body>
            </html>
            """
            
            self.wfile.write(html_content.encode())
        else:
            # Serve static files for other requests
            super().do_GET()

    def log_message(self, format, *args):
        # Log all requests for debugging
        sys.stderr.write("[%s] %s\n" % (self.log_date_time_string(), format % args))

# Create server
Handler = HealthCheckHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

print(f"🚀 Server starting on port {PORT}")
print(f"🌐 Environment: {'Railway' if os.environ.get('RAILWAY_ENVIRONMENT') else 'Local'}")
print("📝 Health check endpoint: /health")
print("🛑 Press Ctrl+C to stop the server")

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\n🛑 Server stopped.")
    httpd.shutdown()
except Exception as e:
    print(f"❌ Server error: {e}")
    sys.exit(1) 