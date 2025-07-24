from flask import Flask, render_template_string
import os

app = Flask(__name__)

# Get port from environment variable
PORT = int(os.environ.get('PORT', 19293))

@app.route('/')
def home():
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>🚀 HTTPS Server on Port {PORT}</title>
        <style>
            body {{ 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                margin: 0; 
                padding: 0; 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }}
            .container {{ 
                background: white; 
                padding: 40px; 
                border-radius: 20px; 
                box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                text-align: center;
                max-width: 600px;
                margin: 20px;
            }}
            h1 {{ color: #333; margin-bottom: 20px; font-size: 2.5em; }}
            .status {{ 
                background: #4CAF50; 
                color: white; 
                padding: 15px; 
                border-radius: 10px; 
                margin: 20px 0; 
                font-weight: bold; 
            }}
            .info {{ 
                background: #f8f9fa; 
                padding: 20px; 
                border-radius: 10px; 
                margin: 20px 0; 
                text-align: left; 
            }}
            .info strong {{ color: #007bff; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 HTTPS Server Running!</h1>
            <div class="status">
                ✅ Server is successfully running on port {PORT}
            </div>
            <div class="info">
                <p><strong>🌐 URL:</strong> {os.environ.get('RAILWAY_PUBLIC_DOMAIN', 'localhost')}</p>
                <p><strong>🔒 Protocol:</strong> HTTPS (Secure)</p>
                <p><strong>📡 Port:</strong> {PORT}</p>
                <p><strong>🏠 Environment:</strong> Railway Cloud</p>
                <p><strong>⏰ Server Time:</strong> {os.environ.get('RAILWAY_START_TIME', 'Live')}</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html

@app.route('/health')
def health():
    return {'status': 'healthy', 'port': PORT}, 200

if __name__ == '__main__':
    print(f"🚀 Starting Flask server on port {PORT}")
    print(f"🌐 Environment: {'Railway' if os.environ.get('RAILWAY_ENVIRONMENT') else 'Local'}")
    print("📝 Health check endpoint: /health")
    app.run(host='0.0.0.0', port=PORT, debug=False) 