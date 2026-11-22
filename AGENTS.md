# AMBOLS Recovery V2 — Engineering Contract

## Mission

Build a reusable black-box requirements-recovery automation for OWASP Juice Shop.

The system must recover observable application behaviour from scenario descriptions through real UI execution, preserve evidence, and distinguish application failures from automation failures.

## Non-negotiable engineering rules

1. Never add a scenario-ID-specific selector, branch, wait, or workaround.
2. Prefer abstraction-level fixes in this order:
   - semantic locator
   - interaction executor
   - state synchronization
   - precondition/fixture contract
   - observer/evidence
   - scenario data
3. Do not change a passing scenario merely to make one failing scenario pass.
4. Every behavioural change must be validated against the full scenario suite.
5. Keep automation errors distinct from functional assertion failures.
6. Prefer observed browser behaviour over assumptions about browser implementation details.
7. Do not replace real UI behaviour with API calls when the scenario is testing UI behaviour. APIs may prepare data preconditions only.
8. Do not use fixed sleeps as the primary synchronization mechanism. Prefer state/condition polling.
9. Preserve before/after evidence for every action.
10. Treat the 69/75 baseline commit `f1c16b7` as the regression reference.

## Architecture

scenario
 -> precondition
 -> semantic locator
 -> resilient executor
 -> real UI interaction
 -> before/after observer
 -> behaviour event
 -> evidence
 -> recovered requirement

## Recovery strategy

When a scenario fails:

1. Classify the failure:
   - locator failure
   - stale/detached DOM
   - blocked interaction/overlay
   - framework synchronization
   - fixture/state failure
   - navigation/popup/download semantics
   - assertion mismatch
   - real application failure
2. Group failures by mechanism, not scenario ID.
3. Fix the shared mechanism.
4. Re-run unit tests.
5. Re-run all UI scenarios.
6. Reject changes that introduce regressions without a stronger general benefit.

## Agent workflow

Before editing:
- inspect the repository and relevant files;
- inspect the failure evidence;
- compare against `f1c16b7`;
- identify the smallest reusable abstraction that explains the failure.

During editing:
- make one coherent change;
- keep code version-tolerant across Juice Shop UI implementations;
- add comments explaining the engineering invariant, not the scenario.

After editing:
- run `pytest -q`;
- run `python run.py --all`;
- inspect status distribution and failure clusters;
- report exact regressions and remaining mechanisms.

## Research integrity

The tool is itself part of the research artifact. Avoid hidden heuristics that encode expected answers. Evidence must come from observable UI state, navigation, controls, text, and interaction outcomes.

External coding agents may propose changes, but the repository's tests and the engineering contract are the final authority.
