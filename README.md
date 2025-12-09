# MOEMS Q&A Agent - Setup Guide

Complete setup instructions for the MOEMS Q&A Agent project.

## 📁 Project Structure

```
moems_qa_agent/
├── README.md                # Main documentation
├── requirements.txt         # Python dependencies
├── .env                     # Environment template
├── setup.sh                 # Run this script to perform the initial setup of your environment. 
│
├── config/
│   └── settings.py         # Configuration and environment
│
├── data/
│   └── knowledge_base.py   # MOEMS knowledge base and evaluation data
│
├── src/
│   ├── __init__.py         # Package initialization
│   ├── agent.py            # Part 1: RAG agent implementation
│   ├── evaluation.py       # Part 2: Evaluation framework
│   └── utils.py            # Helper functions
│
├── scripts/
│   ├── run_agent.py        # Run agent demo/interactive mode
│   └── run_evaluation.py   # Run automated evaluations
│
└── tests/
    └── test_agent.py       # Test suite
```

## 🚀 Quick Setup (5 minutes)

### Step 1: Clone and Navigate

```bash
git clone <your-repo-url>
cd moems_qa_agent
```

### Step 2: Run setup.sh. It creates the Virtual Environment and Installs all the required dependencies

```bash
source setup.sh
```

### Step 4: Configure LangSmith - Pl. ensure to copy your own api_key.

```bash
# Copy environment template
vi .env

# Edit .env and add your LangSmith API key
# Get your key from: https://smith.langchain.com/
```

Your `.env` should look like:
```
LANGCHAIN_API_KEY=lsv2_pt_your_api_key_here
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=moems-qa-agent
```

### Step 5: Verify Setup

```bash
# Test the agent
python scripts/run_agent.py --demo

# Run tests
python tests/test_agent.py
```

✅ If you see demo queries execute successfully, you're ready!

---

## 📚 Detailed Usage

### Part 1: Running the Agent

#### Demo Mode (Recommended for first run)
```bash
python scripts/run_agent.py
```

This will:
- Run 3 demo queries
- Show formatted responses
- Display LangSmith trace links
- Offer interactive mode

#### Interactive Mode
```bash
python scripts/run_agent.py --interactive
```

Ask your own questions like:
- "What is MOEMS?"
- "How is MOEMS scored?"
- "Can a 3rd grader participate?"

Type `quit` to exit or `eval` to proceed to evaluation.

#### Demo Only (No Interactive)
```bash
python scripts/run_agent.py --demo
```

### Part 2: Running Evaluations

#### Full Evaluation (Recommended)
```bash
python scripts/run_evaluation.py
```

This will:
1. Create evaluation dataset (8 questions)
2. Run Evaluation 1: Factual Accuracy
3. Run Evaluation 2: Context Utilization
4. Display detailed analysis

#### Skip Dataset Creation
```bash
python scripts/run_evaluation.py --eval-only
```

Use this if dataset already exists in LangSmith.

#### Analysis Only
```bash
python scripts/run_evaluation.py --analysis
```

View the analysis without running evaluations.

---

## 🧪 Testing

### Run All Tests
```bash
python -m pytest tests/ -v
```

### Run Tests Without pytest
```bash
python tests/test_agent.py
```

### Run Specific Test
```bash
python -m pytest tests/test_agent.py::TestMOEMSAgent::test_basic_query -v
```

---

## 🔍 Troubleshooting

### Issue: "LangSmith not configured"

**Solution:**
1. Check `.env` file exists
2. Verify `LANGCHAIN_API_KEY` is set correctly
3. Ensure no extra spaces around the key
4. Restart terminal/reload environment

```bash
# Check if key is loaded
python -c "from config.settings import LANGCHAIN_API_KEY; print('Key found!' if LANGCHAIN_API_KEY else 'Key missing!')"
```

### Issue: "Module not found"

**Solution:**
Ensure you're running scripts from the project root:

```bash
# From project root
python scripts/run_agent.py

# NOT from scripts directory
cd scripts  # ❌
python run_agent.py  # ❌
```

### Issue: "Dataset already exists"

**Solution:**
This is normal! The script detects existing datasets.

To recreate the dataset:
1. Delete it in LangSmith UI
2. Run `python scripts/run_evaluation.py` again

### Issue: Import errors

