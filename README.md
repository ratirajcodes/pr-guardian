# PR Guardian

PR Guardian is a Switch room where a developer, specialist review agents, and a release owner turn a pull request into an auditable release decision.

It targets the **Best Business Workflow** track of the Flip the Switch Hackathon. Switch is central: it is the shared room where review agents receive the request, hand findings to each other, and wait for a human approval before a release decision is recorded.

## The problem

Pull-request review is fragmented. A developer waits for several specialists, reviewers repeat the same context, and important release decisions disappear in chat. PR Guardian gives each specialist a clear job and turns the final human decision into a reusable release record.

## Workflow

```text
Developer posts PR link and goal
          |
          v
PR Intake Agent ----> Risk Reviewer ----> Test Reviewer
          |                   |                 |
          +-------------------+-----------------+
                              v
                    Release Guardian summary
                              |
                   human approves / requests changes
                              |
                              v
                      final release decision
```

1. A developer addresses `@pr-intake` with a PR URL, goal, and test command.
2. Intake establishes scope and assigns risk and test reviews in the same Switch room.
3. Review agents return evidence-based findings, calling the included local review helper when a fixture or checked-out repository is available.
4. `@release-guardian` creates a decision card. It **cannot approve or release**; it asks the release owner for an explicit decision.
5. The human replies `approve`, `hold`, or `request changes`. The guardian posts the final auditable decision.

## What is included

- `switch/pr-guardian.template.yaml` — a ready-to-import Switch room template and agent briefs.
- `scripts/review_pr.py` — deterministic local helper that produces a compact PR evidence report from a unified diff.
- `fixtures/pr-142.diff` — a deliberately risky sample change used in the demo.
- `demo/demo-script.md` — a 90-second recording plan and exact prompts.

## Run the local evidence helper

No packages are required.

```powershell
python scripts/review_pr.py fixtures/pr-142.diff
```

The sample report identifies a security-sensitive change and a missing test signal. In a real project, give the agent a checked-out repository and have it run the project’s real tests alongside this structured review.

## Set up in Switch Console

1. Install Docker and Switch Console, then create a local Switch server and use its included Mattermost room. The official Switch quickstart describes the setup.
2. Create the `pr-guardian` room and three agents using the names and briefs in `switch/pr-guardian.template.yaml`. Choose your existing coding-agent provider for each.
3. Add yourself as `release-owner` in the room description. Keep `release-guardian` limited to preparing a decision; only the human makes the final approval.
4. Copy the included demo prompt into the room, address `@pr-intake`, and record the interaction.

The Switch console supports agents that run from a local folder. Point all three agents to this repository so they can read the fixture and run `scripts/review_pr.py`.

## Why this is a Switch project

The project is not a standalone PR-review bot. It requires Switch rooms to give people and agents one shared context, route specialist handoffs by mention, and make the release owner’s approval part of the same decision record. Removing Switch removes the cross-agent workflow and the human checkpoint.

## Demo outcome

For the included sample, PR Guardian recommends **HOLD**: the diff adds an admin-sensitive endpoint without a corresponding authorization test. The release owner requests changes; after a test is added, the guardian can present an approval-ready card.

## Submission checklist

- [ ] Repository URL
- [ ] 90-second demo video
- [ ] README with the setup and architecture above
- [ ] Screenshot showing the Switch/Mattermost room and named agents
- [ ] One clear before/after story: unstructured review to human-approved release decision
      
## Demo

[Watch the PR Guardian demo on YouTube](https://youtu.be/zQur8TIrPsg)
