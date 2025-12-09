"""
MOEMS Q&A Agent - Part 1: Agent Implementation

RAG-based agent with full LangSmith tracing for answering
questions about MOEMS competitions.
"""
import time
from typing import List, Dict, Any
from langsmith import Client, traceable

from config.settings import (
    LANGCHAIN_API_KEY,
    AGENT_VERSION,
    AGENT_TYPE,
    SIMULATE_RETRIEVAL_TIME,
    SIMULATE_GENERATION_TIME
)
from data.knowledge_base import KNOWLEDGE_BASE, MockDocument


class MOEMSAgent:
    """
    MOEMS Q&A Agent using RAG pipeline with LangSmith tracing

    This agent demonstrates:
    - Retrieval-Augmented Generation (RAG) architecture
    - Full traceability with LangSmith
    - Document retrieval and answer generation

    Demo version: Uses pre-built knowledge base (no API costs)
    """

    def __init__(self):
        """Initialize agent with knowledge base and LangSmith client"""
        self.knowledge_base = KNOWLEDGE_BASE
        self.client = Client() if LANGCHAIN_API_KEY else None

        print("✓ MOEMS Agent initialized with RAG pipeline")
        if self.client:
            print("✓ LangSmith tracing enabled")
        else:
            print("⚠️  LangSmith not configured (set LANGCHAIN_API_KEY)")

    @traceable(name="find_best_match")
    def _find_best_match(self, question: str) -> Dict:
        """
        Find best matching answer based on keywords

        This simulates semantic search in a production system.
        In production, this would use embeddings and vector similarity.
        """
        question_lower = question.lower()

        # Keyword matching to simulate semantic search
        if "what is moems" in question_lower or "what's moems" in question_lower:
            return self.knowledge_base["what is moems"]
        elif "structure" in question_lower or "format" in question_lower:
            return self.knowledge_base["structure"]
        elif "participate" in question_lower or "who can" in question_lower or "eligib" in question_lower:
            return self.knowledge_base["participate"]
        elif "scor" in question_lower or "point" in question_lower:
            return self.knowledge_base["scored"]
        elif "calculator" in question_lower:
            return self.knowledge_base["calculator"]
        elif "example" in question_lower or "sample problem" in question_lower:
            return self.knowledge_base["example"]
        elif "strateg" in question_lower or "time management" in question_lower:
            return self.knowledge_base["strategies"]
        elif "time" in question_lower or "how long" in question_lower or "minutes" in question_lower:
            return self.knowledge_base["time"]
        elif "3rd grade" in question_lower or "third grade" in question_lower:
            return self.knowledge_base["3rd grader"]
        else:
            # Default response for unmatched questions
            return {
                "answer": "Based on the available MOEMS documentation, I can tell you that MOEMS is a mathematics competition for grades 4-8 students. Could you be more specific about what aspect you'd like to know? Topics include: structure, eligibility, scoring, rules, strategies, and examples.",
                "sources": ["moems_general"],
                "retrieved_docs": [
                    MockDocument(
                        "MOEMS general information. Competition for grades 4-8 students.",
                        "moems_general",
                        "general"
                    )
                ]
            }

    @traceable(name="retrieve_documents")
    def _retrieve(self, question: str) -> Dict:
        """
        Retrieve relevant documents from knowledge base

        Part 1 Requirement: Retrieval step in RAG pipeline

        In production, this would:
        1. Convert question to embeddings
        2. Search vector store for similar documents
        3. Return top-k most relevant documents
        """
        time.sleep(SIMULATE_RETRIEVAL_TIME)  # Simulate retrieval time
        result = self._find_best_match(question)
        return {
            "sources": result["sources"],
            "retrieved_docs": result["retrieved_docs"]
        }

    @traceable(name="generate_answer")
    def _generate(self, question: str, docs: List[MockDocument]) -> str:
        """
        Generate answer using retrieved context

        Part 1 Requirement: Generation step in RAG pipeline

        In production, this would:
        1. Format retrieved documents as context
        2. Create prompt with context + question
        3. Call LLM to generate answer
        4. Return synthesized answer
        """
        time.sleep(SIMULATE_GENERATION_TIME)  # Simulate generation time
        result = self._find_best_match(question)
        return result["answer"]

    @traceable(
        name="moems_agent_query",
        run_type="chain",
        metadata={"agent_type": AGENT_TYPE, "version": AGENT_VERSION}
    )
    def query(self, question: str) -> Dict[str, Any]:
        """
        Main query method implementing full RAG pipeline

        Part 1 Requirement: RAG pipeline with LangSmith tracing

        Process:
        1. Retrieve relevant documents (traced)
        2. Generate answer from context (traced)
        3. Return answer with sources and metadata

        Args:
            question: User's question about MOEMS

        Returns:
            Dictionary containing:
            - question: Original question
            - answer: Generated answer
            - sources: Source document identifiers
            - num_docs_retrieved: Number of documents used
            - retrieved_contexts: Content of retrieved documents
        """
        # Step 1: Retrieve relevant documents
        retrieval_result = self._retrieve(question)

        # Step 2: Generate answer from retrieved docs
        answer = self._generate(question, retrieval_result["retrieved_docs"])

        # Step 3: Return complete result
        return {
            "question": question,
            "answer": answer,
            "sources": retrieval_result["sources"],
            "num_docs_retrieved": len(retrieval_result["retrieved_docs"]),
            "retrieved_contexts": [
                doc.page_content for doc in retrieval_result["retrieved_docs"]
            ]
        }


def demo_agent():
    """Quick demo of agent functionality"""
    print("\n" + "="*80)
    print("MOEMS Q&A AGENT - QUICK DEMO")
    print("="*80 + "\n")

    agent = MOEMSAgent()

    test_question = "What is MOEMS?"
    print(f"Question: {test_question}\n")

    result = agent.query(test_question)

    print(f"Answer: {result['answer']}\n")
    print(f"Sources: {', '.join(result['sources'])}")
    print(f"Documents Retrieved: {result['num_docs_retrieved']}")

    if agent.client:
        print("\n🔗 View trace at: https://smith.langchain.com/")


if __name__ == "__main__":
    demo_agent()