#!/bin/bash
python -m unittest discover -s . -p 'tests.py'
chmod +x tests.sh
./tests.sh
#!/bin/bash
# Make sure this script is correctly located at project/tests.sh

echo "Running tests..."
pytest
chmod +x project/tests.sh
git add project/tests.sh
git commit -m "Make tests.sh executable"

git add .github/workflows/CI.yml
git commit -m "Fix path and script references for tests.sh"
git push origin main

