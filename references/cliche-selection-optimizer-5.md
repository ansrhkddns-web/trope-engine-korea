# Cliche Selection Optimizer 5

Use this file when the request asks for "고도화 진행5", candidate ranking, best cliche selection, or a more practical way to choose from many reference-derived cliches.

Phase 5 upgrades the engine from "compile a usable trope engine" to "select the best cliche portfolio for a specific brief." It assumes earlier references can generate many possible cards, then scores and filters those cards so the final set is familiar, fresh, scene-ready, serializable, and safe.

## Reference Basis

Do not copy examples from external references. Use them as abstract support families:

| Reference family | What to extract | How to use in Korean webnovels |
| --- | --- | --- |
| Trope catalogs | recurring device, recognition signal, expectation | make the reader recognize the promised pleasure quickly |
| Motif and tale-type indexes | small repeatable narrative element | convert motif into proof object, taboo, helper, pursuit, reward, or return |
| Propp-like functions | test, donor, interdiction, struggle, recognition, return | turn function order into reward loops and escalation beats |
| Dramatic situations | pressure relation such as pursuit, revenge, rescue, rivalry | stage conflict through gate, auction, duel, audit, hearing, contract, or broadcast |
| Progression/LitRPG grammar | visible quantified growth | make power, skill, rank, money, affection, or territory measurable |
| Korean regression/reincarnation/possession practice | second chance, desire repair, information asymmetry | give the protagonist active method, not just future knowledge |
| Trope-based story ideation research | trope as combinable story molecule | rank cards by fit and assemble them as a portfolio, not a raw list |
| Reader complaint signals | oversaturation, copy-paste start, passive advantage | add cost, witness change, institution reaction, and new consequence |

## Candidate Normalization

Normalize every candidate card before scoring.

```yaml
candidate_card:
  id:
  cliche:
  source_family:
  genre:
  role:
  recognition_signal:
  reader_reward:
  proof_object:
  witness:
  protagonist_action:
  cost_or_pressure:
  repeat_method:
  freshness_lever:
  copy_risk:
```

If any of `reader_reward`, `proof_object`, `witness`, `protagonist_action`, or `cost_or_pressure` is empty, the card cannot be ranked as ready. Repair it first or reject it.

## Scoring Axes

Score each candidate from 0 to 5.

| Axis | Weight | 5 means | 0 means |
| --- | ---: | --- | --- |
| recognition | 1.2 | reader understands the trope pleasure in one line | the card needs explanation |
| genre_fit | 1.3 | the card naturally belongs to the primary genre promise | it belongs to another genre's pleasure |
| reward_fit | 1.5 | it pays a core reward: power, money, status, revenge, knowledge, safety, relationship, recognition | reward is vague or private |
| proof_visibility | 1.4 | the reward can be shown through object, number, title, witness, access, or changed rule | the reward stays internal |
| protagonist_agency | 1.2 | advantage creates a choice or method | the protagonist merely receives luck |
| cost_integrity | 1.1 | the payoff creates a new pressure | cost is random punishment or absent |
| serial_durability | 1.3 | it can repeat with variation for 5+ episodes and scale for 50+ | one-shot gag or isolated reveal |
| freshness_pressure | 1.0 | variation changes scene pressure, witness, method, or consequence | only names are changed |
| originality_safety | 1.4 | no named setting, unique rule, signature sequence, or copied institution remains | it reads like a disguised existing work |
| package_alignment | 1.0 | title/logline/tag/opening can all sell the same promise | packaging would need a different promise |

Weighted score:

```text
total = sum(axis_score * weight)
max = 62
percentage = round(total / 62 * 100)
```

## Verdicts

| Percentage | Verdict | Meaning |
| ---: | --- | --- |
| 85-100 | select | strong enough for the core portfolio |
| 75-84 | support | usable as support, variation, or later-arc card |
| 60-74 | repair | keep only if one specific axis can be fixed |
| 0-59 | reject | do not use in the current engine |

