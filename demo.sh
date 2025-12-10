#doitlive shell: /bin/bash
#doitlive prompt: {user}@carangos-sa {dir}$

# Carangos S/A - Live Demonstration Script
# This script demonstrates the automated testing system

# First, let's see what we have
ls -la

# Check the project structure
tree -L 2

# Install dependencies
pip install -r requirements.txt

# Run the automated test robot
echo "🤖 Running Automated Test Robot..."
python tests/test_robot.py

# Run the live demonstration
echo "🎬 Starting Live Demo..."
python tests/test_live_demo.py

# Run all tests with the master runner
echo "🧪 Running Complete Test Suite..."
python tests/run_all_tests.py

# Show test coverage
pytest tests/ --cov=modules --cov-report=html --cov-report=term

# Open the presentation page
echo "🌐 Opening presentation page..."
# For Windows: start apresentacao/index_apresentacao.html
# For Linux/Mac: open apresentacao/index_apresentacao.html

echo "✅ Demo Complete! All systems operational!"
