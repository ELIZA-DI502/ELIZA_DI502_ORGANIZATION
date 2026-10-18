# Jira sync: setup guide

Write your epics and user stories as markdown files in `docs/backlog/`. A GitHub Action turns them into Jira issues: one epic per file, with its stories, sub-tasks and tasks.

- **On a pull request**, the action checks the files and comments a plan ("would create 3 issues…"). Nothing is sent to Jira.
- **On merge to `main`**, it creates or updates the issues in Jira, puts new stories and tasks into their sprint, and commits the new issue keys back into the files.

## 1. What's in the package

| Path | What it is |
|---|---|
| `.github/workflows/jira-sync.yml` | The GitHub Action |
| `.jira/jira_sync.py` | The sync script (Python 3.10+) |
| `.jira/config.yml` | Settings: points scale, priorities, issue type names, labels |
| `.jira/team.yml` | Maps GitHub handles to Jira users |
| `.jira/requirements.txt` | Python packages for the script |
| `docs/backlog/_TEMPLATE.md` | The epic template, with one example of each model |
| `docs/JIRA_SYNC_SETUP.md` | This guide |

Copy all of these into your repository at the same paths, then commit and push them to `main`. GitHub only offers the manual "Run workflow" button once the workflow file is on the default branch.

## 2. Prepare Jira

You need a Jira Cloud project with the issue types **Epic**, **Story**, **Task** and a sub-task type (called "Subtask" or "Sub-task"). Scrum projects have these by default.

Check that these are switched on in your project settings:

- **Estimation with story points.** Stories need a story points field. In team-managed projects it's called "Story point estimate"; in company-managed projects it's usually "Story Points".
- **Story points on Tasks.** Needed only if your team uses Model B (story + Tasks). In company-managed projects, a Jira admin may need to make the story points field available on the Task issue type too.
- **Time tracking.** Lets sub-task estimates go into the "Original estimate" field. Without it, the sync writes the estimate into the sub-task's description instead.

- **A Scrum board with sprints.** New issues are placed into existing sprints named like `Sprint 3` or `DI Sprint 3` (your project key, then "Sprint" and a number). The sync never creates sprints: whoever runs sprint planning creates them on the board as usual. If the project has more than one Scrum board, put the right board's id in `board_id` in `.jira/config.yml`.

You don't need to work out the menus up front. In step 5 the **doctor** run lists exactly what is missing.

## 3. Create a Jira API token

One team member creates the token. Issues created by the sync show that person as reporter. They need permission to create issues in the project and to schedule issues (move them into sprints); team members normally have both.

1. Go to <https://id.atlassian.com/manage-profile/security/api-tokens>.
2. Choose **Create API token** (the plain one, not "with scopes"). Give it a name like `github-jira-sync` and pick an expiry date after the end of the semester.
3. Copy the token. You can't see it again later.

## 4. Configure the GitHub repository

### Variables and secrets

In the repository, go to **Settings → Secrets and variables → Actions**.

On the **Variables** tab, add:

| Name | Example | Notes |
|---|---|---|
| `JIRA_BASE_URL` | `https://your-team.atlassian.net` | No trailing slash |
| `JIRA_PROJECT_KEY` | `DI` | The prefix of your issue keys |

On the **Secrets** tab, add:

| Name | Value |
|---|---|
| `JIRA_EMAIL` | The Atlassian login email of the person who made the token |
| `JIRA_API_TOKEN` | The token from step 3 |

Never put the token in a file in the repository.

### Workflow permissions

The sync commits issue keys back to `main`. The workflow file asks for this permission itself, so most repositories need no change. If the "Commit issue keys back" step fails with a permission error:

- **Settings → Actions → General → Workflow permissions:** select *Read and write permissions*. Your organization may lock this setting; ask the owner if it's greyed out.
- **Branch protection on `main`:** if `main` only accepts changes through pull requests, the bot's push is rejected. Allow GitHub Actions to bypass the rule, or relax the rule for this bot.

### Team members

Edit `.jira/team.yml` so that every GitHub handle used in an Owner column maps to that person's Jira login email:

```yaml
alice-gh: alice@metu.edu.tr
bob-gh: bob@metu.edu.tr
```

If Jira hides someone's email, use their Jira account id instead. You find it at the end of their Jira profile URL.

## 5. Check the setup with the doctor

1. Open the repository's **Actions** tab and select **Jira sync** on the left.
2. Click **Run workflow**, keep the command on `doctor`, and click **Run workflow** again.
3. When the run finishes, open it and read the **Summary**.

The doctor checks the login, the project, the issue types, the fields each type accepts, the link type, the board and its sprints (including whether every Sprint value in your files matches a sprint), and every team member. Fix anything marked ❌ or ⚠️, then run it again.

## 6. Your first epic

1. Create a branch.
2. Copy `docs/backlog/_TEMPLATE.md` to a new file, for example `docs/backlog/DI-01-document-qa.md`. Files starting with `_` are never synced.
3. Replace the example content with your own epic. Leave every **Jira** cell empty.
4. Open a pull request. Within a minute or so, the action comments on it with errors, warnings and the planned changes. Push fixes until there are no ❌ errors. Your reviewers check the stories in the same pull request.
5. Merge. The **sync** job creates the issues and puts the stories and tasks into their sprints. Shortly after, a commit by `github-actions[bot]` fills in the Jira cells with links to the new issues.
6. Pull `main` before you edit the file again, so you have the keys.

## 7. Day-to-day rules

