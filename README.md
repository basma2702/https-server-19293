# 🚀 HTTPS Server on Port 19293

A simple HTTPS server that runs on port 19293, ready for cloud deployment.

## 📁 Files

- `https_server_cloud.py` - Main server file (cloud-ready)
- `https_server.py` - Original local HTTPS server
- `https_server.js` - Node.js version
- `index.html` - Web page served by the server
- `Procfile` - Heroku deployment configuration
- `railway.json` - Railway deployment configuration
- `requirements.txt` - Python dependencies

## 🌐 Cloud Deployment Options

### Option 1: Railway (Recommended - Easiest)

1. **Sign up** at [railway.app](https://railway.app)
2. **Connect** your GitHub account
3. **Create** a new project
4. **Deploy** from GitHub repository

### Option 2: Heroku

1. **Install** Heroku CLI
2. **Login** to Heroku:
   ```bash
   heroku login
   ```
3. **Create** a new app:
   ```bash
   heroku create your-app-name
   ```
4. **Deploy**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push heroku main
   ```

### Option 3: Render

1. **Sign up** at [render.com](https://render.com)
2. **Connect** your GitHub account
3. **Create** a new Web Service
4. **Deploy** from GitHub repository

## 🏠 Local Development

### Python Version
```bash
python https_server_cloud.py
```

### Node.js Version
```bash
node https_server.js
```

## 🔧 Configuration

- **Port**: 19293 (configurable via PORT environment variable)
- **Protocol**: HTTPS (local) / HTTP (cloud with SSL termination)
- **SSL**: Self-signed certificates for local development

## 📝 Notes

- Cloud platforms automatically provide SSL certificates
- The server automatically detects cloud vs local environment
- Port 19293 will be used when available, otherwise platform-assigned port

## 🚀 Access Your Server

- **Local**: https://localhost:19293
- **Cloud**: Your platform URL (e.g., your-app.railway.app) 