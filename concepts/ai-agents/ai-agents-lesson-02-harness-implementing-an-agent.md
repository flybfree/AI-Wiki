---
title: "AI Agents Lesson 2 - The Harness - Implementing an Agent"
date: 2026-07-16
status: draft
tags: [lesson, agents, harness, implementation]
---

# Lesson 2: The Harness

**Source**: [OpenAI: A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/) · [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) · [LangGraph: Agent orchestration framework](https://www.langchain.com/langgraph)

## Lesson goal
See how a harness turns a model into a working agent by managing the loop, tools, permissions, state, and stop conditions.

## What the harness is
The harness is the control layer around the model.
It is the part of the system that:
- builds the prompt
- loads the current state
- decides which tools are available
- checks whether an action is allowed
- executes the action
- records the result
- decides whether the agent should continue or stop

The model proposes what to do next.
The harness decides whether that proposal becomes an actual action.

That distinction matters because an agent is not a model call.
An agent is the full loop that surrounds the model call.

## Why the harness matters
Without a harness, you have a model that can suggest actions but not reliably carry them out.
With a harness, you can give the model a controlled way to act in the world.

The harness is what makes the system:
- repeatable
- inspectable
- safer
- easier to debug
- easier to stop when it goes wrong

If Lesson 1 answers “what is an agent?”, this lesson answers “what code actually makes it one?”

## The minimal loop
A simple agent harness usually does four things repeatedly:
1. send the current state to the model
2. parse the model’s next action
3. run the action if it is allowed
4. add the observation back into state

That is enough to create a basic agent.
Everything else is refinement.

## End-to-end example
Here is a full walk-through of one harnessed run for a support assistant.

### Scenario
A customer asks: “Can I get a refund for last month’s charge?”

The harness needs to:
- inspect the ticket
- look up the refund policy
- check the account status
- draft a reply
- stop for approval before sending

### Step-by-step run
#### 1. Load state
The harness starts with:
- the customer message
- the customer ID
- the current ticket ID
- an empty action history
- a `needs_approval` flag set to `False`

#### 2. Ask the model for the next action
The prompt includes the goal, current state, and allowed tools.
The model returns something like:
```json
{"type":"tool","name":"search_policy","args":{"query":"refund eligibility last month charge"}}
```

#### 3. Policy check
The harness checks whether `search_policy` is allowed.
It is read-only, so the action is approved.

#### 4. Run the tool
The tool returns:
- policy title
- excerpt
- effective date
- link to the source

#### 5. Add the observation to state
The harness appends the result to history and rebuilds the prompt.
Now the model can see the actual policy text instead of guessing.

#### 6. Ask for the next action
The model now returns:
```json
{"type":"tool","name":"check_account_status","args":{"customer_id":"12345"}}
```

#### 7. Run the second tool
The harness checks permissions, runs the lookup, and gets back:
- customer is within the refund window
- payment method is valid
- no prior refund has been issued

#### 8. Draft the response
The model returns a draft reply:
```json
{"type":"final","content":"The account appears eligible for a refund. Please confirm and I can submit it."}
```

#### 9. Approval gate
Because the next real action would be an external customer message, the harness pauses.
A human reviews the draft and either approves or edits it.

#### 10. Finish
Once approved, the harness sends the message and records the trace.
The trace now shows exactly what the agent saw, did, and decided.

### Why this example matters
This is the difference between “a model that can talk about support” and “an agent that can actually work a support case.”
The harness turns the model’s suggestions into a controlled operational flow.

## Minimal Python sketch
```python
class Harness:
    def __init__(self, model, tools, policy):
        self.model = model
        self.tools = tools
        self.policy = policy

    def run(self, goal):
        state = {
            "goal": goal,
            "history": [],
            "done": False,
        }

        while not state["done"]:
            prompt = self.build_prompt(state)
            draft = self.model(prompt)
            action = self.parse_action(draft)

            if action["type"] == "final":
                state["done"] = True
                return action["content"]

            if not self.policy.allows(action, state):
                state["history"].append({"blocked": action})
                continue

            tool = self.tools[action["name"]]
            observation = tool(**action["args"])
            state["history"].append({"action": action, "observation": observation})
            state = self.update_state(state, observation)
```

That code is not production ready, but it shows the shape.
The harness owns the loop.
The tools do the work.
The model makes the next-step suggestion.


## Sample trace
A trace for the support example might look like:

1. Goal: answer the refund question safely
2. Tool call: `search_policy`
3. Observation: refund policy found, effective this month
4. Tool call: `check_account_status`
5. Observation: customer eligible
6. Final draft: approval requested before sending
7. Human review: approved
8. Completion: message sent and logged

A trace is useful because it lets you debug the decision path instead of only the final answer.

## What each piece does
### Model
The model reads the prompt and proposes the next action or final answer.

### Tools
Tools are the real capabilities: search, retrieval, file edits, API calls, database reads, and so on.

### Policy
The policy says what is allowed, what needs approval, and what must never happen.

### State
State remembers the goal, the history, the latest results, and any checkpoints.

### Stop condition
The stop condition says when the agent is done, blocked, or stuck.

## Example: support triage agent
Imagine a support agent that handles a customer ticket.

### Step 1: load the ticket
The harness loads the ticket text and current customer state.

### Step 2: ask the model for a next step
The model might say:
- search the policy docs
- check account status
- draft a reply

### Step 3: run the tool
The harness executes the chosen tool and stores the result.

### Step 4: continue the loop
The model sees the new observation and decides what to do next.

### Step 5: require approval before sending
If the next action is to send a customer message, the harness can stop and ask for approval.

That is a real agent implementation: model, tools, state, policy, and a loop.

## What should live in the harness
Good harness code usually owns:
- prompt assembly
- step counting
- state persistence
- tool dispatch
- permission checks
- retries
- timeouts
- logging and traces
- approval gates
- final result formatting

## What should not live in the harness
The harness should not become the place where business logic hides.
It should not contain:
- tool implementation details
- domain rules that belong in policy documents
- huge prompt essays
- random one-off branching hacks

Keep the harness small and legible.
If the harness becomes a second application with its own business logic, debugging gets ugly fast.

## Common failure modes
- the model outputs an action the harness cannot parse
- the harness calls the wrong tool
- the harness forgets to save state
- the agent loops on the same failed action
- the harness allows a risky action without a checkpoint
- the loop has no clear stop condition

Most agent bugs are harness bugs, not model bugs.

## Concrete implementation rule
If you cannot answer these questions in code, the harness is too vague:
- What is the current goal?
- What tool can the agent use right now?
- What action is forbidden?
- What happens after the tool returns?
- How does the loop stop?

## Build this
Write a harness for a travel assistant that can:
- search flights
- compare hotel options
- draft an itinerary
- stop and ask for approval before booking

For each step, define:
- the input state
- the allowed tools
- the approval rule
- the stop condition

## Exercises
1. What makes the harness different from the model?
2. Why should the harness own the loop?
3. What belongs in policy instead of prompt text?
4. Why do stop conditions matter?

## Practical takeaway
A model can suggest an action.
A harness makes that action part of a controlled system.
If you want a real agent, start by designing the harness.

## Key takeaways
- The harness is the control layer around the model.
- The harness owns the loop, state, tools, and policy checks.
- The model proposes; the harness executes.
- Most agent failures are implementation and control failures.
- A clear harness is what makes an agent debuggable and safe.

## Review checklist
- Can you explain the harness in one sentence?
- Can you separate model, tools, policy, and state?
- Can you sketch a basic loop in pseudocode?
- Can you name three things the harness should log?

## Glossary
- **Harness**: the control layer that runs the agent loop and enforces rules
- **Policy**: the rules that decide what the agent may do
- **State**: the current record of the task and its progress
- **Stop condition**: the rule that ends the loop
- **Trace**: the recorded sequence of actions and observations

## Quick self-check
1. What is the harness?
2. What does the harness do that the model does not?
3. Why are stop conditions important?
4. Why do approval gates belong in the harness?

## Research slots to add later
- current agent framework runtime patterns
- structured control loops in LangGraph and similar systems
- approval and policy enforcement patterns from current agent stacks