| You change… | Where |
|---|---|
| Titles, descriptions, acceptance criteria, priority, points, owners, estimates, Document Owner | **The markdown file.** On the next sync these overwrite what is in Jira. |
| Sprint of an issue that already exists | **Jira.** The markdown only decides the first sprint (see below). |
| Status, comments, attachments | **Jira.** The sync never touches these. |

### How sprints are set

- When a story or task is **created**, it goes into the sprint in its *Sprint* cell. If that cell is empty or the table has no Sprint column, it goes into the epic's *Release Target (Sprint)*. A Model B task with an empty Sprint cell uses its story's sprint.
- Sub-tasks always follow their story. Epics are never put in a sprint, since they span several.
- Sprint names are matched exactly first, then by number: `Sprint 3`, `DI Sprint 3` and `3` all find a sprint called `Sprint 3` or `DI Sprint 3`.
- **After that, the sprint is managed in Jira.** Moving a story to another sprint during planning is done on the board, and the sync never moves it back. Changing a Sprint cell later has no effect on that issue.
- If the sprint doesn't exist yet, or is already closed, the issue stays in the backlog and the summary says why. Once the sprint exists, the next sync places it, unless someone has already planned it in Jira.
- Issues created before sprint support was added are left where they are.

### The epic's owner

The *Document Owner* (one GitHub handle from `team.yml`) becomes the epic's assignee in Jira. Changing it in the markdown changes the assignee on the next sync.

### Keeping Jira and the markdown in step

Every sync run ends with a summary that compares the two:

- **Deleted in Jira but still in the markdown:** the sync can't update an issue that no longer exists, so that item is marked as failed and the run turns red. The other items still sync. Delete the row and its section from the markdown, or empty its Jira cell if you want it created again.
- **In Jira but no longer in the markdown:** a synced issue whose row you removed. The sync never deletes issues; close or delete it in Jira if that was the intent.
- **Created in Jira, not in the markdown:** issues someone added by hand under a synced epic, plus open issues that have no epic at all (marked "no epic"). That's fine for bugs and quick chores. Stories belong in the markdown, so add them there; until then they exist only in Jira and the sync ignores them.

- **Don't edit or delete the Jira cells.** The key is how the sync knows an issue already exists. If you delete a key, the next sync creates a duplicate issue.
- **Removing a row doesn't delete the issue.** The sync summary lists issues that exist in Jira but not in any file. Close or delete them in Jira yourself.
- **To move a story to another epic**, move its row and its section, keys included, into the other epic's file. The story's parent is updated on the next sync. Sub-tasks stay with their story.
- **Tasks that belong to no story** go in the epic file's `## Other tasks` table (columns: Task, Owner, Points, Sprint, Jira). They become Tasks under the epic, with no link to a story, and are placed in their Sprint cell's sprint or the epic's Release Target. Work that belongs to no epic at all, like quick bugs or admin chores, can be created directly in Jira; the sync summary lists it under "Created in Jira".
- **Nothing is skipped silently.** A table or a "Tasks", "Sub-tasks" or "Acceptance criteria" heading outside a story section or `## Other tasks` fails the pull request check, so a task can't be lost by putting it in the wrong place. Other tables (for example a reference table in the notes) only produce a warning.
- **One breakdown per story.** Use a *Sub-tasks* table (Model A: the story carries the points) or a *Tasks* table (Model B: the tasks carry the points and the story's Points cell stays empty), never both.
- **Unchanged items are skipped.** The sync stores a fingerprint on each issue, so a run without edits doesn't touch Jira. To push everything again anyway, run the script locally with `--force`, or temporarily add `--force` to the sync step.

## 8. Checking files on your own computer

```bash
pip install -r .jira/requirements.txt
python .jira/jira_sync.py validate
```

This runs the same check as the pull request and needs no Jira access. To run `sync` or `doctor` locally, first set the four `JIRA_*` values as environment variables.

## 9. Troubleshooting

| Symptom | Likely cause and fix |
|---|---|
| `Missing environment variable JIRA_BASE_URL` | The variable is missing or misspelled (step 4). Variables and secrets are on separate tabs. |
| `HTTP 401` | Wrong email or token, or the token expired. Create a new token and update the secret. |
| `HTTP 403` or `HTTP 404` on the project | The token owner can't see the project, or `JIRA_PROJECT_KEY` is wrong. |
| `... is not available on task issues; skipped` | That field isn't on the issue type's screen. Run the doctor; ask a Jira admin to add the field. |
| `Jira requires fields this sync doesn't fill` | The project has extra required fields. Make them optional, or give them a default value. |
| `Sprint 'Sprint 3': no sprint matching ...` | Create the sprint on the board, or fix the name in the markdown. The issue waits in the backlog and is placed on the next sync. |
| `no Scrum board found` | The project has only a Kanban board, or the token owner can't see the board. Set `board_id` in `.jira/config.yml`, or plan sprints in Jira by hand. |
| `HTTP 403` when placing an issue in a sprint | The token owner lacks the "Schedule issues" permission in the project. |
| `... no longer exists in Jira` | The issue was deleted in Jira. See *Keeping Jira and the markdown in step* in section 7. |
| `No single Jira user found for @handle` | The email in `team.yml` doesn't match a Jira user, or Jira hides it. Use the account id. |
| Pull request comment missing | Pull requests from forks get no comment (no access to secrets or write permission). The job summary still shows the result. |
| "Commit issue keys back" fails | See *Workflow permissions* in step 4. The issues were created, but their keys weren't saved to the files. Fix the permission, delete the new issues in Jira (the run's summary lists their keys), then choose **Run workflow → sync**. Without deleting them first, you get duplicates. |
