#!/bin/bash
python -m unittest discover -s . -p 'tests.py'
<<<<<<< HEAD
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

=======
chmod +x project/tests.sh
.project/tests.sh
>>>>>>> a1f8e1fb7a238c7b10d3d2c53be994c2e7c75f9e
