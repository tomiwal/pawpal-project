# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF7)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I used Claude to help design and implement the entire PawPal+ scheduling system. The main task was: "Build a pet care planning assistant with UML design, Python classes for scheduling logic, and a Streamlit UI."

**What did the agent do?**

1. Helped design the UML diagram by explaining class structure (Owner, Pet, Task, Schedule, Scheduler)
2. Guided me through implementing class stubs from the UML
3. Explained lambda functions and sorting algorithms for priority-based task sorting
4. Connected the backend logic to the Streamlit UI by showing template code
5. Fixed syntax errors (indentation, missing colons, wrong priority capitalization)
6. Implemented missing methods (add_preference, get_total_duration, is_due_today)
7. Created test cases and filled in documentation

**What did you have to verify or fix manually?**

- I had to understand lambda functions conceptually before using them (asked for simpler explanation)
- Fixed priority value checks to handle lowercase inputs from Streamlit
- Verified the scheduling logic worked correctly by testing with sample data
- Adjusted time constraints and priority mapping to match the app's behavior

---

## Prompt Comparison (SF11)

> Compare two different prompts (or two different models) on the same task.

| | Option A | Option B |
|-|----------|----------|
| **Model / tool used** | | |
| **Prompt** | | |
| **Response summary** | | |
| **What was useful** | | |
| **Problems noticed** | | |
| **Decision** | | |

**Which approach did you use in your final implementation and why?**

<!-- Your conclusion -->
