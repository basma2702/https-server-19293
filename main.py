from flask import Flask
import os

app = Flask(__name__)

# Get port from environment variable
PORT = int(os.environ.get('PORT', 19293))

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>🚀 HTTPS Server Running!</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #f0f0f0; }
            .container { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            h1 { color: #333; }
            .status { color: green; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 HTTPS Server Running!</h1>
            <p class="status">✅ Server is successfully running on port ''' + str(PORT) + '''</p>
            <p><strong>URL:</strong> ''' + os.environ.get('RAILWAY_PUBLIC_DOMAIN', 'localhost') + '''</p>
            <p><strong>Protocol:</strong> HTTPS (Secure)</p>
            <p><strong>Environment:</strong> Railway Cloud</p>
        </div>
    </body>
    </html>
    '''

@app.route('/health')
def health():
    return {'status': 'healthy', 'port': PORT}, 200

if __name__ == '__main__':
    print(f"🚀 Starting Flask server on port {PORT}")
    print(f"🌐 Environment: {'Railway' if os.environ.get('RAILWAY_ENVIRONMENT') else 'Local'}")
    app.run(host='0.0.0.0', port=PORT, debug=False) 