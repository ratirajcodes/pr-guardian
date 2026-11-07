# 90-second demo script

## Before recording

1. Create a Mattermost or Discord channel connected to the Switch room named `pr-guardian`.
2. Add all four agents from `switch/pr-guardian.template.yaml`.
3. Give every agent this repository as its working directory.
4. Keep `fixtures/pr-142.diff` open in the agent folder.

## The recording

**0:00–0:12 — problem and room**

Show the `#pr-guardian` room and say: “A normal PR review fragments context between developers, security, QA, and release owners. PR Guardian makes the review and human decision one shared workflow.”

**0:12–0:25 — developer request**

Post:

> @pr-intake Please review PR-142. It adds an endpoint for reindexing customer search after a migration. The diff is in `fixtures/pr-142.diff`; expected test command is `pytest`.

**0:25–0:45 — specialist handoff**

Show `@pr-intake` summarizing the request and addressing `@risk-reviewer` and `@test-reviewer`. Show the risk reviewer running the helper, then reporting that an `/admin` endpoint lacks explicit authorization evidence. Show the test reviewer reporting that no regression test appears in the diff.

**0:45–1:05 — decision card**

Show `@release-guardian` combining both reviews into a clear **HOLD** card with the exact remediation: add authorization enforcement and a regression test.

**1:05–1:20 — human checkpoint**

As the release owner, post:

> request changes — add an authorization test proving non-admin users receive 403, then return for review.

Show the guardian recording this decision. Say: “The agents surfaced evidence, but only the person responsible for the release made the decision.”

**1:20–1:30 — close**

Show the README architecture. Say: “Switch is essential here: it provides the room, specialist handoffs, shared evidence, and the human approval trail.”
