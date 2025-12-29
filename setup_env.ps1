$VENV = ".venv"

if (!(Test-Path $VENV)) {
    Write-Host "Creating virtual environment..."
    py -m venv $VENV
}

Write-Host "Activating virtual environment..."
& "$VENV\Scripts\Activate.ps1"

Write-Host "Upgrading pip..."
pip install --upgrade pip

Write-Host "Installing dependencies..."
pip install -r requirements.txt

Write-Host "Environment ready"
