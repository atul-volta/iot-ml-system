#!/usr/bin/env python3
import os

# Define project structure
structure = [
    ".github/ISSUE_TEMPLATE",
    ".github/workflows",
    "docs",
    "iot/device_code",
    "ml/notebooks",
    "ml/models",
    "ml/scripts",
    "tests"
]

# Create directories
for folder in structure:
    os.makedirs(folder, exist_ok=True)
    print(f"Created directory: {folder}")

# Create a basic README.md
readme_content = """# IoT Machine Learning System

This project integrates IoT device data with machine learning models. It follows Agile practices with incremental development.

## Project Structure
- **iot/**: IoT integration code.
- **ml/**: Machine learning experiments and production code.
- **docs/**: Documentation and Agile boards.
- **tests/**: Automated tests.

## How to Start
1. Install dependencies: `pip install -r requirements.txt`
2. Run the sample ML script: `python ml/scripts/simple_model.py`
"""
with open("README.md", "w") as f:
    f.write(readme_content)
    print("Created README.md")

# Create a basic .gitignore
gitignore_content = """__pycache__/
*.pyc
.env
venv/
"""
with open(".gitignore", "w") as f:
    f.write(gitignore_content)
    print("Created .gitignore")

# Create a basic requirements.txt
requirements_content = """scikit-learn
pandas
numpy
jupyter
"""
with open("requirements.txt", "w") as f:
    f.write(requirements_content)
    print("Created requirements.txt")

# Create a starter ML script
simple_ml_script = """#!/usr/bin/env python3
\"\"\"A simple ML example using scikit-learn\"\"\"

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def main():
    # Load dataset
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42)
    
    # Build model
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    
    # Predict and evaluate
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2f}")

if __name__ == "__main__":
    main()
"""
with open("ml/scripts/simple_model.py", "w") as f:
    f.write(simple_ml_script)
    print("Created ml/scripts/simple_model.py")
