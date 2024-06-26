#!/bin/bash
#!/bin/bash

# Run the unit tests
python3 -m unittest discover -s . -p "test_pipeline.py"
chmod +x tests.sh
./tests.sh
