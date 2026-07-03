#!/usr/bin/env python3
"""
Server locale per testare TWA.
Avvia con: python3 serve.py
Poi apri http://<IP_MAC>:8080 dal tablet.
"""
import http.server
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

server = http.server.HTTPServer(("0.0.0.0", 8080), http.server.SimpleHTTPRequestHandler)
print("Server avviato su http://0.0.0.0:8080")
print("Ctrl+C per fermare")
server.serve_forever()
