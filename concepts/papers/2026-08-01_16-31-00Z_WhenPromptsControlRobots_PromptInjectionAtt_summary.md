# Summary: 2026-08-01_16-31-00Z_WhenPromptsControlRobots_PromptInjectionAttacksinM.md
Saved: 2026-08-03 20:30
Source: 2026-08-01_16-31-00Z_WhenPromptsControlRobots_PromptInjectionAttacksinM.md
Model: None

---

## Summary  
This paper investigates how malicious prompts can hijack autonomous robotic agents that rely on large language models (LLMs) for task planning and control, focusing specifically on multi‑agent configurations. The authors demonstrate that both direct injections into instruction strings and indirect injections through perception modules can cause unsafe actions and degrade performance. Their study is the first systematic analysis of prompt injection attacks in a LLM‑driven multi‑agent robotic system, revealing how attack vectors propagate across agents via shared prompt structures. By varying attack complexity and architectural query design, they quantify the impact on task completion and safety.

## Key Contributions  
- [Finding 1] A comprehensive investigation of prompt injection attacks against an LLM‑based multi‑agent robotic platform is presented for the first time.  
- [Finding 2] The paper shows that injected prompts can induce adversarial actions while reducing overall task completion rates.  
- [Finding 3] Attack propagation through shared prompt components and sensitivity to architectural changes are identified as key factors influencing success.

## Methodology  
The authors constructed a multi‑agent system where each agent uses an LLM to generate task instructions, perform perception tasks, and coordinate actions. Experiments were conducted across two settings—single‑agent and multi‑agent—and varied the complexity of attack goals, injection strategies (direct vs. indirect), and prompt compositions. They measured outcomes such as safety violations, task success rates, and cross‑agent contamination. Architectural modifications to LLM queries were also tested to assess their protective effect.

## Results  
Attack success was observed when malicious prompts altered the instruction hierarchy or hijacked perception outputs, leading to unsafe robot actions and a measurable drop in task completion. In multi‑agent scenarios, contaminated prompts could be shared among agents, causing cross‑contamination where one compromised agent influences others. Architectural changes that isolate LLM queries reduced vulnerability, indicating that query design is a critical defense point.

## Significance  
Prompt injection poses a tangible safety risk to robots that depend on LLMs for decision making, especially in collaborative setups where failures can cascade. This work provides the first systematic evidence of such attacks and highlights the need for robust prompting practices and architectural safeguards before deploying LLM‑controlled robotic agents in real‑world environments.

## Related Concepts  
prompt injection, multi‑agent systems, large language models, robotics, adversarial attacks, task planning, perception modules, cross‑contamination, query isolation.
