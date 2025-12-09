"""
Tests for MOEMS Q&A Agent

Basic test suite to verify agent functionality.

Run with: python -m pytest tests/
"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.agent import MOEMSAgent


class TestMOEMSAgent:
    """Test suite for MOEMSAgent"""

    def setup_method(self):
        """Initialize agent before each test"""
        self.agent = MOEMSAgent()

    def test_agent_initialization(self):
        """Test agent initializes correctly"""
        assert self.agent is not None
        assert self.agent.knowledge_base is not None

    def test_basic_query(self):
        """Test basic query returns expected structure"""
        result = self.agent.query("What is MOEMS?")

        assert "question" in result
        assert "answer" in result
        assert "sources" in result
        assert "num_docs_retrieved" in result
        assert "retrieved_contexts" in result

        assert isinstance(result["answer"], str)
        assert len(result["answer"]) > 0
        assert result["num_docs_retrieved"] > 0

    def test_moems_definition(self):
        """Test query about MOEMS definition"""
        result = self.agent.query("What is MOEMS?")

        answer = result["answer"].lower()
        assert "moems" in answer
        assert "mathematical olympiad" in answer or "mathematics competition" in answer

    def test_structure_query(self):
        """Test query about MOEMS structure"""
        result = self.agent.query("What is the structure of a MOEMS contest?")

        answer = result["answer"].lower()
        assert "5" in answer or "five" in answer
        assert "problem" in answer
        assert "30" in answer or "minutes" in answer

    def test_calculator_query(self):
        """Test query about calculator rules"""
        result = self.agent.query("Are calculators allowed in MOEMS?")

        answer = result["answer"].lower()
        assert "calculator" in answer
        assert "no" in answer or "not" in answer or "prohibit" in answer

    def test_scoring_query(self):
        """Test query about scoring"""
        result = self.agent.query("How is MOEMS scored?")

        answer = result["answer"].lower()
        assert "point" in answer
        assert "5" in answer or "five" in answer

    def test_eligibility_query(self):
        """Test query about eligibility"""
        result = self.agent.query("Who can participate in MOEMS?")

        answer = result["answer"].lower()
        assert "grade" in answer
        assert "4" in answer or "8" in answer

    def test_third_grader_query(self):
        """Test edge case query about 3rd graders"""
        result = self.agent.query("Can a 3rd grader participate?")

        answer = result["answer"].lower()
        assert "3rd" in answer or "third" in answer or "grade" in answer

    def test_unknown_query(self):
        """Test query with unknown topic"""
        result = self.agent.query("What is the weather today?")

        # Should return default response
        assert "answer" in result
        assert len(result["answer"]) > 0

    def test_sources_returned(self):
        """Test that sources are properly returned"""
        result = self.agent.query("What is MOEMS?")

        assert len(result["sources"]) > 0
        assert all(isinstance(s, str) for s in result["sources"])

    def test_contexts_returned(self):
        """Test that contexts are properly returned"""
        result = self.agent.query("What is MOEMS?")

        assert len(result["retrieved_contexts"]) > 0
        assert all(isinstance(c, str) for c in result["retrieved_contexts"])


def run_tests():
    """Run all tests manually (if pytest not available)"""
    import traceback

    test_agent = TestMOEMSAgent()
    test_methods = [
        method for method in dir(test_agent)
        if method.startswith("test_")
    ]

    print(f"\nRunning {len(test_methods)} tests...\n")

    passed = 0
    failed = 0

    for method_name in test_methods:
        try:
            test_agent.setup_method()
            method = getattr(test_agent, method_name)
            method()
            print(f"✓ {method_name}")
            passed += 1
        except Exception as e:
            print(f"✗ {method_name}")
            print(f"  Error: {e}")
            traceback.print_exc()
            failed += 1

    print(f"\n{'='*60}")
    print(f"Results: {passed} passed, {failed} failed")
    print(f"{'='*60}\n")

    return failed == 0


if __name__ == "__main__":
    # Run tests manually if pytest not available
    success = run_tests()
    sys.exit(0 if success else 1)