# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

I designed PawPal+ with five core classes: Owner (stores user info and preferences), Pet (stores pet information), Task (represents a care task with priority and duration), Schedule (holds a list of tasks for a day), and Scheduler (the engine that generates plans). The Scheduler is responsible for sorting tasks by priority and fitting them into available time.

**b. Design changes**

The design stayed mostly consistent from UML to implementation. I did add a `return 0` fallback to `get_priority_value()` to handle unexpected priority values gracefully.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

The scheduler considers two main constraints:
1. **Time available** - Owner's available minutes per day (default 480 minutes)
2. **Task priority** - High/medium/low priority determines task ordering

Tasks are sorted by priority (high → medium → low), and only tasks that fit within available time are scheduled.

**b. Tradeoffs**

The main tradeoff: **Greedy scheduling vs. optimal packing**. The scheduler uses a simple greedy approach (sort by priority, add tasks in order until time runs out). This prioritizes important tasks but may leave gaps in the schedule. A more complex algorithm could pack tasks more efficiently, but would be slower and harder to explain to users.

---

## 3. AI Collaboration

**a. How you used AI**

I used AI to:
- Understand UML diagram structure and Mermaid syntax
- Learn Python class design patterns
- Debug sorting logic using lambda functions
- Connect Streamlit UI to backend logic

Most helpful prompts were specific examples with expected input/output.

**b. Judgment and verification**

I initially received lambda syntax for sorting, which I found confusing. I asked for a simpler explanation and ended up understanding it better, then used the lambda version because it was more Pythonic. I verified it worked by testing with sample data.

---

## 4. Testing and Verification

**a. What you tested**

I tested:
- Priority value mapping (high=3, medium=2, low=1)
- Task sorting order (tasks sorted from highest to lowest priority)
- Time-fitting logic (tasks only added if they fit in available time)
- End-to-end flow through the Streamlit UI

**b. Confidence**

I'm fairly confident the scheduler works for the basic use case. Edge cases I'd test next:
- What if no tasks fit in available time?
- What if priorities are invalid?
- What if duration_minutes is 0 or negative?

---

## 5. Reflection

**a. What went well**

I'm most satisfied with the clean separation of concerns - the models.py logic is completely independent of the Streamlit UI, making it testable and reusable.

**b. What you would improve**

- Add validation for invalid inputs (negative durations, unknown priorities)
- Implement more sophisticated scheduling (consider task dependencies, recurring tasks)
- Add a visual timeline display in Streamlit (showing what time each task runs)
- Write unit tests for all class methods

**c. Key takeaway**

The most important lesson: designing the system structure (UML) before coding saved a lot of time and made implementation straightforward. Clear class responsibilities made the code easy to understand and modify.
