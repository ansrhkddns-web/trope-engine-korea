# Serial Arc Deployment Planner 7

Use this file when the request asks for "고도화 진행7", serial deployment, episode operation, arc deployment, cliche placement across episodes, reward scheduling, hook cadence, or turning a reader-tested trope engine into a usable 1-50 episode operating plan.

Phase 7 upgrades the engine from "reader-tested cliche portfolio" to "serial deployment plan." It places selected cliches into episode jobs, tracks reward debt, rotates proof and hook types, and creates repair checkpoints so the engine can survive actual serialization.

## Reference Basis

Do not copy examples from external references. Extract operational principles:

| Reference family | What to extract | Skill use |
| --- | --- | --- |
| Serial fiction and cliffhanger research | next-installment desire, unresolved question, payoff before hook | build fair episode endings and paid boundaries |
| Korean webnovel narrative-form research | episode-level interest, readability, immediacy, commodity logic | make each episode carry a visible reward and next-click pressure |
| Narrative planning research | causal event chains, character intention, plot coherence | ensure each episode follows from the previous win or cost |
| Trope-based story ideation research | trope cards as recombinable units | deploy selected cards as scheduled engine parts |
| Reader feedback calibration | likely praise, complaints, fatigue point | place repair checkpoints before fatigue becomes structural |
| Progression and LitRPG grammar | measurable growth and visible state change | make power, rank, money, affection, territory, or access advance on schedule |

## Deployment Principle

Every episode should have one clear job.

```text
pressure -> protagonist method -> visible proof -> witness reaction -> reward -> new cost/question
```

An episode can contain several events, but only one primary reader-reward job. If two jobs compete, split them across episodes.

## Episode Job Types

| Job | Purpose | Typical cliche cards | Best placement |
| --- | --- | --- | --- |
| promise proof | prove the title/concept | identity, advantage, first proof | episode 1 |
| method repeat | show repeatable engine | advantage, renewal, changed proof | episode 2 |
| social amplification | make the reward public | witness, institution, reaction | episode 3 |
| cost arrival | show success has pressure | cost, antagonist, rule change | episode 4 |
| mini-arc payoff | close first question and open bigger one | reward, paid hook, institution turn | episode 5 |
| scale transfer | move same reward to bigger arena | escalation, rival institution | episodes 6-10 |
| antagonist competence | opposition learns or counters | antagonist mirror, cost causality | episodes 8-15 |
| reward diversification | add second reward channel | money, safety, access, relationship | episodes 11-25 |
| myth expansion | reveal larger world without drowning proof | hidden system, secret faction | episodes 20-50 |
| reset-with-memory | refresh the engine without erasing progress | new institution, new metric, new witness | after major arc |

## Deployment Horizons

### 1-Episode Deployment

Use for openings or proof scenes.

Required:

- title promise;
- starting pressure;
- protagonist action;
- proof object;
- witness reaction;
- small payoff;
- concrete next question.

### 1-5 Deployment

Use for launch packages and free-sample windows.

| Episode | Primary job | Must pay | Must open |
| --- | --- | --- | --- |
| 1 | promise proof | first visible reward | cost or question caused by proof |
| 2 | method repeat | proof under changed condition | institution notices |
| 3 | social amplification | public/status reaction | stronger authority response |
| 4 | cost arrival | pressure caused by success | mini-arc confrontation |
| 5 | mini-arc payoff | one full promise paid | paid-boundary larger question |

### 6-25 Deployment

Use for first paid arc.

| Segment | Job | Cliche deployment |
| --- | --- | --- |
| 6-8 | convert first proof into status | witness, institution, access card |
| 9-12 | let antagonist counter logically | antagonist competence, cost causality |
| 13-16 | diversify reward | money, safety, relationship, knowledge, territory |
| 17-20 | reveal hidden rule or larger institution | long-term hook, system/faction card |
| 21-25 | pay arc reward and open scale transfer | mini-boss, board/sect/guild ruling, new arena |

### 26-50 Deployment

