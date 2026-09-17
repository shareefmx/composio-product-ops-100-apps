#!/usr/bin/env python3
"""
Main CLI Orchestration Entrypoint for Composio AI Product Ops Assignment.
Provides single-command research execution, verification checks, data exports,
and a local preview server for the single-page interactive case study.
"""

import sys
import os
import argparse
import http.server
import socketserver
import webbrowser

# Add current workspace directory to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from assignment.agent.researcher import ComposioResearchAgent
from assignment.agent.export import export_all_artifacts
from assignment.agent.verifier import run_full_verification


def start_server(port: int = 8080, open_browser: bool = True):
    web_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "web"))
    os.chdir(web_dir)

    class QuietHandler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, format, *args):
            # Suppress noisy logs
            pass

    print(f"\n=======================================================")
    print(f"  COMPOSIO PRODUCT OPS CASE STUDY SERVER RUNNING")
    print(f"  Serving directory: {web_dir}")
    print(f"  URL: http://localhost:{port}")
    print(f"  Press Ctrl+C to stop the server.")
    print(f"=======================================================\n")

    if open_browser:
        try:
            webbrowser.open(f"http://localhost:{port}")
        except Exception:
            pass

    with socketserver.TCPServer(("", port), QuietHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[!] Server stopped.")


def main():
    parser = argparse.ArgumentParser(description="Composio AI Product Ops 100-App Research Toolkit")
    parser.add_argument("--all", action="store_true", help="Run research agent across all 100 applications")
    parser.add_argument("--verify", action="store_true", help="Execute multi-pass verification benchmark")
    parser.add_argument("--export", action="store_true", help="Export latest JSON and CSV datasets")
    parser.add_argument("--serve", action="store_true", help="Start local HTTP server for interactive HTML dashboard")
    parser.add_argument("--port", type=int, default=8080, help="Port for local HTTP server (default: 8080)")

    args = parser.parse_args()

    if args.export:
        print("[*] Exporting datasets and analysis...")
        export_all_artifacts()
    elif args.verify:
        print("[*] Running automated verification loop...")
        report = run_full_verification()
        prog = report["progression"]
        print(f"\n[✓] Verification Completed:")
        print(f"    - Pass 1 Raw Accuracy: {prog['pass1_accuracy_pct']}%")
        print(f"    - Pass 2 Heuristics Accuracy: {prog['pass2_accuracy_pct']}%")
        print(f"    - Pass 3 Human Golden Audit: {prog['pass3_accuracy_pct']}%")
        print(f"    - Accuracy Gain: +{prog['gain_from_verification_pct']}%")
    elif args.all:
        agent = ComposioResearchAgent()
        agent.run_batch()
    elif args.serve:
        start_server(port=args.port)
    else:
        # Default behavior: run quick sample and offer instructions
        print("===============================================================")
        print("  Composio AI Product Ops Intern Take-Home Research Engine")
        print("===============================================================")
        print("\nAvailable commands:")
        print("  python assignment/run.py --serve   # Launch interactive case study dashboard in browser")
        print("  python assignment/run.py --all     # Execute research agent across all 100 apps")
        print("  python assignment/run.py --verify  # Run automated verification benchmarks")
        print("  python assignment/run.py --export  # Re-generate JSON & CSV data files")
        print("\nRunning quick agent verification run on 3 sample apps:\n")
        agent = ComposioResearchAgent()
        agent.run_batch(limit=3)


if __name__ == "__main__":
    main()
