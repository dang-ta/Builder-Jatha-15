# Spec: schemas and API (v0.1)

## Question
```json
{
  "id": "kin-001",
  "chapter": "kinematics",
  "concepts": ["uniform-acceleration", "equations-of-motion"],
  "difficulty": 1,
  "source": "illustrative | NCERT ex X.Y | JEE Main 2023 S1 Q12",
  "text": { "en": "...", "pa": "..." },
  "answer": { "value": 25, "unit": "m", "tolerance": 0.01 },
  "common_mistakes": ["uses s = ut instead of s = ut + 1/2 at^2"],
  "solution_steps": [{ "en": "...", "pa": "..." }],
  "verification": {
    "check": "answer = 0.5 * 2 * 5**2",
    "status": "unverified | verified | failed",
    "reviewed_by": null
  }
}
```

## Attempt event
```json
{ "student_id": "s-01", "question_id": "kin-001", "response": 25,
  "correct": true, "seconds": 74, "hints_used": 1, "ts": "ISO-8601", "offline": false }
```

## Mastery record (per student, per concept)
```json
{ "student_id": "s-01", "concept": "uniform-acceleration",
  "score": 0.62, "attempts": 9, "last_mistake": "sign of acceleration" }
```

## API
| Method | Path | Purpose |
|---|---|---|
| GET  | /questions/next?student_id= | next practice items from mastery + teacher overrides |
| POST | /attempts | submit attempt(s); accepts a batch for offline sync |
| POST | /doubts | Socratic tutor turn: {student_id, question_id?, message, lang} |
| GET  | /students/{id}/mastery | mastery map |
| GET  | /teacher/overview | class status, at-risk flags |
| POST | /teacher/override | set what a student works on next |
| GET  | /teacher/review-queue | unverified/failed explanations |
