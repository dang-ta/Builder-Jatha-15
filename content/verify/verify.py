"""Verify each question's computed answer against its answer key.

Usage: python content/verify/verify.py data/seed/questions.sample.json [--write]
Sets verification.status to 'verified' or 'failed'. Only verified items may be shown to students.
"""
import json, math, sys

def run_check(code: str):
    env = {"math": math, "__builtins__": {}}
    try:
        import sympy
        env["sympy"] = sympy
    except ImportError:
        pass
    exec(code, env)  # checks are authored in-repo and reviewed; never run untrusted code here
    return float(env["answer"])

def main(path, write=False):
    questions = json.load(open(path, encoding="utf-8"))
    passed = 0
    for q in questions:
        key, tol = q["answer"]["value"], q["answer"].get("tolerance", 0.01)
        try:
            got = run_check(q["verification"]["check"])
            ok = math.isclose(got, key, rel_tol=tol, abs_tol=tol)
        except Exception as e:
            got, ok = f"error: {e}", False
        q["verification"]["status"] = "verified" if ok else "failed"
        passed += ok
        print(f"{q['id']}: key={key} computed={got} -> {'PASS' if ok else 'FAIL'}")
    print(f"\n{passed}/{len(questions)} verified")
    if write:
        json.dump(questions, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main(sys.argv[1], "--write" in sys.argv)
