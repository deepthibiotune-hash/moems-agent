"""
Knowledge base data for the MOEMS Q&A Agent

This module contains the pre-built knowledge base that simulates
a document store/vector database for demo purposes.
"""


class MockDocument:
    """Mock document class to simulate retrieved documents"""
    def __init__(self, content: str, source: str, topic: str = "general"):
        self.page_content = content
        self.metadata = {"source": source, "topic": topic}


# Knowledge Base: Pre-indexed MOEMS information
KNOWLEDGE_BASE = {
    "what is moems": {
        "answer": "MOEMS stands for Mathematical Olympiads for Elementary and Middle Schools. It is a mathematics competition designed for students in grades 4-8, providing an engaging way for students to develop problem-solving skills through challenging mathematical problems.",
        "sources": ["moems_overview", "moems_introduction"],
        "retrieved_docs": [
            MockDocument(
                "MOEMS stands for Mathematical Olympiads for Elementary and Middle Schools. It is a mathematics competition designed for students in grades 4-8.",
                "moems_overview",
                "introduction"
            ),
            MockDocument(
                "MOEMS provides an engaging way for students to develop problem-solving skills through challenging mathematical problems.",
                "moems_introduction",
                "introduction"
            )
        ]
    },
    "structure": {
        "answer": "Each MOEMS contest consists of exactly 5 problems. Students have 30 minutes total to complete all 5 problems. Calculators are strictly prohibited during the contest, emphasizing mental math and problem-solving skills.",
        "sources": ["moems_structure", "moems_rules"],
        "retrieved_docs": [
            MockDocument(
                "Each MOEMS contest consists of exactly 5 problems. Students have 30 minutes total to complete all 5 problems.",
                "moems_structure",
                "format"
            ),
            MockDocument(
                "Calculators are strictly prohibited during MOEMS contests, emphasizing mental math and problem-solving skills.",
                "moems_rules",
                "equipment"
            )
        ]
    },
    "participate": {
        "answer": "Students in grades 4 through 8 can participate in MOEMS. This includes both elementary school students (grades 4-5) and middle school students (grades 6-8). The competition is appropriate for students aged approximately 9-14 years old.",
        "sources": ["moems_eligibility"],
        "retrieved_docs": [
            MockDocument(
                "Students in grades 4 through 8 can participate in MOEMS. This includes both elementary and middle school students (grades 4-5 for elementary, 6-8 for middle school). Appropriate for ages 9-14.",
                "moems_eligibility",
                "participation"
            )
        ]
    },
    "scored": {
        "answer": "Each problem in a MOEMS contest is worth 1 point. The maximum score for a single contest is 5 points (one for each problem). Teams compete based on cumulative scores across multiple contests throughout the year.",
        "sources": ["moems_scoring"],
        "retrieved_docs": [
            MockDocument(
                "Each problem is worth 1 point. Maximum score per contest is 5 points. Teams compete based on cumulative scores across multiple contests.",
                "moems_scoring",
                "scoring"
            )
        ]
    },
    "calculator": {
        "answer": "No, calculators are not allowed in MOEMS contests. Calculators are strictly prohibited. The competition emphasizes mental math and problem-solving skills without computational aids.",
        "sources": ["moems_rules"],
        "retrieved_docs": [
            MockDocument(
                "Calculators are strictly prohibited in MOEMS contests. The competition emphasizes mental math and problem-solving skills without computational aids.",
                "moems_rules",
                "equipment"
            )
        ]
    },
    "example": {
        "answer": "Here's a sample MOEMS algebra problem: If 3x + 7 = 22, what is the value of x? Solution: x = 5. To solve, subtract 7 from both sides to get 3x = 15, then divide by 3 to get x = 5. This type of problem tests students' ability to isolate variables and perform basic algebraic operations.",
        "sources": ["moems_examples"],
        "retrieved_docs": [
            MockDocument(
                "Sample Problem: If 3x + 7 = 22, what is x? Solution: Subtract 7 from both sides: 3x = 15, then divide by 3 to get x = 5. Tests variable isolation and basic algebra.",
                "moems_examples",
                "problems"
            )
        ]
    },
    "strategies": {
        "answer": "Given the 30-minute time limit for 5 problems, students have an average of 6 minutes per problem. Recommended strategy: (1) Quickly read all 5 problems first (2 minutes), (2) Start with problems that seem easiest (10 minutes for 2-3 problems), (3) Work on medium difficulty problems next (10 minutes), (4) Attempt challenging problems last (8 minutes). Time management is crucial for success in MOEMS competitions.",
        "sources": ["moems_strategies"],
        "retrieved_docs": [
            MockDocument(
                "Time management strategy: Average 6 minutes per problem. (1) Read all problems first (2 min), (2) Start with easiest (10 min), (3) Work on medium difficulty (10 min), (4) Attempt hardest last (8 min).",
                "moems_strategies",
                "strategy"
            )
        ]
    },
    "time": {
        "answer": "Students have 30 minutes total to complete all 5 problems in a MOEMS contest. This works out to an average of 6 minutes per problem, though students are free to allocate their time as they see fit across the problems.",
        "sources": ["moems_structure"],
        "retrieved_docs": [
            MockDocument(
                "30 minutes total for all 5 problems. Average of 6 minutes per problem, though time can be allocated as needed.",
                "moems_structure",
                "format"
            )
        ]
    },
    "3rd grader": {
        "answer": "MOEMS is officially designed for grades 4-8. While the standard eligibility is grades 4-8, exceptional cases such as an advanced 3rd grader may be handled on a case-by-case basis by contacting MOEMS organizers directly. The competition content is generally geared toward the cognitive development of students in the 4-8 grade range.",
        "sources": ["moems_eligibility", "moems_eligibility_exceptions"],
        "retrieved_docs": [
            MockDocument(
                "MOEMS is designed for grades 4-8.",
                "moems_eligibility",
                "participation"
            ),
            MockDocument(
                "Standard eligibility is grades 4-8. Exceptional cases such as advanced 3rd graders may be handled case-by-case by contacting organizers. Content is geared toward 4-8 grade cognitive development.",
                "moems_eligibility_exceptions",
                "participation"
            )
        ]
    }
}


