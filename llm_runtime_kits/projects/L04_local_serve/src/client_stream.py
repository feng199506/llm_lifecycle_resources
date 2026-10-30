#!/usr/bin/env python3
import json
import urllib.request

body = json.dumps({"messages": [{"role": "user", "content": "ping"}], "stream": True}).encode()
req = urllib.request.Request("http://127.0.0.1:8090/v1/chat/completions", data=body, headers={"Content-Type": "application/json"})
with urllib.request.urlopen(req, timeout=30) as resp:
    for line in resp:
        print(line.decode(), end="")
