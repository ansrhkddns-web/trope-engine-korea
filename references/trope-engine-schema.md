# Trope Engine Schema

Use this file when producing a durable concept bible, reusable trope pack, or anything the user may continue across turns. The goal is to keep outputs stable enough to become a project asset.

## Canonical Spec

Create or update these fields:

| Field | Purpose |
| --- | --- |
| `project_signal` | title direction, genre promise, expected reader pleasure |
| `genre_stack` | primary engine, support engine, delayed flavor engines |
| `reader_contract` | reward channels, visible proof, payoff cadence |
| `protagonist_engine` | starting wound, unfair advantage, active method, limitation |
| `world_engine` | rule that repeatedly creates incidents |
| `institution_map` | who measures, blocks, buys, punishes, or rewards value |
| `trope_stack` | selected cliche cards and their jobs |
| `first_proof_scene` | episode 1 proof with pressure/action/proof/witness/cost |
| `reward_ledger` | promises opened, paid, delayed, and at-risk |
| `escalation_ladder` | personal -> institution -> region -> nation/world/system |
| `product_package` | title, logline, tags, first 5 episode promise |
| `originality_safety` | reference abstraction and copy-risk checks |
| `production_handoff` | next artifact to create: bible, episode map, brief, or prose packet |

## Compact YAML-Like Shape

Use this shape when the user asks for a clean reusable spec. It is not strict machine YAML; readability matters.

```yaml
project_signal:
  title_direction:
  one_line_promise:
  target_reward:
genre_stack:
  primary:
  support:
  delayed_flavors:
reader_contract:
  reward_channels:
  visible_proof:
  first_small_payoff:
  first_large_payoff:
protagonist_engine:
  starting_wound:
  unfair_advantage:
  active_method:
  limitation_or_cost:
world_engine:
  repeated_incident_rule:
  scarcity_or_pressure:
institution_map:
  measuring_body:
  market_or_public:
  enemy_institution:
trope_stack:
  approved_cards:
  restricted_cards:
first_proof_scene:
  pressure:
  action:
  proof_object:
  witness:
  reward:
  cost_or_hook:
reward_ledger:
  opened:
  paid:
  debt:
escalation_ladder:
  episodes_1_5:
  episodes_6_25:
  episodes_26_50:
  after_50:
product_package:
  title_candidates:
  logline:
  tags:
originality_safety:
  copy_risk:
  transformed_elements:
production_handoff:
  next_artifact:
  next_questions:
```

## Completion Rules

- Do not leave `first_proof_scene` empty.
- Do not list trope cards without assigning a job.
- Do not list rewards without proof objects.
- Do not list a support genre unless it changes institution, reward, cost, or witness.
- Mark assumptions instead of pretending unknown details are confirmed.
- If the user asks for quick ideation, use only the compact fields; if they ask for a bible, use the full shape.

## Update Rules

When revising an existing spec:

- Preserve useful decisions unless the user asks to reset.
- Mark replaced cliches as `restricted_cards` if they should not return.
- Update reward ledger when hooks or promises change.
- Update product package if the core promise changes.
- Update escalation ladder if the first proof changes.
