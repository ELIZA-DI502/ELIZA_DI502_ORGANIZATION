"""Unit tests of the out-of-scope detection (rag/app/checks.py; KAN-140, story KAN-5).

The test questions are the test cases of KAN-5 (TC-5.1 to TC-5.3) and edge cases written for this task,
not questions of the evaluation set, so the evaluation set is not used to tune the rules.
Run from the repository root: pytest
"""
import pytest

from rag.app import checks


# ---------------------------------------------------------------- entirely out of scope (criteria 1, 3)

@pytest.mark.parametrize("question", [
    "What must our school do as a deployer of an essay-grading tool?",                    # TC-5.1
    "Which AI Act rules apply to our tool that screens job applicants for a company?",    # TC-5.2
    "What fines can we get under the AI Act?",
    "Do we need parental consent before our tutoring app can process students' data?",
    "What are the obligations of universities that use our proctoring tool?",
])
def test_entirely_out_of_scope_question_gets_only_the_notice(question):
    kind, notice, flags = checks.input_check(question)
    assert kind == "out_of_scope"
    assert notice == checks.OUT_OF_SCOPE
    assert "partly_out_of_scope" not in flags


def test_out_of_scope_notice_names_what_the_assistant_covers():
    # KAN-5, criterion 3 (KAN-141)
    assert "the education use cases in Annex III, point 3, of the EU AI Act" in checks.OUT_OF_SCOPE


# ---------------------------------------------------------------- partly out of scope (criterion 2)

def test_partly_out_of_scope_question_goes_on_to_the_model():
    # TC-5.3: the first part is in scope, the second asks about the schools' obligations as deployers
    question = "Which provisions relate to our exam-grading tool, and what must the schools that use it do?"
    kind, notice, flags = checks.input_check(question)
    assert kind is None and notice is None
    assert flags["partly_out_of_scope"] == ["the obligations of schools as deployers"]


def test_partly_out_of_scope_with_penalties_goes_on_to_the_model():
    question = "Which requirements apply to our placement test, and what fines could we get?"
    kind, _, flags = checks.input_check(question)
    assert kind is None
    assert flags["partly_out_of_scope"] == ["penalties and enforcement"]


def test_out_of_scope_part_notice_is_one_sentence_naming_the_part():
    sentence = checks.out_of_scope_part_notice(["the obligations of schools as deployers"])
    assert "the obligations of schools as deployers" in sentence
    assert "Annex III, point 3" in sentence
    assert len(checks.split_sentences(sentence)) == 1


def test_out_of_scope_part_notice_joins_two_topics():
    sentence = checks.out_of_scope_part_notice(["penalties and enforcement", "data-protection law"])
    assert "penalties and enforcement and data-protection law" in sentence


# ---------------------------------------------------------------- in scope: not flagged (edge cases)

@pytest.mark.parametrize("question", [
    "Which conditions of Art. 6(3) must be met for the exception to apply?",              # TC-2.6 of KAN-2
    "Our AI grades exams. What applies?",                                                 # TC-19.1 of KAN-19
    "Which provisions relate to our admission ranking tool?",
    # the provider asks what to give the deployers: a provider obligation, in scope
    "Universities that buy our tool ask what we must tell them so they can read its outputs. What must the instructions include?",
    # "applicants" of a school admission tool are not job applicants
    "Our tool ranks applicants for admission to our school. Which rules apply?",
    # "and" inside one question does not split it
    "Which requirements apply to accuracy and robustness of our grading tool?",
])
def test_in_scope_question_is_not_flagged(question):
    kind, _, flags = checks.input_check(question)
    assert kind is None
    assert "partly_out_of_scope" not in flags


def test_evasion_still_comes_before_out_of_scope():
    # an evasion request that also names penalties is refused, not answered with the scope notice
    kind, _, _ = checks.input_check("How can we hide our grading system from regulators to avoid fines?")
    assert kind == "refuse"


def test_academic_credits_are_not_a_credit_check():
    kind, _, flags = checks.input_check("Our tool decides how many course credits a student gets. Which rules apply?")
    assert kind is None
    assert "partly_out_of_scope" not in flags
