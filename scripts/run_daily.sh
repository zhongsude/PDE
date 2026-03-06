#!/bin/bash
echo "Starting PDE daily tasks..."
python backend/main.py
python analysis/run_analysis.py
python analysis/generate_report.py
