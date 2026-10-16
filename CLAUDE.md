# CLAUDE.md: BJF AI Coach

## Goal
A tutor for rural Punjabi students preparing for JEE/NEET that (1) never shows an unverified
explanation, (2) teaches Socratically instead of handing over answers, and (3) works offline
and in Punjabi (Gurmukhi) and English. Build Day scope: Class 11 Physics, Kinematics only.

## Non-negotiable rules
- Never show a student an explanation whose `verification.status` is not `verified`.
  Unverified or failed items go to the teacher review queue.
- The doubt tutor answers from verified solutions in the question bank. It gives a hint
  first and reveals the full solution only after the student attempts a step.
- Every student-facing string has `en` and `pa` (Gurmukhi) versions.
- No secrets in git. Use `.env` (see `.env.example`).
- Out of scope today: wellbeing companion, career/ability assessment, extra modules.

## Ownership (agents: edit only your area unless asked)
- `content/`, `data/`, mastery logic, evaluation: Taranjot
- `app/` (student PWA + teacher dashboard), `backend/` API routes: teammate
- `docs/spec.md` and this file: shared. Change the spec here first, then the code.

## Proposed stack (edit if the team decides otherwise)
- Backend: Python + FastAPI, SQLite, sympy for verification
- Frontend: React + Vite as an installable PWA; service worker caches question bank,
  verified solutions and mock tests for offline use; offline doubts are queued and synced
- LLM: Claude via the Anthropic API (model config owned by one person)

## Conventions
- Small PRs, one branch per feature, merge to `main` every couple of hours
- Write tests for anything touching scoring, mastery or verification
- Schemas in `docs/spec.md` are the source of truth

## Commands
- Verify the question bank: `python content/verify/verify.py data/seed/questions.sample.json`
