# Mode Playbooks

Use this file when deciding how to run the skill for a specific user request. It keeps the skill from loading too many references or producing a mismatched output.

## Mode Selection

| User request | Primary mode | Load first | Optional add-ons |
| --- | --- | --- | --- |
| "헌터+회귀 클리셰 팩" | trope pack | `default-genre-settings.md`, `trope-card-library.md` | `reader-reward-model.md`, `variation-engine.md` |
| "익숙하지만 새롭게" | freshness pass | `variation-engine.md` | `scene-proof-bank.md`, `failure-patterns.md` |
| "이 아이디어 진단" | diagnosis | `diagnostics-rubric.md` | `failure-patterns.md`, `reader-response-simulation.md` |
| "제목/소개글/태그" | product package | `product-packaging.md` | `scene-proof-bank.md`, `reader-reward-model.md` |
| "1화 장면" | proof scene | `scene-proof-bank.md` | `reader-reward-model.md`, `episode-hook-designer` if episode hooks dominate |
| "50화까지" | escalation map | `escalation-ladders.md` | `trope-engine-schema.md`, `production-handoff.md` |
| "바이블로 정리" | structured spec | `trope-engine-schema.md` | `production-handoff.md`, `output-templates.md` |
| "독자 반응" | reader response | `reader-response-simulation.md` | `diagnostics-rubric.md`, `product-packaging.md` |
| "유명작 느낌" | originality safety | `originality-safety.md` | `variation-engine.md`, `scene-proof-bank.md` |
| "요즘 잘 먹히는" | market reference | `market-research-protocol.md` | current web research, then stable references |

## Output Size Rules

- For quick ideation, use 5-8 sections, not a full bible.
- For a complete concept, include first proof, reward loop, cliche stack, and 1-5 episode path.
- For a bible or long-running plan, include the standard schema and production handoff.
- For diagnosis, lead with judgment and fixes, then details.
- For packaging, do not overload with lore; show title promise, logline, tags, and first 5 episodes.

## Reference Loading Rules

- Do not read every reference for normal requests.
- Load `output-templates.md` only when the final structure matters.
- Load `trope-engine-schema.md` only when continuity or reuse matters.
- Load `market-research-protocol.md` only for current trends or platform-specific requests.
- Load `originality-safety.md` whenever a named reference work appears.
- Load `failure-patterns.md` when the result feels generic, bloated, too easy, or not serializable.

## Mode Playbooks

### Quick Trope Pack

Use when the user wants ideas fast.

Steps:

1. Pick primary and support genre.
2. State reader promise.
3. Select 5 cliche cards.
4. Give one fresh variation for each.
5. Build one first proof scene.
6. Add repeatable reward loop and risk/fix.

Avoid:

- long market explanation;
- 50-episode roadmap unless requested;
- too many named institutions.

### Full Concept Engine

Use when the user wants a usable premise.

Steps:

1. Use input assembly if vague.
2. Pick genre stack.
3. Build protagonist engine.
4. Define world/institution engine.
5. Select trope stack.
6. Build first proof scene.
7. Add reward ledger.
8. Add 1-5 episode proof path.
9. Add package direction.

Avoid:

- ending without a proof scene;
- listing tropes without jobs;
- adding novelty that removes the core reward.

### Diagnosis

Use when the user provides an idea, outline, or existing plan.

Steps:

1. Score critical axes.
2. Identify the first failure pattern.
3. Name the biggest drop-off risk.
4. Preserve one strong part.
5. Give a concrete repair.
6. Rewrite the first proof scene if needed.
7. End with a work order.

Avoid:

- vague praise;
- rewriting everything when one repair will work;
- diagnosing style before engine.

### Product Package

Use when the user asks for title, intro, tags, sales copy, or first-screen promise.

Steps:

1. Identify title promise.
2. Align logline and tags to the same reward.
3. Confirm opening scene proves the promise.
4. Build first 5 episode package path.
5. Flag mismatch.

Avoid:

- poetic titles that hide the genre;
- tags that the first 5 episodes do not support;
- intro copy that depends on unexplained lore.

### Production Handoff

Use when the user wants to continue into writing.

Steps:

1. Preserve stable decisions in schema.
2. Name the next artifact.
3. List non-negotiable promise.
4. List approved/restricted cliche cards.
5. List first proof and reward ledger.
6. Give next 3 tasks.

Avoid:

- reopening already-set decisions without reason;
- handing off only vibes;
- omitting must-avoid items.

## Default Final Section

For substantial outputs, end with:

- **다음 작업**: the next artifact or edit.
- **잃으면 안 되는 것**: the core reader promise.
- **주의할 것**: the highest risk.