# Evaluation Dataset: Questions with ground truth answers
EVALUATION_EXAMPLES = [
    {
        "question": "What is MOEMS?",
        "reference": "MOEMS stands for Mathematical Olympiads for Elementary and Middle Schools, a mathematics competition for students in grades 4-8 that helps develop problem-solving skills."
    },
    {
        "question": "What is the structure of a MOEMS contest?",
        "reference": "Each MOEMS contest consists of 5 problems to be completed in 30 minutes total, with calculators prohibited."
    },
    {
        "question": "Who can participate in MOEMS?",
        "reference": "Students in grades 4-8 (elementary and middle school) can participate. Exceptional 3rd graders may participate on a case-by-case basis."
    },
    {
        "question": "How is MOEMS scored?",
        "reference": "Each problem is worth 1 point, for a maximum of 5 points per contest. Teams compete based on cumulative scores."
    },
    {
        "question": "Are calculators allowed in MOEMS?",
        "reference": "No, calculators are strictly prohibited in MOEMS contests to emphasize mental math and problem-solving skills."
    },
    {
        "question": "How much time do students have for each problem?",
        "reference": "Students have 30 minutes total for 5 problems, averaging 6 minutes per problem, though they can allocate time as needed."
    },
    {
        "question": "What strategies should students use for time management?",
        "reference": "Read all problems first (2 min), start with easiest (10 min), work on medium difficulty (10 min), attempt hardest last (8 min)."
    },
    {
        "question": "Can a 3rd grader participate in MOEMS?",
        "reference": "MOEMS is designed for grades 4-8, but exceptional 3rd graders may participate on a case-by-case basis by contacting organizers."
    }
]


# Demo questions for testing
DEMO_QUESTIONS = [
    "What is MOEMS?",
    "What is the structure of a MOEMS contest?",
    "Are calculators allowed in MOEMS contests?",
]