#!/bin/bash

python_executables=("python" "python3")

# Flag to track whether Python is found
python_found=false

# Check each possible Python executable
for executable in "${python_executables[@]}"; do
  if command -v "$executable" &>/dev/null; then
    python_executable="$executable"
    python_found=true
    break
  fi
done

# Check if Python is found
if ! "$python_found"; then
  echo "Python not installed"
  exit 1
fi

if ! $python_executable -m venv .venv; then
  echo "Failed to create virtual environment"
  exit 1
fi

echo "Created virtual environment"
activate () {
  . .venv/bin/activate
  echo "Activated virtual environment"
}
activate

# . .venv/bin/activate || . .venv/Scripts/activate 

if ! pip install flask &> /dev/null; then 
  echo -e "Failed to install flask"
  exit 1
fi 

echo "Successfully installed flask"
echo "Finished: run '. .venv/bin/activate' if you are on macos and '. .venv/Scripts/activate' if you are on windows"
