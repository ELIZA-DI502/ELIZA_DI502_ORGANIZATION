"""Unit tests of the rule-based checks of the RAG service (rag/app/checks.py, D3).

The checks run without the model, so these tests need no Ollama and no vector store.
Run from the repository root: pytest
"""
from rag.app import checks


# ---------------------------------------------------------------- input check

def test_evasion_request_is_refused():
    # TC-2.4 of KAN-2
    kind, notice, _ = checks.input_check("How can we hide from regulators that our system grades students?")
    assert kind == "refuse"
    assert notice == checks.REFUSAL


def test_condition_question_is_not_refused():
    # TC-2.6 of KAN-2: a question about conditions or exceptions goes on to the model
    kind, _, _ = checks.input_check("Which conditions of Art. 6(3) must be met for the exception to apply?")
    assert kind is None


def test_out_of_scope_question_gets_a_notice():
    kind, notice, _ = checks.input_check("What fines can we get under the AI Act?")
    assert kind == "out_of_scope"
    assert notice == checks.OUT_OF_SCOPE


def test_email_address_is_found():
    assert checks.has_personal_data("Please answer to test.user@example.com")


def test_question_without_personal_data_passes():
    assert not checks.has_personal_data("Which requirements apply to our exam-proctoring tool?")


# ---------------------------------------------------------------- output check

def test_verdict_sentence_is_caught():
    assert checks.is_verdict("Your placement test is high-risk.")


def test_provision_explanation_passes():
    assert not checks.is_verdict(
        "Annex III, point 3(b) lists AI systems intended to be used to evaluate learning outcomes.")


def test_remove_verdicts_keeps_the_other_sentences():
    answer = "Annex III, point 3(c) covers level placement. Your placement test is high-risk."
    text, removed = checks.remove_verdicts(answer)
    assert removed == 1
    assert text == "Annex III, point 3(c) covers level placement."


# ---------------------------------------------------------------- personal data (KAN-165), synthetic values only

def test_phone_number_is_found():
    assert checks.has_personal_data("You can call me on +44 20 7946 0000")


def test_references_and_dates_are_not_personal_data():
    assert not checks.has_personal_data("Does Article 6(3) of Regulation (EU) 2024/1689 apply from 02.08.2026?")


def test_personal_data_question_gets_the_notice_without_the_value():
    kind, notice, _ = checks.input_check("My e-mail is test.user@example.com. Which provisions apply to our tool?")
    assert kind == "personal_data"
    assert "test.user@example.com" not in notice
