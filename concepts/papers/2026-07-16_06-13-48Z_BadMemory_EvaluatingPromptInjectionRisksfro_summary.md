# Summary: 2026-07-16_06-13-48Z_BadMemory_EvaluatingPromptInjectionRisksfromMemory.md
Saved: 2026-07-23 23:45
Source: 2026-07-16_06-13-48Z_BadMemory_EvaluatingPromptInjectionRisksfromMemory.md
Model: None

---

## Summary  
The paper investigates how persistent memory files in agentic systems can be exploited for prompt‑injection attacks, showing that malicious payloads embedded in these files can influence both the current session and future sessions. By evaluating two agentic platforms—Anthropic Claude Code and OpenAI Codex—across four models (Claude Haiku 4.5, Claude Opus 4.7, GPT‑5.2, GPT‑5.5), the authors demonstrate that attack success rates and payload persistence differ dramatically across systems, adversarial goals, and multi‑session sequences. Their work expands the threat model for prompt injection to include long‑term memory changes rather than only transient prompt manipulation.  

## Key Contributions  
- Persistent memory updates create a new attack surface for prompt injection in agentic systems.  
- Attack success varies substantially across systems, models, adversarial goals, and multi‑session sequences.  
- Payloads already planted in memory files can successfully influence current and future sessions.  

## Methodology  
The authors employed a sandboxed synthetic workspace to simulate realistic user interactions with the two agentic platforms. They injected untrusted payloads into existing memory files and measured whether those payloads altered the agents’ behavior during subsequent prompts, tracking both immediate effects and long‑term persistence across multiple sessions. The evaluation covered four distinct model variants to capture differences in capability and resilience.  

## Results  
Across all models, only a minority of payloads succeeded at overwriting memory files outright; however, many could still steer the agent’s outputs or preferences without direct file modification. Multi‑session attacks were more effective than single‑shot attempts, indicating that an adversary can gradually accumulate influence over time. The results show that while current defenses may block obvious injection attempts, they do not fully protect against covert manipulation of persistent memory.  

## Significance  
These findings highlight that the addition of persistent memory to agentic systems introduces a novel vulnerability: attackers can embed malicious instructions that survive beyond a single interaction and affect future behavior. This changes the security landscape for AI developers who rely on long‑term adaptation, urging the design of defenses that safeguard memory updates without sacrificing useful learning capabilities.  

## Related Concepts  
- Prompt injection  
- Memory files  
- Agentic systems  
- Adversarial payloads  
- Sandboxed evaluation  
- Multi‑session attacks  
- Threat modeling
