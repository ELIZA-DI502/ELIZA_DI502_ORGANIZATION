# Learning spike: Gözde Nur

**Sprint:** 1 (14/10–28/10/2026) · **Goal:** close my gaps in the Sprint 1 fundamentals from the [Online Course Register](../../online-course-register/README.md)

## Where I start

I compared my knowledge with the "Sprint 1 fundamentals" table in the Online Course Register.

| Topic | My level before Sprint 1 | What I do in Sprint 1 |
|---|---|---|
| LLM basics | Known from the NLP course at METU Informatics Institute (IS 584) | – |
| Embeddings & vector search | Known from IS 584 | – |
| RAG | Known from IS 584 | – |
| Evaluation basics | Known before the project | – |
| Python environment | Known; I use virtual environments and `requirements.txt` | – |
| Scrum basics | New to me | Read the course resource "What is Scrum?" (done) |
| Git & GitHub | I use Git, but not often in a team | Refreshed branches and pull requests (done) |
| Prompt engineering | I had not written prompts for a RAG system | Read two short guides (done) |
| Chat interface (Gradio) | I have not used Gradio | Not needed: the team chose React for the interface (see section 4) |

## 1. Scrum basics

**Source:** Scrum.org, ["What is Scrum?"](https://www.scrum.org/resources/what-scrum-module) (resource given in the Online Course Register)

**What I learned:**

- Scrum has three roles: the Product Owner (decides what is built first), the Scrum Master (helps the team follow Scrum) and the Developers (do the work).
- Work is done in sprints. Each sprint has planning at the start, and a review and a retrospective at the end. Our sprints are two weeks long.
- A user story is a need of a user ("As a …, I want …, so that …"). A task is a piece of work the team does. A spike is a short, timeboxed piece of learning or research, like this note.

## 2. Git & GitHub

**Source:** GitHub Docs, ["Hello World"](https://docs.github.com/en/get-started/start-your-journey/hello-world)

**What I already did in our project:** created the team repository, invited the team members, and added a workflow that brings the course template updates into our repository.

**What I refreshed:** how to create a branch, commit changes to it, open a pull request and merge it into `main`. In our repository, changes to the charter pages go through a branch and a pull request, and every branch and commit contains a Jira key (for example `KAN-14`).

## 3. Prompt engineering

**Course Register goal:** "Write a prompt that tells the model to answer only from the given passages and to say when it does not know."

**Sources:**

- Anthropic, ["Prompt engineering overview"](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- DAIR.AI, [Prompt Engineering Guide](https://www.promptingguide.ai/)

**What I learned:**

- Be clear and direct
- Zero-shot and few-shot prompts
- Chain-of-thought
- Separate the parts of the prompt
- Allow "I don't know"

**How we will use this in ELIZA:** our prompt will (1) give the retrieved provisions in a marked section, (2) tell the model to answer only from them and to cite the Article or Annex for every statement, (3) let the model say "The provided text does not answer this question" when the provisions do not answer, and (4) tell the model never to say whether a product is compliant, prohibited or high-risk. We can add one or two example answers (few-shot) if the answer format is not stable. The prompt will be a file in `prompts/` and will be tested on the D2 evaluation set.

## 4. Chat interface (Gradio)

**Source:** Gradio documentation, ["Creating a chatbot fast"](https://www.gradio.app/guides/creating-a-chatbot-fast)

**What Gradio is:** a Python library that builds a simple web chat page in a few lines of code. It was one of the interface options in Spike 01.

**Outcome:** not needed. The team chose React (with a Node.js backend) for the interface in the System Design Document, so I did not build the Gradio "hello world". My Sprint 1 work moved to the NLP part instead: the [model selection spike](model-selection-spike.md) and the NLP decisions D7–D12 in the System Design Document.
