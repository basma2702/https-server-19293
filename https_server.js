const https = require('https');
const fs = require('fs');
const path = require('path');

// Create self-signed certificate if it doesn't exist
function createSelfSignedCert() {
    const { execSync } = require('child_process');
    
    if (!fs.existsSync('server.crt') || !fs.existsSync('server.key')) {
        console.log('Creating self-signed certificate...');
        try {
            execSync('openssl req -x509 -newkey rsa:4096 -keyout server.key -out server.crt -days 365 -nodes -subj "/C=US/ST=State/L=City/O=Organization/CN=localhost"', { stdio: 'inherit' });
            console.log('Certificate created successfully!');
        } catch (error) {
            console.log('OpenSSL not found. Please install OpenSSL or use existing certificates.');
            console.log('You can generate certificates manually using:');
            console.log('openssl req -x509 -newkey rsa:4096 -keyout server.key -out server.crt -days 365 -nodes -subj "/C=US/ST=State/L=City/O=Organization/CN=localhost"');
            process.exit(1);
        }
    }
}

// Create certificate
createSelfSignedCert();

// SSL options
const options = {
    key: fs.readFileSync('server.key'),
    cert: fs.readFileSync('server.crt')
};

// Create HTTPS server
const server = https.createServer(options, (req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end(`
        <!DOCTYPE html>
        <html>
        <head>
            <title>HTTPS Server on Port 19293</title>
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
                <p class="status">✅ Server is successfully running on port 19293</p>
                <p><strong>URL:</strong> https://localhost:19293</p>
                <p><strong>Protocol:</strong> HTTPS (Secure)</p>
                <p><strong>Certificate:</strong> Self-signed (you may see a security warning)</p>
                <hr>
                <p><em>Server started at: ${new Date().toLocaleString()}</em></p>
            </div>
        </body>
        </html>
    `);
});

const PORT = 19293;

server.listen(PORT, () => {
    console.log(`🌐 HTTPS Server running on https://localhost:${PORT}`);
    console.log('⚠️  Note: You\'ll see a security warning in your browser due to self-signed certificate');
    console.log('🛑 Press Ctrl+C to stop the server');
});

// Handle graceful shutdown
process.on('SIGINT', () => {
    console.log('\n🛑 Server stopped.');
    server.close(() => {
        process.exit(0);
    });
}); 