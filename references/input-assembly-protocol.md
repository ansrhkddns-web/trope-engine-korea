# Input Assembly Protocol

Use this file when the user gives a vague request, many genre keywords, a rough premise, or only says to make something "commercial", "familiar but fresh", "Korean webnovel style", or "cliche-rich".

## Goal

Convert messy input into a usable trope engine without asking too many questions. Ask only when the primary genre or requested output is impossible to infer.

## Input Triage

Classify the user's request:

| User input type | What to infer | Best output |
| --- | --- | --- |
| Genre keywords only | primary engine, support engine, reward channels | quick trope pack |
| One-line premise | promise, protagonist advantage, first proof | familiar-but-fresh premise |
| Existing outline | weak axis, missing reward, stale trope | diagnosis and revision |
| Many genre devices | primary/support/delayed engines | combination board |
| "Make it commercial" | reward cadence, proof, package promise | reward engine + first 5 episodes |
| "Make it new" | familiar core, preserved reward, variation axes | freshness pass |
| Title/intro request | promise, keywords, first proof, tags | product package |
| Long series request | escalation, enemy ladder, institution reaction | 1-50 episode map |

## Default Assumptions

If the user gives little information:

- Use Korean commercial webnovel defaults.
- Prefer action-visible genre proof over lore.
- Choose one primary genre and one support genre.
- Give the protagonist one unfair advantage and one early weakness.
- Put a public proof scene in episode 1.
- Include a repeatable reward loop and a 1-5 episode proof plan.
- Include a warning if assumptions may be wrong.

## Assembly Steps

1. **Extract keywords**
   - genre devices: gate, tower, system, regression, chaebol, sect, demonic cult, academy, possession, revenge
   - protagonist state: weak, ruined, extra, illegitimate child, porter, failed disciple, low-rank hunter
   - advantage: memory, hidden skill, appraisal, contract, manual, land, money, future knowledge
   - desired feeling: revenge, growth, money, survival, recognition, comedy, dark, catharsis

2. **Assign jobs**
   - Primary genre: first click and first proof.
   - Support genre: reward variety or institution pressure.
   - Flavor genre: delayed spice after the first reward is proven.

3. **Build the minimum viable engine**
   - Reader promise:
   - World engine:
   - Protagonist advantage:
   - First proof:
   - Repeating reward:
   - Institution reaction:
   - First enemy:
   - First hook object:

4. **Add proof and consequence**
   - Every advantage needs a scene where it is used.
   - Every reward needs a witness, object, or changed access.
   - Every big reward should create a cost, debt, suspicion, contract, or enemy move.

5. **Choose output template**
   - Use `output-templates.md` for exact structure.
   - If the user did not specify a format, use quick trope pack plus first proof scene and risk/fix.

## Inference Rules

- If the request includes `회귀`, default the protagonist's first win to information advantage unless the user names another advantage.
- If the request includes `헌터`, default the first proof to rank/gate/raid/rescue.
- If the request includes `재벌`, default the first proof to a small decisive deal, boardroom reversal, land, stock, or subsidiary.
- If the request includes `무협`, default the first proof to duel, test, manual insight, poison reversal, or elder recognition.
- If the request includes `탑` or `시스템`, default the first proof to hidden condition, tutorial exploit, title, or ranking anomaly.
- If the request includes `마교`, decide whether the demonic side is the protagonist's faction, temptation, false accusation, or ideological contrast.
- If the request includes `정파`, decide whether it is a genuine order, corrupt institution, rival legitimacy, or public mask.
- If the request includes `기연`, attach a price, owner, debt, curse, political risk, or future consequence.

## Ask Only These Questions When Necessary

Ask one concise Korean question if:

- primary genre cannot be inferred;
- the user asks for "current trend" but platform/genre scope is missing;
- the user wants diagnosis but provides no premise/outline;
- the request depends on a specific existing work but the user has not provided enough details to abstract safely.

Otherwise, state assumptions and proceed.

## Minimum Output for Vague Requests

Include:

- **제가 잡은 방향**:
- **전제/가정**:
- **메인 장르와 보조 장르**:
- **독자 약속**:
- **주인공 우위**:
- **1화 증명 장면**:
- **클리셰 카드 5개**:
- **신선한 변주 3개**:
- **1-5화 보상 흐름**:
- **위험과 보완**:
