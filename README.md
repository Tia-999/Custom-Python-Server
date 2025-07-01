# 🖥️ Simple Python HTTP Server

This is a basic HTTP server built using Python's `http.server` module. It handles both `GET` and `POST` requests on a custom IP and port.

## 📌 Features

- Handles `GET` requests and responds with a fun HTML message.
- Handles `POST` requests and returns the current server time in JSON format.
- Easily extendable for more request types like PUT, DELETE, etc.

## 🚀 How to Run

### 1. Make sure you're on the same local network.
Edit the `HOST` in the Python file to your local IP address (e.g. `192.168.x.x`).  
You can find it by running:

```bash
ipconfig (on Windows)
ifconfig (on macOS/Linux)
