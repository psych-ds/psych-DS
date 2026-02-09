#!/bin/bash
# migrate_pyenv.sh - Automated migration script

set -e  # Exit on error

echo "🔧 Psych-DS pyenv Migration Script"
echo "===================================="
echo ""

# Check if in git repo
if [ ! -d ".git" ]; then
    echo "❌ Error: Not in a git repository"
    echo "   Please run this from the root of the psych-DS repository"
    exit 1
fi

# Check if pyenv directory exists
if [ ! -d "pyenv" ]; then
    echo "⚠️  Warning: pyenv/ directory not found"
    echo "   Perhaps it's already been removed?"
    read -p "   Continue anyway? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 0
    fi
fi

echo "📋 Step 1: Updating .gitignore"
echo "================================"

# Check if .gitignore exists
if [ ! -f ".gitignore" ]; then
    echo "Creating .gitignore..."
    touch .gitignore
fi

# Add Python ignores if not already present
if ! grep -q "pyenv/" .gitignore 2>/dev/null; then
    echo "Adding Python virtual environment patterns to .gitignore..."
    cat >> .gitignore << 'EOF'

# Python virtual environments
pyenv/
venv/
.venv/
env/
ENV/
.env/

# Python artifacts
__pycache__/
*.py[cod]
*.so
*.egg-info/
dist/
build/
EOF
    echo "✅ Updated .gitignore"
else
    echo "✅ .gitignore already contains pyenv/"
fi

echo ""
echo "🗑️  Step 2: Removing pyenv from git tracking"
echo "=============================================="

if [ -d "pyenv" ]; then
    echo "Removing pyenv/ from git (keeping local files)..."
    git rm -r --cached pyenv/ || true
    echo "✅ Removed from git tracking"
else
    echo "ℹ️  pyenv/ not tracked in git"
fi

echo ""
echo "📦 Step 3: Adding Python package configuration"
echo "==============================================="

# Check if files need to be downloaded/created
if [ ! -f "pyproject.toml" ]; then
    echo "⚠️  pyproject.toml not found in current directory"
    echo "   Please add the pyproject.toml file before running git add"
else
    echo "✅ Found pyproject.toml"
fi

if [ ! -f "requirements.txt" ]; then
    echo "⚠️  requirements.txt not found in current directory"
    echo "   Please add the requirements.txt file before running git add"
else
    echo "✅ Found requirements.txt"
fi

echo ""
echo "💾 Step 4: Committing changes"
echo "=============================="

read -p "Commit the changes now? (y/N) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    git add .gitignore
    
    if [ -f "pyproject.toml" ]; then
        git add pyproject.toml
    fi
    
    if [ -f "requirements.txt" ]; then
        git add requirements.txt
    fi
    
    git commit -m "Remove pyenv virtual environment from git

- Virtual environments should not be in version control
- User-specific paths make it non-portable
- Replaced with pyproject.toml and requirements.txt
- Updated .gitignore to exclude virtual environments"
    
    echo "✅ Changes committed"
else
    echo "ℹ️  Skipping commit - you can commit manually:"
    echo "   git add .gitignore pyproject.toml requirements.txt"
    echo "   git commit -m 'Remove pyenv and add proper Python packaging'"
fi

echo ""
echo "🧹 Step 5: Cleanup local pyenv directory"
echo "=========================================="

if [ -d "pyenv" ]; then
    read -p "Delete local pyenv/ directory? (y/N) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -rf pyenv/
        echo "✅ Deleted pyenv/"
    else
        echo "ℹ️  Keeping local pyenv/ - remember to delete it manually later"
    fi
else
    echo "ℹ️  pyenv/ already deleted"
fi

echo ""
echo "🎉 Migration Complete!"
echo "======================"
echo ""
echo "Next steps:"
echo "1. Set up your own virtual environment:"
echo "   python3 -m venv .venv"
echo "   source .venv/bin/activate  # or .venv\\Scripts\\activate on Windows"
echo "   pip install -r requirements.txt"
echo ""
echo "2. Test the tools:"
echo "   python schema_model/tools/convert_to_json.py"
echo ""
echo "3. Push changes:"
echo "   git push origin main"
echo ""
echo "4. Notify your team about the changes"
echo ""
