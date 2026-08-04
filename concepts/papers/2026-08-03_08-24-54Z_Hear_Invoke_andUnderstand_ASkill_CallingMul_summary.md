# Summary: 2026-08-03_08-24-54Z_Hear_Invoke_andUnderstand_ASkill_CallingMultimodal.md
Saved: 2026-08-03 23:45
Source: 2026-08-03_08-24-54Z_Hear_Invoke_andUnderstand_ASkill_CallingMultimodal.md
Model: None

---

## Summary  
The paper proposes SpeechAgent‑R, a skill‑calling multimodal agent that enables large audio language models to perform complex acoustic tasks by invoking external tools and reasoning over intermediate observations. It learns structured interaction behaviors through trajectory‑based supervised fine‑tuning and then refines them with multi‑turn reinforcement learning. The approach is evaluated on the HIU‑Corpus, which contains 65,492 interaction trajectories and 507.6 hours of audio across 24 tasks, eight skills, and nine tools, using a joint evaluation benchmark called HIU‑Bench that includes in‑distribution (ID) and out‑of‑distribution (OOD) splits with substantial shifts in tool usage. Results show that SpeechAgent‑R achieves 84.17 on ID tasks and 70.94 on OOD tasks, improving over the baseline by 15.40 and 14.23 points respectively.

## Key Contributions  
- [Finding 1] Construction of HIU‑Corpus with 65,492 interaction trajectories and 507.6 hours of audio across 24 tasks, eight skills, and nine tools.  
- [Finding 2] Development of SpeechAgent‑R that integrates multimodal understanding with skill‑calling and tool invocation via supervised fine‑tuning followed by reinforcement learning.  
- [Finding 3] Introduction of HIU‑Bench for joint evaluation of task performance, interaction quality, and generalization to diverse task settings.

## Methodology  
The authors approach the problem by first building a richly annotated dataset where human agents generate audio‑language interactions that involve multiple skills and tools. They train SpeechAgent‑R on these trajectories using supervised fine‑tuning to map raw audio inputs to appropriate skill calls, then apply multi‑turn reinforcement learning to optimize the agent’s dialogue policy for higher interaction quality. Evaluation is performed on HIU‑Bench, which splits tasks into ID and OOD sets with varying tool usage patterns, allowing a comprehensive assessment of both performance and generalization.

## Results  
SpeechAgent‑R achieves 84.17 on in‑distribution tasks and 70.94 on out‑of‑distribution tasks. Compared to the baseline model under the same agent harness, it improves by 15.40 points on ID tasks and 14.23 points on OOD tasks, demonstrating substantial gains in both accuracy and adaptability.

## Significance  
These results prove that learning skill and tool coordination can markedly enhance audio agents’ ability to handle diverse task settings and perform adaptive tool interactions, moving the field toward more capable, real‑world multimodal systems that can reason beyond static classification. The work also establishes a benchmark (HIU‑Bench) for evaluating such agentic capabilities.

## Related Concepts  
Audio language models, multimodal agents, skill calling, reinforcement learning, trajectory fine‑tuning, out‑of‑distribution evaluation, tool interaction, hierarchical task planning.
