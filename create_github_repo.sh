#!/bin/bash
# Create a new GitHub repository and push the local project

# Repository name (customize as needed)
REPO_NAME="iot-ml-system"

# Create a new GitHub repository (public by default)
gh repo create $REPO_NAME --public --source=. --remote=origin --push

echo "GitHub repository '$REPO_NAME' created and initial commit pushed."

