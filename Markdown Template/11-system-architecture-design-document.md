# System Architecture Design Document

**Note: this document uses HTML tags to disable rendering of instructions. View the raw file for further details.**

<!--
How to use this template
- Start short and update the document every sprint. It is a working document, not a finished blueprint [1] [2].
- Propose changes through pull requests [2]. After merge, this page is published to Confluence, where instructors and peer reviewers comment.
-->

| Team | Sprint | Status | Last updated | Updated by | 
|---|---|---|---|---|
|  |  | proposed | yyyy-mm-dd | |

<!--
Status [2]:
- proposed: drafted, waiting for feedback
- accepted: reviewed and agreed; work can start
- revised: changed after feedback or a new decision (see Change log)
- implemented: built as described
-->

## 1. Summary

<!--
One paragraph anyone can follow: what the system does, its main parts, and how they work together [1].
Link to the charter instead of restating it.
-->

## 2. Goals and non-goals

### Goals

<!-- The charter objectives this design serves, with links to their success criteria [1]. -->

### Non-goals

<!-- What this design leaves out on purpose [1]. -->

## 3. System architecture diagram

<!--
ISO/IEC 5338: 6.4.4 System architecture definition process.
Show which technologies you use and how they connect. Update the diagram as the design changes; give each version a number and date.
Label each box with the component and its technology. Label each arrow with what passes along it.

Use one tool and delete the other option below:
- Miro: https://miro.com/diagramming/software-architecture-diagram/
  Export the board as PNG into docs/images/, embed it, and link the board.
- Mermaid flowchart: https://mermaid.js.org/syntax/flowchart.html
  Write the diagram in a ```mermaid block.
-->

**Version:** v1 (yyyy-mm-dd)

**Option A: Miro**
[Miro board](https://miro.com/)

**Option B: Mermaid** (replace the example)

```mermaid
flowchart LR
    user(["AI user"]) -->|request| ui["Frontend<br/>technology"]
    ui -->|API call| api["Backend<br/>technology"]
    api -->|input| model["Model service<br/>model name and version"]
    api -->|query| store[("Data store<br/>technology")]
    subgraph offline ["Offline data pipeline"]
        source[("Data source")] -->|raw data| prep["Preprocessing<br/>technology"]
    end
    prep -->|cleaned data| store
```

## 4. Components

<!-- One row per box in the diagram. -->

| Component | Responsibility | Technology and version | SBOM entry |
|---|---|---|---|
|  |  |  |  |

## 5. Design details

### Data pipeline

<!-- Sources, cleaning, labelling, splits, storage, and how data reaches the model. ISO/IEC 5338: 6.4.8 AI data engineering process. -->

### Model

<!-- How the model is selected, trained, tuned or prompted. ISO/IEC 5338: 6.4.9 Implementation process. -->

### Evaluation

<!-- Metrics, the baseline you compare against, and how validation data is kept separate from test data. ISO/IEC 5338: 6.4.11 Verification process. -->

### Interfaces

<!-- One row per arrow in the diagram. ISO/IEC 5338: 6.4.10 Integration process. -->

| From | To | What passes | Format or protocol |
|---|---|---|---|
|  |  |  |  |

### Deployment

<!-- Where each component runs (e.g. a laptop, a university server, a cloud service) at which stage (internal testing versus MVP) and how users reach the system. List the resources themselves in Facilities & Resources. ISO/IEC 5338: 6.4.12 Transition process. -->

## 6. Decisions

<!--
This section is the project's technical decision log. (ISO/IEC 5338: 6.3.3 Decision management process.)
One record per technology choice and per major design choice [2].
Also record later AI decisions here, such as retraining or resetting the model, or changing what it is specified to do.
Decisions that change the charter (scope, deliverables, milestones) go into a new charter version instead.
For a model choice, keep per-model details (version, used or rejected and why) in the AI-BOM and link its row here.
List the simplest option you considered too, such as the baseline or "do nothing" [1].
If an experiment settled the choice, link its experiment card and AI SBOM row.
Do not rewrite a past decision. Mark it superseded and add a new record [2].
Copy the block below for each decision.
-->

### D1: <decision title>

**Context:**

**Options considered:**

| Option | Pros | Cons |
|---|---|---|
|  |  |  |

**Decision:**

**Why:**

**Consequences:**

**Evidence:**

**Owner and date:**

**Status:** proposed / accepted / superseded by D?

## 7. Open design areas

<!-- Areas where a decision is still needed, and which spike in docs/spikes/ will settle it [2]. When the spike ends, record its outcome as a decision in section 6 and remove the area from this list. -->

## 8. Change log

| Version | Date | Change | Pull request |
|---|---|---|---|
| v1 | yyyy-mm-dd | First version |  |

## Checklist before submitting

- [ ] Every box in the diagram has a row in Components, and every row has a box.
- [ ] Every arrow in the diagram has a row in Interfaces.
- [ ] Every technology in Components appears in the SBOM under the same name and version.
- [ ] Every technology in Components has a decision in section 6.
- [ ] Every relevant spike has a decision in section 6, or a note in Open design areas saying why not.
- [ ] The diagram version matches the latest change log entry.

## References

[1] GitLab Inc. "Design document template" (`_template.md`). The GitLab Handbook. https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/main/content/handbook/engineering/architecture/design-documents/_template.md

[2] GitLab Inc. "Architecture Design Workflow." The GitLab Handbook. https://handbook.gitlab.com/handbook/engineering/architecture/workflow/

Diagram tools: [Miro, software architecture diagrams](https://miro.com/diagramming/software-architecture-diagram/) · [Mermaid, flowchart syntax](https://mermaid.js.org/syntax/flowchart.html)
