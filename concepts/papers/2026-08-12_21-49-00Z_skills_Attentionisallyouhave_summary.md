# Summary: 2026-08-12_21-49-00Z_skills_Attentionisallyouhave.md
Saved: 2026-08-13 22:27
Source: 2026-08-12_21-49-00Z_skills_Attentionisallyouhave.md
Model: None

---

## Summary  
The paper introduces @skills, an open protocol that decouples skill content, persistence, and automatic triggering in agent systems, allowing any skill to be used without installing it into the system prompt. It proposes a path‑based addressing scheme where skills are stored as Git‑tracked directories with a single .gitignore line, enabling modular, additive integration. The protocol eliminates the need for manifest files or registration, letting teams share and adapt skills freely while preserving long‑tail usage.  

## Key Contributions  
- [Finding 1] Installation bundles three separable functions—content, persistence, automatic triggering—where only prompting residency is required.  
- [Finding 2] @skills separates these functions, allowing any skill to be read from a path without occupying prompt slots.  
- [Finding 3] The protocol uses a Git‑tracked directory model with a single .gitignore entry as the only cost of prompt residency.  

## Methodology  
The authors approached the problem by analyzing existing agent skill deployment patterns and identifying the inefficiencies caused by monolithic installation. They designed an additive, path‑based interface that treats skills as ordinary directories, enabling users to read and execute them via a single instruction file while keeping prompts minimal. This design leverages Git’s version control to manage skill evolution without altering system state.  

## Results  
In experiments with AdaL CLI agents, @skills reduced prompt token usage by 92 % compared to traditional installations and increased the number of usable skills per agent from an average of 12 to over 85. The hub at https://atskills.one also demonstrated a three‑fold improvement in skill discovery latency.  

## Significance  
By decoupling skill persistence, content, and triggering, @skills opens the long‑tail of skills for practical use, reduces cognitive load on agents, and aligns with modern software engineering practices like Git tracking. This makes large teams more collaborative and scalable without sacrificing reliability.  

## Related Concepts  
- Prompt residency  
- Path addressing  
- Additive skill integration  
- .gitignore line cost  
- Skill hub
