from flask import Flask
import os

app = Flask(__name__)

# Get port from environment variable (Render will set this)
PORT = int(os.environ.get('PORT', 19293))

@app.route('/')
def home():
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>🚀 Basma Alam the great - Render Server</title>
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
            .render-highlight {{ 
                background: #e3f2fd; 
                padding: 15px; 
                border-radius: 8px; 
                margin: 10px 0; 
                border-left: 4px solid #2196f3;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Basma Alam the great</h1>
            <div class="status">
                ✅ Render server running on port {PORT}
            </div>
            <div class="info">
                <p><strong>🌐 Server Type:</strong> Render Cloud Platform</p>
                <p><strong>🔒 Protocol:</strong> HTTPS (Secure)</p>
                <p><strong>🏠 Environment:</strong> Render Free Tier</p>
                <p><strong>⏰ Server Time:</strong> Live</p>
            </div>
            <div class="render-highlight">
                <p><strong>🎯 Port:</strong> {PORT} (Render managed)</p>
                <p><strong>✅ Status:</strong> Remote server - No localhost!</p>
                <p><strong>🌍 Access:</strong> Available worldwide</p>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/health')
def health():
    return {
        'status': 'healthy', 
        'port': PORT,
        'platform': 'Render',
        'message': f'Render server running on port {PORT}'
    }, 200

@app.route('/port')
def port_info():
    return {
        'port': PORT,
        'platform': 'Render',
        'free_tier': True
    }, 200

if __name__ == '__main__':
    print(f"🚀 Starting Render server on port {PORT}")
    print(f"🌐 Platform: Render Cloud")
    print(f"🎯 Port {PORT}: Configured!")
    print(f"📝 Health check: /health")
    print(f"📊 Port info: /port")
    
    app.run(host='0.0.0.0', port=PORT, debug=False) 