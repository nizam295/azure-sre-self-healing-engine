from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import json

class RemediationHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))
        
        print(f"[SRE-ENGINE] Incoming alert webhook detected from Grafana! State: {data.get('status')}")
        
        if data.get('status') == 'firing':
            print("[CRITICAL] Application fault threshold crossed! Initiating self-healing protocol...")
            try:
                # Triggers docker to automatically restart your application container dynamically
                subprocess.run(["docker", "restart", "monitoring-stack_app-node_1"], check=True)
                print("[SUCCESS] Application container successfully restarted and restored to a healthy state!")
            except Exception as e:
                print(f"[FAILURE] Automated remediation failed: {str(e)}")
                
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(b'{"status":"processed"}')

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 5001), RemediationHandler)
    print("[SRE-ENGINE] Self-healing endpoint listening on port 5001...")
    server.serve_forever()
