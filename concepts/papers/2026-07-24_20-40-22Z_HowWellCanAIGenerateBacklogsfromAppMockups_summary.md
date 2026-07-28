# Summary: 2026-07-24_20-40-22Z_HowWellCanAIGenerateBacklogsfromAppMockups.md
Saved: 2026-07-27 23:25
Source: 2026-07-24_20-40-22Z_HowWellCanAIGenerateBacklogsfromAppMockups.md
Model: None

---

## Summary  
This paper investigates how well artificial intelligence can generate project backlogs directly from visual app mockups, a task that traditionally relies on manual effort and can suffer from missed or inconsistent items such as epics, user stories, and tasks. The authors propose a multimodal prompting strategy using GPT‑4o to evaluate the effectiveness of three different approaches: a zero‑shot baseline, compositional chain‑of‑thought (CCoT) reasoning for vision‑language tasks, and a persona‑driven prompt that injects developer expertise. Their study spans seven app development projects across two countries and includes interviews with developers to capture subjective feedback on the generated backlogs.

## Key Contributions  
- Finding 1: The zero‑shot baseline tends to prioritize recall over precision, producing many items but often at low accuracy.  
- Finding 2: CCoT prompting yields a more balanced performance, achieving average F1 scores of 52–66 % for epics and user stories across the evaluated projects.  
- Finding 3: Adding architectural context to the prompt improves backend‑task precision by up to 35 %, though tasks remain challenging and developers still accept up to 26 % of false positives as useful.

## Methodology  
The authors adopt a multimodal approach that feeds app mockups (images) into GPT‑4o, which can process both visual and textual inputs. They test three prompting strategies: (1) a zero‑shot baseline where the model is given only the prompt “Generate backlog items from this screenshot,” (2) CCoT prompting that chains reasoning steps to reason about the mockup’s components before listing items, and (3) persona‑driven prompting that simulates a developer’s voice to guide output. The evaluation includes quantitative F1 scores for each item type and qualitative interviews with developers to assess perceived usefulness.

## Results  
Across the seven projects, the CCoT approach achieved an average F1 of 52–66 % for epics and user stories, indicating a moderate balance between recall and precision. Tasks such as backend implementation were more difficult; when architectural context was added, backend‑task precision improved by up to 35 %. Developer interviews revealed that roughly 26 % of the generated false positives were still considered valuable, highlighting the open‑ended nature of backlog creation.

## Significance  
These findings demonstrate that hybrid prompting—combining vision‑language reasoning with architectural context—can significantly reduce manual effort in sprint planning while preserving a level of accuracy. However, they also underscore that AI assistance does not replace human oversight; developers must still review and curate the output. The work contributes to the broader field of AI‑assisted software engineering by introducing a new evaluation metric, Revised Recall, which integrates ground‑truth data with developer assessments.

## Related Concepts  
- Multimodal AI (vision‑language integration)  
- Chain‑of‑thought prompting for reasoning tasks  
- F1 score as a balanced accuracy metric  
- Architectural context injection in prompts  
- Revised Recall, a hybrid recall measure incorporating human feedback  
- Sprint backlog generation and sprint planning  
- AI‑assisted software engineering workflows
