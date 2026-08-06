# Summary: 2026-08-02_16-10-02Z_Prompt_InducedWasteinCodingAgents_ReasoningStructu.md
Saved: 2026-08-05 20:17
Source: 2026-08-02_16-10-02Z_Prompt_InducedWasteinCodingAgents_ReasoningStructu.md
Model: None

---

## Summary  
This paper investigates how the wording of prompts to coding agents influences both the amount of work performed and the overall cost, revealing that many common prompt habits generate unnecessary effort without improving task success. The authors preregistered a cross‑model experiment across two real coding‑agent harnesses on hidden software tasks to isolate the impact of prompt design from model capabilities. Their core insight is that effective prompts must tightly bound the scope of work and include explicit stopping rules, whereas vague or overly ambitious prompts lead to extensive exploration and tool misuse. By quantifying “prompt‑induced waste,” they show that prompt engineering is an operational lever for efficient coding agents.

## Key Contributions  
- Prompt habits such as requesting multiple approaches cause agents to develop and discard several solution paths before implementing one, creating substantial extra reasoning work without success gains.  
- Different kinds of waste propagate through distinct channels: some remain in the reasoning layer, while others expand into tool use, latency, repeated testing, and context growth.  
- Prompts that define a clear scope, request the smallest sufficient change, and specify a stopping rule preserve diagnosis and validation while avoiding unnecessary exploration.

## Methodology  
The authors conducted a preregistered study using multiple reasoning models (e.g., GPT‑4, Claude) and two real coding‑agent harnesses. Tasks were selected with hidden evaluation metrics to prevent bias from visible success rates. Prompt variations were systematically varied across the same task set, and total cost—measured in token usage, turn count, tool calls, and latency—was recorded for each combination.

## Results  
The primary finding is that prompts encouraging “deep thinking” or “maximum certainty” increase visible reasoning length but also trigger repeated checks, extra tests, and longer execution times. Conversely, prompts that limit the task to a minimal change and stop once the solution is found reduce total cost by up to 45 % compared with unconstrained prompts. Waste analysis shows that ~60 % of inefficiency stays within reasoning, while another ~30 % manifests as tool‑use overhead and repeated context updates.

## Significance  
Prompt design directly controls the operational efficiency of coding agents; without careful prompting, agents may perform far more work than necessary, inflating latency and resource consumption. The study provides empirical evidence that bounded, well‑structured prompts are essential for building cost‑effective AI assistants in software development workflows.

## Related Concepts  
- Prompt engineering  
- Reasoning structure  
- Tool behavior  
- Latency and execution cost  
- Context growth  
- Preregistered studies  
- Bounded exploration
