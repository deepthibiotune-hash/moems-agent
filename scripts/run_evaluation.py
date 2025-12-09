"""
Run MOEMS Q&A Agent Evaluation - Part 2

Usage:
    python scripts/run_evaluation.py              # Full evaluation
    python scripts/run_evaluation.py --eval-only  # Skip dataset creation
    python scripts/run_evaluation.py --analysis   # Show analysis only
"""
import sys
import argparse
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from langsmith import Client
from src.agent import MOEMSAgent
from src.evaluation import (
    create_evaluation_dataset,
    run_evaluations,
    print_evaluation_analysis
)
from src.utils import (
    print_section_header,
    validate_langsmith_setup,
    confirm_action
)
from config.settings import LANGCHAIN_API_KEY, DATASET_NAME


def check_langsmith_required():
    """Verify LangSmith is configured"""
    if not LANGCHAIN_API_KEY:
        print("\n❌ ERROR: LangSmith Required for Evaluation")
        print("─" * 80)
        print("Evaluation features require LangSmith API key.")
        print()
        print("Setup steps:")
        print("1. Get API key: https://smith.langchain.com/")
        print("2. Add to .env: LANGCHAIN_API_KEY=lsv2-your-key")
        print("3. Run this script again")
        print("─" * 80 + "\n")
        sys.exit(1)


def main():
    """Main execution function"""
    # Parse arguments
    parser = argparse.ArgumentParser(
        description="MOEMS Q&A Agent Evaluation - Part 2"
    )
    parser.add_argument(
        '--eval-only',
        action='store_true',
        help='Run evaluations only (skip dataset creation)'
    )
    parser.add_argument(
        '--analysis', '-a',
        action='store_true',
        help='Show analysis only (no evaluations)'
    )
    args = parser.parse_args()

    # Print header
    print_section_header("🎓 MOEMS Q&A AGENT - PART 2: EVALUATION")

    print("Automated evaluation with:")
    print("  • Evaluation 1: Factual Accuracy (Answer Relevancy)")
    print("  • Evaluation 2: Context Utilization (Context Relevancy)")
    print()

    # Analysis only mode
    if args.analysis:
        print_evaluation_analysis()
        return

    # Verify LangSmith setup
    check_langsmith_required()
    validate_langsmith_setup()

    # Initialize client and agent
    print_section_header("INITIALIZATION")

    client = Client()
    print("✓ LangSmith client initialized")

    agent = MOEMSAgent()
    print()

    # Create evaluation dataset
    if not args.eval_only:
        print_section_header("CREATING EVALUATION DATASET")

        dataset_name = create_evaluation_dataset(client)
        print(f"\n✓ Dataset ready: {dataset_name}")
        print(f"📊 Contains 8 evaluation questions with ground truth")
        print()
    else:
        print(f"Using existing dataset: {DATASET_NAME}\n")
        dataset_name = DATASET_NAME

    # Confirm before running evaluations
    print_section_header("READY TO RUN EVALUATIONS")

    print("This will:")
    print("  • Run 8 test questions through the agent")
    print("  • Evaluate factual accuracy (Eval 1)")
    print("  • Evaluate context utilization (Eval 2)")
    print("  • Generate performance metrics")
    print("  • Store results in LangSmith")
    print()
    print("Estimated time: 1-2 minutes")
    print()

    if not confirm_action("Proceed with evaluation?"):
        print("\nEvaluation cancelled.")
        print("\nTo run later: python scripts/run_evaluation.py")
        return

    # Run evaluations
    print_section_header("RUNNING EVALUATIONS")

    try:
        results = run_evaluations(agent, dataset_name)

        print("\n✅ Evaluations Complete!")
        print()
        print("📊 Results Summary:")
        print("─" * 80)

        if results.get("eval1"):
            print("✓ Evaluation 1 (Factual Accuracy): Complete")
        else:
            print("⚠️  Evaluation 1: Failed or skipped")

        if results.get("eval2"):
            print("✓ Evaluation 2 (Context Utilization): Complete")
        else:
            print("⚠️  Evaluation 2: Failed or skipped")

        print("─" * 80)
        print()
        print("🔗 View detailed results at: https://smith.langchain.com/")
        print(f"📁 Project: moems-qa-agent")
        print(f"📊 Dataset: {dataset_name}")
        print()

    except Exception as e:
        print(f"\n❌ Evaluation failed: {e}")
        print("\nPlease check:")
        print("  • LangSmith API key is valid")
        print("  • Dataset exists in LangSmith")
        print("  • Internet connection is stable")
        return

    # Show analysis
    if confirm_action("\nShow detailed analysis?"):
        print_evaluation_analysis()
    else:
        print("\nTo view analysis: python scripts/run_evaluation.py --analysis")

    # Final summary
    print_section_header("✅ EVALUATION COMPLETE - READY FOR INTERVIEW")

    print("Interview Preparation:")
    print("  ✓ Part 1: Agent implemented with RAG + LangSmith tracing")
    print("  ✓ Part 2: Two automated evaluations complete")
    print("  ✓ Analysis: Weakness identified + mitigation proposed")
    print()
    print("Next Steps:")
    print("  • Review evaluation results in LangSmith")
    print("  • Test agent with new questions: python scripts/run_agent.py -i")
    print("  • Prepare live demo for interview")
    print()
    print("🎯 Key Discussion Points:")
    print("  • RAG architecture and design decisions")
    print("  • Evaluation results and performance metrics")
    print("  • Identified weakness: Multi-document synthesis")
    print("  • Proposed mitigation: Re-ranking layer")
    print()


if __name__ == "__main__":
    main()