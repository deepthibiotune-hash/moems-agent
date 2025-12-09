"""
Utility functions for the MOEMS Q&A Agent
"""
import time
from typing import List


def format_response(result: dict, include_metadata: bool = True) -> str:
    """
    Format agent response for display

    Args:
        result: Query result dictionary
        include_metadata: Whether to include sources and doc count

    Returns:
        Formatted string for display
    """
    lines = [
        "─" * 80,
        f"💡 Answer:",
        "─" * 80,
        result['answer']
    ]

    if include_metadata:
        lines.extend([
            "",
            "─" * 80,
            f"📚 Sources: {', '.join(result['sources'])}",
            f"📊 Documents Retrieved: {result['num_docs_retrieved']}",
            "─" * 80
        ])

    return "\n".join(lines)


def print_demo_header():
    """Print header for demo mode"""
    print("\n" + "="*80)
    print("MOEMS Q&A AGENT - DEMO MODE")
    print("="*80)
    print()
    print("📝 Demo queries showcase the agent's capabilities")
    print("🔍 Each query is fully traced in LangSmith")
    print()


def print_interactive_header():
    """Print header for interactive mode"""
    print("\n" + "="*80)
    print("INTERACTIVE MODE - Ask Your Own Questions!")
    print("="*80)
    print()
    print("📝 Example questions you can ask:")
    examples = [
        "What is MOEMS?",
        "What is the structure of a MOEMS contest?",
        "Who can participate in MOEMS?",
        "How is MOEMS scored?",
        "Are calculators allowed?",
        "Give me an example problem",
        "What strategies should students use?",
        "Can a 3rd grader participate if advanced?",
    ]
    for example in examples:
        print(f"  • {example}")
    print()
    print("Type 'quit' or 'exit' to end")
    print("Type 'eval' to proceed to evaluation")
    print("="*80 + "\n")


def run_timed_query(agent, question: str, query_num: int = None,
                    total_queries: int = None) -> dict:
    """
    Run a query with timing and formatted output

    Args:
        agent: MOEMSAgent instance
        question: Question to ask
        query_num: Query number (for display)
        total_queries: Total number of queries (for display)

    Returns:
        Query result dictionary
    """
    if query_num and total_queries:
        print(f"\n{'─'*80}")
        print(f"Query {query_num}/{total_queries}")
        print(f"{'─'*80}")

    print(f"❓ Question: {question}")
    print("\n🔍 Processing...")

    start_time = time.time()
    result = agent.query(question)
    elapsed_time = time.time() - start_time

    print(f"\n{format_response(result)}")
    print(f"⏱️  Response Time: {elapsed_time:.2f}s")

    return result


def validate_langsmith_setup() -> bool:
    """
    Validate LangSmith configuration

    Returns:
        True if LangSmith is properly configured
    """
    from config.settings import LANGCHAIN_API_KEY

    if not LANGCHAIN_API_KEY:
        print("\n⚠️  LangSmith Not Configured")
        print("─" * 80)
        print("LangSmith tracing is disabled. To enable:")
        print()
        print("1. Get API key: https://smith.langchain.com/")
        print("2. Add to .env: LANGCHAIN_API_KEY=lsv2-your-key")
        print("3. Restart the application")
        print("─" * 80 + "\n")
        return False

    print("✓ LangSmith configured and ready")
    return True


def print_langsmith_link(project_name: str = "moems-qa-agent"):
    """Print link to LangSmith dashboard"""
    print(f"\n🔗 View traces at: https://smith.langchain.com/")
    print(f"📁 Project: {project_name}\n")


def confirm_action(prompt: str, default: bool = True) -> bool:
    """
    Ask user for confirmation

    Args:
        prompt: Confirmation prompt
        default: Default value if user just presses enter

    Returns:
        True if user confirms, False otherwise
    """
    try:
        suffix = " (Y/n): " if default else " (y/N): "
        response = input(prompt + suffix).strip().lower()

        if not response:
            return default

        return response in ['y', 'yes']
    except KeyboardInterrupt:
        print("\n")
        return False


def print_section_header(title: str, width: int = 80):
    """Print a formatted section header"""
    print("\n" + "="*width)
    print(title)
    print("="*width + "\n")