**Solution:**
Install in development mode:

```bash
pip install -e .
```

---

## 🎯 Interview Preparation

### 1. Prepare Demo Queries

Test these before the interview:
```python
from src.agent import MOEMSAgent

agent = MOEMSAgent()

# Test queries
agent.query("What is MOEMS?")
agent.query("What is the structure of a MOEMS contest?")
agent.query("Can a 3rd grader participate if they're advanced?")
```

### 2. Review LangSmith Traces

1. Visit https://smith.langchain.com/
2. Navigate to project: `moems-qa-agent`
3. Review traces for:
    - Retrieval steps
    - Generation steps
    - Timing information

### 3. Review Evaluation Results

1. Check evaluation experiments in LangSmith
2. Note scores for both evaluations
3. Prepare to discuss:
    - Factual accuracy performance
    - Context relevancy metrics
    - Identified weaknesses

### 4. Prepare Discussion Points

From `src/evaluation.py`, review:
- **Identified Weakness**: Multi-document synthesis
- **Proposed Mitigation**: Re-ranking layer
- **Key Design Decisions**: RAG architecture choices

### 5. Test Live Demo Flow

Practice this sequence:
```bash
# Terminal 1: Run agent
python scripts/run_agent.py --interactive

# Terminal 2: Open LangSmith
open https://smith.langchain.com/

# Ask 2-3 questions in Terminal 1
# Show traces in Terminal 2
```

---

## 🔧 Development

### Adding New Questions to Knowledge Base

Edit `data/knowledge_base.py`:

```python
KNOWLEDGE_BASE = {
    # ... existing entries ...
    "new_topic": {
        "answer": "Your answer here",
        "sources": ["source1", "source2"],
        "retrieved_docs": [
            MockDocument("Content", "source1", "topic")
        ]
    }
}
```

### Adding New Evaluations

Edit `src/evaluation.py`:

```python
def my_custom_evaluator(run, example):
    """Custom evaluation logic"""
    # Your evaluation code
    return {
        "key": "my_metric",
        "score": score,
        "comment": "Explanation"
    }

# Add to run_evaluations()
results["eval3"] = evaluate(
    predict,
    data=dataset_name,
    evaluators=[my_custom_evaluator],
    experiment_prefix="eval3-custom"
)
```

### Modifying Agent Behavior

Edit `src/agent.py`:

- `_find_best_match()`: Change keyword matching logic
- `_retrieve()`: Modify retrieval parameters
- `_generate()`: Adjust generation process

---

## 📊 Project Statistics

- **Total Lines of Code**: ~1,200
- **Modules**: 7 Python files
- **Test Coverage**: 12 test cases
- **Evaluation Questions**: 8
- **Demo Queries**: 3
- **Knowledge Base Entries**: 9

---

## 🔗 Useful Links

- **LangSmith Dashboard**: https://smith.langchain.com/
- **LangSmith Docs**: https://docs.smith.langchain.com/
- **Project Repository**: [Your GitHub URL]

---

## 📝 Pre-Interview Checklist

Before the interview, verify:

- [ ] Virtual environment activated
- [ ] All dependencies installed (`pip list` shows langsmith)
- [ ] `.env` file configured with valid API key
- [ ] Demo runs successfully (`python scripts/run_agent.py`)
- [ ] Evaluations run successfully (`python scripts/run_evaluation.py`)
- [ ] Tests pass (`python tests/test_agent.py`)
- [ ] LangSmith traces visible in dashboard
- [ ] Can explain RAG architecture
- [ ] Can explain identified weakness and mitigation
- [ ] Prepared 2-3 challenging test questions

---

## 💡 Tips for Success

1. **Keep it Simple**: Focus on explaining the RAG pipeline clearly
2. **Use LangSmith**: Showcase the tracing for transparency
3. **Know Your Data**: Understand the knowledge base structure
4. **Prepare Edge Cases**: Have interesting questions ready
5. **Explain Trade-offs**: Discuss why you chose each approach

---

## 🆘 Getting Help

If you encounter issues:

1. Check this guide's Troubleshooting section
2. Review error messages carefully
3. Verify all setup steps completed
4. Test with demo mode first
5. Check LangSmith dashboard for trace errors

---

**Ready to go?**

Run `python scripts/run_agent.py` to get started! 🚀