Use for second-stage durability.

| Segment | Job | Cliche deployment |
| --- | --- | --- |
| 26-32 | same method in bigger arena | scale echo, institution transplant |
| 33-38 | relationship/status consequence | public witness, alliance, betrayal, reputation |
| 39-44 | expose cost of the advantage | taboo, debt, timeline drift, rule patch |
| 45-50 | settle second arc and reveal long engine | hidden world/system, national/faction layer |

## Deployment Schema

Use this schema for stable artifacts.

```yaml
serial_arc_deployment:
  brief:
  source_families:
  selected_engine:
  deployment_horizon:
  core_reader_promise:
  episode_jobs:
    - episode:
      job:
      cliche_cards:
      pressure:
      protagonist_method:
      proof_object:
      witness:
      reward_paid:
      reward_debt_opened:
      hook_type:
      fatigue_guard:
  arc_segments:
    - range:
      arc_job:
      reward_channel:
      institution_shift:
      antagonist_move:
      payoff:
      next_scale:
  hook_cadence:
    payoff_before_hook:
    hook_rotation:
    banned_hook:
  feedback_checkpoints:
    - episode:
      check:
      repair_if_weak:
  continuity_anchors:
    non_negotiable_promise:
    approved_cards:
    restricted_cards:
    unresolved_debts:
  validation:
    verdict:
    first_repair:
    next_artifact:
```

## Hook Cadence

Rotate hook types so the serial does not feel like one repeated cliffhanger.

| Hook type | Opens | Use when | Risk |
| --- | --- | --- | --- |
| consequence hook | what the win caused | after visible payoff | feels punitive if not causal |
| discovery hook | what proof revealed | after investigation/proof scene | can become lore dump |
| authority hook | who now reacts | after public proof | weak if authority is incompetent |
| contract hook | what obligation appears | after status/money gain | unfair if terms were hidden too long |
| rival hook | who can counter | after social recognition | stale if rival is only jealous |
| scale hook | where same reward grows next | arc ending | confusing if scale changes reward type |
| emotional hook | relationship/status shift | romance/status engines | weak if not tied to action |
| metric hook | rank, money, points, territory, favorability changes | progression engines | shallow if numbers have no consequence |

Rule:

```text
pay one reward -> open one cost/question -> name the next arena
```

## Feedback Checkpoints

Place checkpoints before predictable fatigue.

| Checkpoint | What to ask | Repair if weak |
| --- | --- | --- |
| after episode 1 | Did readers understand the promise? | sharpen proof object and witness |
| after episode 3 | Is the reaction satisfying or repetitive? | change witness authority |
| after episode 5 | Did the paid boundary feel fair? | pay one more promise before hook |
| after episode 10 | Is the method still interesting? | change pressure or proof type |
| after episode 15 | Is the antagonist competent? | give opponent partial truth and leverage |
| after episode 25 | Did the arc pay enough? | close a debt before scale transfer |
| after episode 50 | Can the same reward scale again? | move to bigger institution, not new unrelated genre |

## Deployment Failure Modes

| Failure | Sign | Repair |
| --- | --- | --- |
| card pileup | too many cliches in one episode | assign one primary job per episode |
| debt bloat | many questions open, few paid | use reward debt ledger and close one debt |
| hook monotony | every episode ends on danger | rotate consequence, authority, metric, emotional, contract hooks |
| causal drift | new events do not follow from previous wins/costs | relabel edges: because, therefore, but |
| scale whiplash | world suddenly expands | make scale grow through institution reaction |
| comment-chasing | every reader complaint changes core promise | repair delivery, not the genre promise |
| proof collapse | later arcs rely on exposition | schedule proof objects every arc segment |

## Output Contract

For phase-7 outputs, include:

- brief and selected engine;
- source families used;
- deployment horizon;
- core reader promise;
- episode job table;
- cliche deployment schedule;
- reward debt ledger summary;
- hook cadence;
- feedback checkpoints;
- continuity anchors;
- validation verdict and first repair;
- next production artifact.
