# Summary: 2026-07-30_14-34-41Z_Tycho_ActiveAbstractionwithProgrammaticWorldModels.md
Saved: 2026-07-30 20:38
Source: 2026-07-30_14-34-41Z_Tycho_ActiveAbstractionwithProgrammaticWorldModels.md
Model: None

---

## Summary  
The paper introduces **Tycho**, a coding‑agent framework that treats the ARC‑AGI‑3 game series as an active abstraction problem: agents must infer hidden rules, state, and goals while minimizing costly actions. By separating raw observations from structured events (animation, level completion, game‑over), Tycho enables agents to build executable world models, test hypotheses, repair them, or bypass them, thereby achieving high relative human action efficiency. The authors demonstrate that orchestrating model construction with a policy yields the best performance across all 25 public games.

## Key Contributions  
- [Finding 1] **Active abstraction as an interactive skill‑acquisition task** – formalizing ARC‑AGI‑3 environments as parameterized deterministic Moore machines and defining the joint problem of generating testable models from costly interaction.  
- [Finding 2] **Programmatic world‑model construction and orchestration** – a coding‑agent system that produces executable hypotheses, repairs verification failures automatically, and decides when to use or bypass these models.  
- [Finding 3] **Superior action efficiency with model‑driven policies** – the actor‑requested delegation policy reaches 88.49 RHAE, while GPT‑5.6 Sol and Opus 5 achieve perfect 100 % RHAE, completing all levels and outperforming human baselines.

## Methodology  
Tycho treats each ARC‑AGI‑3 level as a sequence of frames that are parsed into three categories: actionable observations (player inputs), intermediate animation (visual effects), and terminal events (level win/loss). The agent maintains a structured history, extracts the deterministic transition set, and feeds it to a model builder. Orchestration policies decide whether to construct a new hypothesis, repair an existing one after verification failure, use it for planning, or bypass it entirely. This process is repeated per policy, with Claude Opus 4.8 providing inference under matched budgets.

## Results  
In 25 public games (183 levels total), the actor‑requested delegation policy yields a mean Relative Human Action Efficiency of **88.49**, the highest among four tested policies. GPT‑5.6 Sol and Opus 5 both reach **100 % RHAE**, completing every level. Their game‑balanced first‑run human‑replay midranks are 98.5 and 100.0, respectively. Opus 5 reduces scored actions by 61 % compared with the aggregate official human baselines. Automatic repair after verification failures produces models that reproduce observed transitions at **83.07 RHAE**, indicating that transition match is a necessary but insufficient condition for strong play.

## Significance  
Tycho bridges the gap between raw interaction and efficient abstraction, offering a scalable approach to active learning in complex games. By automating model construction and repair, it reduces human cognitive load while preserving high performance, which could be transferred to other domains requiring on‑the‑fly world modeling (e.g., robotics, autonomous navigation). The work also clarifies the trade‑off between transition fidelity and action efficiency, providing a benchmark for future active abstraction systems.

## Related Concepts  
- **Moore machine** – a finite‑state automaton that captures deterministic transitions.  
- **Active abstraction** – generating testable models from costly interaction.  
- **World model** – an executable hypothesis about the underlying dynamics of an environment.  
- **Relative Human Action Efficiency (RHAE)** – metric comparing agent action counts to human baselines.