When two cards have similar scores, prefer the card with stronger first-scene proof over the card with more lore.

## Genre Weight Overrides

Use the base weights unless the genre has a clear priority.

| Genre | Increase | Reduce slightly | Reason |
| --- | --- | --- | --- |
| hunter/gate | proof_visibility, witness, institution reaction | lore novelty | raids need visible proof and public reaction |
| tower/system | reward_fit, serial_durability, metric clarity | romance ambiguity | floor/quest systems need repeatable measurable progress |
| regression/finance | protagonist_agency, originality_safety, cost_integrity | pure omniscience | future knowledge becomes stale without risk and action |
| chaebol/corporate | proof_visibility, package_alignment, institution reaction | private training | money/status must be visible through deals, shares, access, or boards |
| murim/martial arts | recognition, escalation, honor witness | modern metric clarity | status, lineage, duel, and sect reaction carry the pleasure |
| academy | role coverage, rival witness, repeat_method | world mystery | tests and rankings must recur without becoming identical |
| possession/villain/extra | originality_safety, agency, relationship consequence | passive survival | the character must change the script through action |
| support/profession | proof_visibility, witness authority, reward_fit | combat spectacle | competence must be measurable and recognized |
| romance/rofan | relationship reward, social witness, cost_integrity | raw power scaling | emotional choice and public status must both move |

## Portfolio Selection Rules

Select a portfolio, not only top-scoring cards.

Minimum roles for a full engine:

- identity card;
- advantage card;
- proof card;
- witness/social reaction card;
- cost/pressure card;
- renewal or repeat-method card;
- antagonist or institution card;
- long-term hook card.

Selection constraints:

- Do not select more than two cards with the same proof object.
- Do not select more than two cards whose reward is only status.
- Include at least one card that creates cost from the protagonist's success.
- Include at least one witness with authority: association, guild, board, sect elder, professor, public ranking, media, court, imperial family, or market.
- Include at least one card that can be paid off inside the first scene.
- Include at least one card that opens a 50+ episode arena.
- If the genre is a combination, the primary genre must own identity, advantage, proof, and first witness.

## Redundancy And Conflict Checks

After ranking, remove cards that duplicate jobs.

| Problem | Sign | Repair |
| --- | --- | --- |
| proof redundancy | several cards all use rank test, duel, or auction | change one proof to rescue, audit, contract, broadcast, trial, or board vote |
| witness redundancy | every reward is private or seen by the same group | add rival, institution, public, enemy, or beneficiary witness |
| reward monotony | every payoff is status recognition | add money, safety, revenge progress, access, relationship, or knowledge |
| free-power stack | advantage has no price | add exposure risk, legal cost, debt, time limit, relationship loss, or institution control |
| genre split | support genre steals the first click | move support genre to episode 3+ or make it serve the primary reward |
| copy-like chain | institution, scene order, and rule system resemble one source | change at least two of institution, proof object, action, consequence, or timing |

## Ranking Output

Use this compact structure when presenting phase-5 selection.

```yaml
cliche_selection_optimizer:
  brief:
  primary_genre:
  source_families:
  candidate_count:
  selected_count:
  scoring_weights:
  selected_portfolio:
    - id:
      role:
      cliche:
      percentage:
      verdict:
      reason:
      proof_object:
      witness:
      cost_or_pressure:
      freshness_lever:
  rejected_or_deferred:
    - id:
      reason:
      repair_if_needed:
  portfolio_balance:
    missing_roles:
    duplicate_risks:
    strongest_first_scene_card:
    strongest_long_term_card:
  next_artifact:
```

## Repair Loop

If the best portfolio is below `select` level:

1. Repair proof first.
2. Repair protagonist agency second.
3. Repair cost from success third.
4. Repair witness authority fourth.
5. Repair long-term arena last.

Do not solve a weak portfolio by adding more cards. Replace or repair the weakest job.
