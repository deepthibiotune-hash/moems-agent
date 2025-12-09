"""
Run the MOEMS Q&A Agent - Demo and Interactive Modes

Usage:
    python scripts/run_agent.py              # Run demo queries
    python scripts/run_agent.py --interactive # Interactive Q&A mode
    python scripts/run_agent.py --demo       # Demo mode only
"""
import sys
import time
import argparse
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.agent import MOEMSAgent
from src.utils import (
    print_demo_header,
    print_interactive_header,
    print_section_header,
    run_timed_query,
    validate_langsmith_setup,
    print_langsmith_link,
    format_response
)
from data.knowledge_base import DEMO_QUESTIONS


def run_demo_mode(agent: MOEMSAgent):
    """
    Run demo queries to showcase agent capabilities

    Args:
        agent: MOEMSAgent instance
    """
    print_demo_header()

    for i, question in enumerate(DEMO_QUESTIONS, 1):
        run_timed_query(agent, question, i, len(DEMO_QUESTIONS))
        time.sleep(0.5)  # Brief pause between queries

    print("\n✓ Demo queries complete!")

    if agent.client:
        print_langsmith_link()


def run_interactive_mode(agent: MOEMSAgent):
    """
    Interactive Q&A session with the agent

    Args:
        agent: MOEMSAgent instance
    """
    print_interactive_header()

    query_count = 0

    while True:
        try:
            # Get user input
            user_question = input("❓ Your question: ").strip()

            # Handle empty input
            if not user_question:
                continue

            # Handle exit commands
            if user_question.lower() in ['quit', 'exit', 'q']:
                print(f"\n✅ Exiting interactive mode ({query_count} questions asked)")
                break

            # Handle eval command
            if user_question.lower() in ['eval', 'evaluation']:
                print(f"\n✅ Proceeding to evaluation ({query_count} questions asked)")
                print("\nRun: python scripts/run_evaluation.py")
                break

            # Process query
            print("\n🔍 Processing your question...")

            start_time = time.time()
            result = agent.query(user_question)
            elapsed_time = time.time() - start_time

            query_count += 1

            # Display results
            print(f"\n{format_response(result)}")
            print(f"⏱️  Response Time: {elapsed_time:.2f}s")

            if agent.client:
                print(f"🔗 View trace at: https://smith.langchain.com/")

        except KeyboardInterrupt:
            print(f"\n\n✅ Exiting interactive mode ({query_count} questions asked)")
            break

        except Exception as e:
            print(f"\n⚠️  Error: {e}")
            print("Please try another question.")

    return query_count


def main():
    """Main execution function"""
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="MOEMS Q&A Agent - Demo and Interactive Modes"
    )
    parser.add_argument(
        '--interactive', '-i',
        action='store_true',
        help='Run in interactive mode'
    )
    parser.add_argument(
        '--demo', '-d',
        action='store_true',
        help='Run demo mode only'
    )
    args = parser.parse_args()

    # Print header
    print_section_header("🎓 MOEMS Q&A AGENT - PART 1: AGENT DEMONSTRATION")

    print("RAG-based Q&A agent with full LangSmith tracing")
    print("Demo Mode: No API costs (pre-built knowledge base)")
    print()

    # Validate LangSmith setup
    validate_langsmith_setup()

    # Initialize agent
    print_section_header("INITIALIZING AGENT")
    agent = MOEMSAgent()

    # Determine mode
    if args.interactive:
        # Interactive mode only
        run_interactive_mode(agent)
    elif args.demo:
        # Demo mode only
        run_demo_mode(agent)
    else:
        # Default: Demo then offer interactive
        run_demo_mode(agent)

        print("\n" + "="*80)
        response = input("Would you like to ask your own questions? (y/n): ").strip().lower()

        if response == 'y':
            query_count = run_interactive_mode(agent)
            print(f"\n✓ Interactive session complete ({query_count} questions asked)")

    # Final summary
    print_section_header("✅ SESSION COMPLETE")

    if agent.client:
        print("🔗 View all traces at: https://smith.langchain.com/")
        print(f"📁 Project: moems-qa-agent")

    print("\n💡 Next Steps:")
    print("  • Run evaluations: python scripts/run_evaluation.py")
    print("  • Review traces in LangSmith dashboard")
    print("  • Prepare for interview demonstration")
    print()


if __name__ == "__main__":
    main()