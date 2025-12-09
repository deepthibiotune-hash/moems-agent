#!/bin/bash

# MOEMS Q&A Agent - Setup Script
# Run this to set up your environment for the interview demo

set -e  # Exit on error

echo "🚀 Setting up MOEMS Agent..."
echo ""

# Check Python version
echo "✓ Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
required_version="3.9"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "❌ Python 3.9+ required. Found: $python_version"
    exit 1
fi
echo "  Found Python $python_version"
echo ""

# Create virtual environment
echo "✓ Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "  Created venv/"
else
    echo "  Using existing venv/"
fi
echo ""

# Activate virtual environment
echo "✓ Activating virtual environment..."
source venv/bin/activate
echo ""

# Upgrade pip
echo "✓ Upgrading pip..."
pip install --upgrade pip > /dev/null 2>&1
echo ""

# Install dependencies
echo "✓ Installing dependencies (this may take 2-3 minutes)..."
pip install -r requirements.txt

echo "  ✓ All packages installed successfully"
echo ""

# Check for .env file
echo "✓ Checking environment variables..."
if [ ! -f ".env" ]; then
    echo "  ⚠️  No .env file found. Creating from template..."
    cat > .env << EOL
# OpenAI API Key (required)
OPENAI_API_KEY=your_openai_api_key_here
# LangSmith Configuration (required for tracing)
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_api_key_here
LANGCHAIN_PROJECT=moems-qa-agent
EOL
    echo ""
    echo "  📝 Created .env file. Please edit it with your API keys:"
    echo "     - Get OpenAI key: https://platform.openai.com/api-keys"
    echo "     - Get LangSmith key: https://smith.langchain.com/"
    echo ""
    echo "  Then run: source .env"
    exit 1
else
    echo "  Found .env file"
    source .env

    # Validate required keys
    if [ -z "$OPENAI_API_KEY" ] || [ "$OPENAI_API_KEY" = "your_openai_api_key_here" ]; then
        echo "  ❌ OPENAI_API_KEY not set in .env"
        exit 1
    fi

    if [ -z "$LANGCHAIN_API_KEY" ] || [ "$LANGCHAIN_API_KEY" = "your_langsmith_api_key_here" ]; then
        echo "  ❌ LANGCHAIN_API_KEY not set in .env"
        exit 1
    fi

    echo "  ✓ All API keys configured"
fi
echo ""

# Test imports
echo "✓ Testing imports..."
python3 -c "
import langchain
import langchain_openai
import langsmith
import faiss
print('  All imports successful')
" || { echo "❌ Import test failed"; exit 1; }
echo ""

echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "  1. Run the agent: python scripts/run_agent.py. It can take options --demo or --interactive"
echo "  2. Run full evaluation: python scripts/run_evaluation.py"
echo "  3. Run test cases: python tests/test_agent.py"
echo "  4. Check README.md for usage examples"
echo ""
