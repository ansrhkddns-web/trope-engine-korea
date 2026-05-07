# Reward Debt Ledger 7

Use this file with `serial-arc-deployment-planner-7.md` when a serial plan opens promises, mysteries, revenge goals, romance tension, rank ladders, money goals, or long-term cliche hooks that must be paid later.

Reward debt is not bad. It is how serial fiction creates continuation. It becomes dangerous when the story keeps borrowing patience without visible repayment.

## Reward Debt Types

| Debt type | Reader waits for | Safe repayment | Danger sign |
| --- | --- | --- | --- |
| proof debt | proof that the protagonist is special | public result, object, number, witness | only internal monologue confirms it |
| revenge debt | punishment or reversal against an offender | visible loss, apology, exposure, status reversal | humiliation continues too long |
| power debt | stronger ability or rank | new skill use, rank change, new access | training without payoff |
| money/status debt | wealth, title, shares, land, sect status | contract, account, board vote, public recognition | abstract "influence" only |
| knowledge debt | answer to mystery or future info | one concrete rule revealed | mystery replaces reward |
| relationship debt | trust, affection, alliance, reconciliation | changed behavior or public choice | endless misunderstanding |
| safety debt | reduced danger for self or group | rescue, survival rate, secured territory | danger escalates without relief |
| justice debt | public correction of unfairness | hearing, verdict, reputation shift | system remains unmoved |

## Debt Rules

- Open no more than three major debts in the first five episodes.
- Pay one visible debt before opening a larger same-type debt.
- Do not let all debts belong to the same reward channel.
- Track who knows the debt exists: protagonist, reader, witness, institution, antagonist.
- A paid boundary should close at least one small debt and open one larger concrete debt.
- Long mysteries must pay small functional answers before the big reveal.

## Ledger Schema

```yaml
reward_debt_ledger:
  open_debts:
    - id:
      type:
      opened_episode:
      promise:
      who_knows:
      proof_needed:
      planned_payoff_episode:
      payoff_form:
      risk_if_delayed:
      status:
  paid_debts:
    - id:
      paid_episode:
      visible_payoff:
      witness:
      new_debt_opened:
  debt_balance:
    current_open_count:
    overdue:
    same_channel_overload:
    next_debt_to_pay:
```

## Debt Cadence

Use this default cadence unless the genre needs faster payoff.

| Range | Open | Pay |
| --- | --- | --- |
| episode 1 | title promise, first cost | first proof |
| episodes 2-3 | institution question, rival question | method repeat, social proof |
| episodes 4-5 | paid-boundary larger pressure | first mini-arc promise |
| episodes 6-10 | antagonist logic, larger arena | status/access debt |
| episodes 11-25 | hidden rule, relationship/status consequence | first paid arc reward |
| episodes 26-50 | origin or scale mystery | second arc reward and next arena |

## Genre Debt Defaults

| Genre | Open early | Pay early | Delay safely |
| --- | --- | --- | --- |
| hunter/gate | survival proof, guild reaction | casualty reduction, scout/contract | gate origin |
| tower/system | rule exploit, rank change | floor clear, system notice | system source |
| regression/finance | future knowledge use, money/status repair | acquisition, vote, stock/land proof | second regressor/cartel |
| murim | sect status, technique proof | duel win, elder recognition | scripture origin/war |
| academy | ranking, professor/rival reaction | exam result, club/team recognition | hidden curriculum |
| possession/villain/extra | death flag avoidance, social reputation | public reversal, saved victim | world script authority |
| support/profession | competence proof, team dependency | measurable survival/craft result | industry monopoly |
| romance/rofan | status choice, emotional trust | public choice, changed treatment | succession/divine contract |

## Overdue Debt Signals

| Signal | Meaning | Repair |
| --- | --- | --- |
| readers ask "그래서 언제 갚음?" | promise is overdue | move payoff earlier or reduce new hooks |
| every episode opens a new enemy | debt bloat | close one enemy/status debt |
| mystery expands but rules stay vague | knowledge debt abuse | reveal one usable rule |
| revenge target disappears too long | revenge debt drift | give interim reversal or trace |
| romance only misunderstands | relationship debt fatigue | pay one honest action |
| rank/money numbers rise privately | proof debt unpaid | add public metric or witness |

## Debt Repair Operators

| Operator | Use when | Effect |
| --- | --- | --- |
| early partial payoff | debt is too large for current arc | pay a small visible piece now |
| witnessed repayment | payoff feels private | make a meaningful witness react |
| debt merge | too many similar debts exist | combine two debts into one institutional pressure |
| debt conversion | reward channel is overloaded | convert status debt into money, safety, access, or relationship debt |
| debt deadline | payoff keeps drifting | assign an episode and consequence |
| debt echo | long-term hook needs continuity | repeat the same debt at a larger scale |

## Debt Ledger Output

Use this compact form in phase-7 deployment.

```yaml
reward_debt_summary:
  open_count:
  next_debt_to_pay:
  safe_to_open_new_debt:
  overdue_debts:
  paid_boundary_payoff:
  new_paid_boundary_hook:
  repair:
```
