"""
MOEMS Q&A Agent - Core Package

This package contains the main implementation of the MOEMS Q&A agent
with RAG pipeline and LangSmith tracing.
"""

from src.agent import MOEMSAgent
from src.evaluation import (
    create_evaluation_dataset,
    run_evaluations,
    print_evaluation_analysis
)

__version__ = "1.0.0"
__all__ = [
    "MOEMSAgent",
    "create_evaluation_dataset",
    "run_evaluations",
    "print_evaluation_analysis"
]