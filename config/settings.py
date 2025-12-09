"""
Configuration and settings for the MOEMS Q&A Agent
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# LangSmith Configuration
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2", "true")
LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT", "moems-qa-agent")

# Set environment variables for LangSmith
if LANGCHAIN_API_KEY:
    os.environ["LANGCHAIN_TRACING_V2"] = LANGCHAIN_TRACING_V2
    os.environ["LANGCHAIN_PROJECT"] = LANGCHAIN_PROJECT

# Agent Configuration
AGENT_VERSION = "1.0.0"
AGENT_TYPE = "rag"

# Retrieval Configuration
DEFAULT_NUM_DOCS = 3
SIMULATE_RETRIEVAL_TIME = 0.3  # seconds
SIMULATE_GENERATION_TIME = 0.2  # seconds

# Evaluation Configuration
DATASET_NAME = "moems-qa-evaluation"
EVALUATION_1_PREFIX = "eval1-factual-accuracy"
EVALUATION_2_PREFIX = "eval2-context-utilization"