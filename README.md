# Robust Calculator

A simple command-line calculator that supports addition, subtraction, multiplication, and division.

## Features
- Add, subtract, multiply, divide
- Handles invalid operations and numbers
- Gracefully handles divide-by-zero errors
- Command-line interface (CLI)

## Getting Started

### 1. Clone the repository
\`\`\`bash
git clone https://github.com/am3696-dev/robust-calculator
cd robust-calculator
\`\`\`

### 2. Create and activate a virtual environment
\`\`\`bash
python -m venv .venv
source .venv/bin/activate   # On Mac/Linux
.venv\Scripts\activate      # On Windows
\`\`\`

### 3. Install dependencies
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. Run the calculator
\`\`\`bash
python -m calculator.app
\`\`\`

### 5. Run tests with coverage
\`\`\`bash
pytest --cov=calculator tests/
\`\`\`

### 6. Notes
- Type \`quit\` to exit the calculator.
- CLI input is case-insensitive and trims whitespace.
EOL
