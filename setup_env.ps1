$VENV = ".venv"

# 1. Create virtual environment if it doesn't exist
if (!(Test-Path $VENV)) {
    Write-Host "Creating virtual environment..."
    py -m venv $VENV
} else {
    Write-Host "Virtual environment already exists."
}

# 2. Activate virtual environment
Write-Host "Activating virtual environment..."
& "$VENV\Scripts\Activate.ps1"

# 3. Upgrade pip
py -m pip install --upgrade pip

# 4. Generate requirements.txt from installed packages
Write-Host "Generating requirements.txt..."
pip freeze | Sort-Object | Out-File requirements.txt -Encoding utf8

# 5. Install dependencies from requirements.txt
Write-Host "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

Write-Host "Environment ready"
