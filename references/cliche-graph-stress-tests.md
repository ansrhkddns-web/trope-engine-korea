# Cliche Graph Stress Tests

Use this file after selecting cliche cards from genre banks, reference synthesis, or remix operators. It tests whether the cards form a durable serial engine.

## Graph Model

A cliche graph has:

- **nodes**: cliche cards, motif objects, institutions, witnesses, antagonists, rewards, costs.
- **edges**: causal links that explain why one node creates the next.
- **loops**: repeatable sequences that can generate episodes.
- **ladders**: escalating arenas from personal to institutional to world-scale.

Minimum usable graph:

`promise -> pressure -> protagonist action -> proof object -> witness reaction -> reward -> cost -> next pressure`

## Required Node Types

| Node type | Required? | Purpose |
| --- | --- | --- |
| Promise node | yes | tells readers what pleasure they are buying |
| Protagonist advantage node | yes | creates action |
| Pressure node | yes | forces a scene now |
| Proof object node | yes | makes reward visible |
| Witness node | yes | amplifies payoff |
| Institution node | yes | gives social/genre consequence |
| Cost node | yes | prevents free reward |
| Antagonist node | yes for long concepts | contests the method |
| Hook object node | yes | creates next-click pressure |
| Long-term ladder node | yes for series | proves 50+ episode durability |

## Edge Types

Use these edge labels when explaining or linting a graph:

- `causes`: A directly creates B.
- `reveals`: A changes the meaning of B.
- `measures`: institution or witness evaluates proof.
- `prices`: market, rank, reputation, or law changes value.
- `claims`: owner, sponsor, family, sect, or contract asserts right.
- `punishes`: rule owner retaliates.
- `recruits`: proof creates offer or alliance.
- `mirrors`: antagonist uses a rival version of the advantage.
- `escalates`: local win opens larger arena.
- `debts`: reward creates obligation.

## Stress Tests

### T01 Node Necessity

Remove each cliche card. If the proof scene, reward loop, or next pressure still works unchanged, the card is decorative.

Repair:

- merge it with another card;
- change it into cost or witness;
- cut it.

### T02 Edge Causality

Every next event must be caused by proof, witness, reward, or cost.

Fail sign:

- "then suddenly" escalation.

Repair:

- add a report, claim notice, ranking review, audit, contract clause, rumor, bid, or debt.

### T03 Proof Visibility

The reward must be visible through an object, number, access change, witness statement, public reaction, or institutional decision.

Fail sign:

- protagonist only knows they won.

Repair:

- add rank board, contract, footage, token, price, deed, apology, title, license, or public invitation.

### T04 Agency

The protagonist must make a choice that uses the advantage.

Fail sign:

- advantage passively triggers.

Repair:

- make the protagonist select, refuse, bargain, expose, rescue, optimize, or exploit a rule.

### T05 Cost Integrity

The cost must come from the reward itself.

Fail sign:

- random punishment after success.

Repair:

- make the reward damage someone's revenue, authority, reputation, ownership, secrecy, or timeline.

### T06 Witness Authority

The witness must matter emotionally or institutionally.

Fail sign:

- crowd noise with no consequence.

Repair:

- use rival, guild scout, elder, professor, board member, family head, reporter, victim, market buyer, or system admin.

### T07 Antagonist Competence

The antagonist should be correct by an old metric and wrong by the protagonist's new metric.

Fail sign:

- antagonist is only foolish or cruel.

Repair:

- give them a rational incentive, old-system expertise, or a mirrored advantage.

### T08 Payoff Density

Every episode seed should pay at least one concrete reward before adding a larger hook.

Fail sign:

- all mystery, no payment.

Repair:

- add small rank, money, access, relationship, revenge, or knowledge payoff.

### T09 Loop Variation

The repeat loop must vary proof object, witness, cost, or arena.

Fail sign:

- same rank test with higher numbers.

Repair:

- rotate test venue: exam, raid, audit, duel, auction, hearing, board vote, social ceremony.

### T10 Scale Ladder

Escalation must preserve the original reward in a larger arena.

Fail sign:

- genre promise changes after arc 1.

Repair:

- map personal -> team -> institution -> market/faction -> region/nation/world using the same reward channel.

### T11 Originality Firewall

The graph must not depend on named settings, unique rules, signature scenes, or character-role layouts from a source.

Repair:

- change institution, proof object, action, witness, scene order, and cost.

### T12 Paid-Trust Hook

The hook must ask a concrete question after paying a reward.

Fail sign:

- pure cliffhanger before payoff.

Repair:

- use reward-then-cost: win title, then owner appears; win board vote, then audit begins; save victim, then debt is claimed.

## Graph Verdict

| Result | Meaning |
| --- | --- |
| `pass` | all required node types exist, edges are causal, proof and cost are visible |
| `revise` | the graph works but one or two edges/nodes are weak |
| `rebuild` | missing proof, witness, cost, agency, or originality firewall |

## Output Template

When stress-testing a cliche graph, include:

- **Graph verdict**:
- **Strongest node**:
- **Weakest edge**:
- **Decorative cards to cut or merge**:
- **Missing required node types**:
- **First repair**:
- **Repaired graph path**:
- **Episode loop after repair**:
