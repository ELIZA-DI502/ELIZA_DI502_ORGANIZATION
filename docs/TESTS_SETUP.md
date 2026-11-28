# Unit tests and GitHub Actions: guide

The unit tests in `tests/` check the rule-based parts of the RAG service (`rag/app/checks.py`): the input check (evasion, out of scope, personal data) and the output check (verdicts, citations). A GitHub Action runs them on every pull request and on every push to `main`, so everyone sees whether a change keeps them passing.

- **On a pull request to `main`**, the action runs all tests and shows the result on the pull request.
- **On a push to `main`** (also a merge), it runs them again on `main`.
- **On demand**, it can be run by hand from the *Actions* tab.

Added in [KAN-140](https://yarengursoy.atlassian.net/browse/KAN-140), following the instructor's Sprint 3 feedback on testing: unit tests for functions, tests in `tests/`, and a CI pipeline that runs them when a pull request is opened.

## 1. What's in the repository

| Path | What it is |
|---|---|
| `.github/workflows/tests.yml` | The GitHub Action |
| `pytest.ini` | Settings of pytest: tests are in `tests/`, the repository root is on the Python path (KAN-234) |
| `tests/test_checks.py` | Unit tests of the input and output checks (KAN-234, KAN-148) |
| `tests/test_out_of_scope.py` | Unit tests of the out-of-scope detection (KAN-140, story KAN-5) |
| `rag/app/checks.py` | The code under test |

## 2. What the action does

On every run, on a fresh Ubuntu machine on GitHub:

1. Checks out the branch of the pull request (or `main`).
2. Installs Python 3.12, the version of `rag/Dockerfile`.
3. Installs only `pytest==9.2.0` and `pyyaml==6.0.3`, the versions of `requirements.txt`. The checks under test need no model, no Ollama and no vector store, so the heavy packages of `requirements.txt` (torch, chromadb, …) are not installed. A run takes about one minute.
4. Runs `python -m pytest -v` from the repository root.

The action only reads the repository (`permissions: contents: read`). It does not change any file, does not comment and does not touch Jira. The other actions (`jira-sync.yml`, `confluence-sync.yml`, `hoca-sync.yml`) are separate and work as before. GitHub Actions is free for a public repository.

## 3. Reading the result

On the pull request, under the description, the check **Tests / unit-tests** shows one of:

| Mark | Meaning | What to do |
|---|---|---|
| 🟡 dot | The tests are running | Wait about one minute |
| ✅ green tick | All tests pass | Nothing; the pull request can be reviewed and merged |
| ❌ red cross | At least one test fails | See section 4 |

The same mark appears next to each commit on `main` after a push or merge. The person who opened the pull request also gets an e-mail from GitHub when the tests fail.

## 4. When a test fails

The action does not change or delete anything. It only shows that something is wrong.

1. **Find the failing test.** Click **Details** next to the red cross. The log shows the name of every failing test and what it expected, for example:
   ```
   FAILED tests/test_out_of_scope.py::test_partly_out_of_scope_question_goes_on_to_the_model
   assert 'out_of_scope' is None
   ```
   Here the test expected the question to go on to the model (`None`), but the check returned the out-of-scope notice.
2. **Decide what is wrong.**
   - **The code is wrong** (the change broke a behaviour that a story asks for): fix the code on the same branch.
   - **The test is out of date** (the behaviour was changed on purpose, for example after a story's acceptance criteria changed): update the test on the same branch, and say why in the pull request.
3. **Push the fix to the same branch.** The tests run again by themselves on every new commit; when they pass, the cross turns into a green tick.
4. **If a test fails on `main`** (a red cross next to a commit on `main`), the last merge broke something: open a pull request with the fix.

Merging is not blocked by a red cross (see section 7). The reviewer should not approve a pull request with a red cross unless the pull request says why.

## 5. Running the tests on your own computer

Not needed for a pull request, because the action runs them. To run them before you push:

```bash
pip install pytest==9.2.0 pyyaml==6.0.3     # or: pip install -r requirements.txt
python -m pytest -v                         # from the repository root
```

To run one file or one test:

```bash
python -m pytest tests/test_out_of_scope.py -v
python -m pytest -k partly_out_of_scope -v
```

## 6. Adding a test

1. Put the test in `tests/`, in a file whose name starts with `test_` (for example `tests/test_sources.py`). pytest finds it by itself; the action needs no change.
2. Write each test as a function whose name starts with `test_`, with `assert` for what must be true. Name the story and the test case it comes from in a comment, for example `# TC-5.3 of KAN-5`.
3. Take the test questions from the story's test cases or write new edge cases. **Do not copy questions from the evaluation set** (`docs/eval/`), and never from the `test` split: the rules must not be tuned on the evaluation questions (KAN-185).
4. If the new test needs another package, add it with its version to the `pip install` line of `.github/workflows/tests.yml` and to `requirements.txt`.
5. Run the tests (section 5) or open the pull request and check that the action is green.

## 7. Blocking a merge when the tests fail (optional)

By default the action only shows the result; a pull request with a red cross can still be merged. To make passing tests a condition for merging, a repository admin sets a branch protection rule:

1. **Settings** → **Branches** → **Add branch protection rule** (or **Add rule**).
2. **Branch name pattern:** `main`.
3. Tick **Require status checks to pass before merging**, search for **unit-tests** and select it.
4. **Create** (or **Save changes**).

This matches the instructor's note that a pull request must pass the tests before it is merged. Whether to turn it on is a team decision.

## 8. What these tests do not cover

The unit tests check the rule-based code only. They do not call the answer model, the embedding model or the vector store, so they do not measure answer quality. That is measured by the evaluation runs on the `val` split (`src/evaluation.ipynb`, Weights & Biases) and, at the end, on the `test` split. Integration tests of the services (retrieval, LLM requests) would need Ollama and the vector store on the GitHub machine and are not part of this action.
