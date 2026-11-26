# Engineering Contract — Juice Shop Execution

## Mission

Maintain a reusable black-box functional test automation for OWASP Juice Shop.

The system executes the 78 catalogued scenarios through the real application UI, preserves observable evidence, and keeps automation failures distinct from application behaviour.

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
10. Keep reporting code dependent on execution evidence, not on expected outcomes from the catalog.

## Architecture

scenario catalog
 -> precondition
 -> semantic locator
 -> resilient executor
 -> real UI interaction
 -> before/after observer
 -> evidence JSON + screenshots
 -> Markdown/DOCX reporting
 -> optional LLM humanization

## Scenario suite

Current catalog:

- ADM: 3
- CAR: 7
- CAT: 17
- CHK: 28
- IDT: 17
- PER: 6
- Total: 78

The source of truth for the scenario inventory is `scenarios/scenarios.json`.

## Failure-handling strategy

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
2. Group failures by shared mechanism, not scenario ID.
3. Fix the shared mechanism.
4. Re-run unit tests.
5. Re-run the full UI scenario suite.
6. Reject changes that introduce regressions without a stronger general benefit.

## Reporting integrity

The executor is the source of truth for execution status and observed state.

The LLM is optional and is used only to organize and humanize documentation. It must not promote an expected result into an observed result or invent UI details.

The reporting pipeline is:

```text
execution
   ↓
evidence JSON + screenshots
   ↓
optional humanization
   ↓
fixed DOCX template
```

## Validation after changes

Run:

```powershell
python -m pytest -q
python run.py --start-app --all
```

If the complete suite passes, regenerate the final documentation:

```powershell
python -m reporting.humanizer --all --force
python -m reporting.docx_generator --humanize auto --force-humanize
```

Before committing:

```powershell
git status
git diff --check
```

The main branch is the canonical branch for the project.
