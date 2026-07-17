# Summary: 2026-07-16_17-58-36Z_SciDiagramEdit_LearningtoEditScientificDiagramsfro.md
Saved: 2026-07-16 23:01
Source: 2026-07-16_17-58-36Z_SciDiagramEdit_LearningtoEditScientificDiagramsfro.md
Model: None

---

## Summary  
The paper introduces **SciDiagramEdit**, a framework that learns to edit scientific figures from the natural‑language revisions recorded in arXiv manuscript histories. By treating figure editing as an instruction‑driven task on editable vector primitives, it moves beyond simple template replacement toward genuine visual reasoning. The authors demonstrate that skill evolution—where an agentic proposer refines its own editing strategy over multiple epochs—can dramatically improve edit accuracy on unseen revisions. This work thus bridges the gap between human manuscript revision intent and automated figure generation.

## Key Contributions  
- **Benchmark of Revision‑Grounded Pairs**: Mining before/after figure pairs from arXiv version histories creates a dataset where each edit is directly linked to authors’ revision intent, providing a natural training signal.  
- **Skill‑Evolution Framework**: The system uses an agentic learner that continuously updates its skill specification based on execution traces across epochs, enabling progressive improvement without retraining.  
- **Agentic Editing of Vector Primitives**: Instead of generating final images directly, the model edits individual vector elements (schematics, arrows, captions) under a user‑visible interface, preserving the original visual grammar.

## Methodology  
The authors first collected figure revisions from arXiv’s version history, extracting paired before/after vectors and the accompanying natural‑language instructions. They then trained an agentic model to propose edits by iteratively refining a skill specification derived from its own execution traces. The skill is parameterized as a set of primitive‑level actions (e.g., “move arrow X”, “replace label Y”). Over epochs, the model’s trace shows which primitives it modifies and how, allowing the skill spec to be updated incrementally. This closed‑loop learning mimics human co‑editing: users can inspect each primitive while the agent proposes refinements.

## Results  
On a held‑out validation set of 120 revision pairs, the skill‑evolved model achieved an average edit accuracy increase of **≈23 %** compared to a baseline that used static instructions. The improvement is most pronounced on complex diagrams containing multiple heterogeneous elements (schematics + plots). Moreover, user studies indicated that the agent’s intermediate proposals were perceived as more faithful to the authors’ revision intent than fully automated outputs.

## Significance  
Automating figure editing saves researchers significant time and reduces the risk of visual errors. By grounding edits in real‑world manuscript revisions, SciDiagramEdit provides a reliable, human‑informed training signal that can be applied across disciplines. The skill‑evolution approach also illustrates how iterative learning can enhance instruction‑driven AI tasks beyond static fine‑tuning.

## Related Concepts  
- **Skill evolution** – the process of refining an agent’s behavior through successive execution traces.  
- **Agentic learning** – a paradigm where the learner proposes its own modifications to improve performance.  
- **Vector primitives** – individual editable components (arrows, labels, shapes) that constitute scientific diagrams.  
- **Infographic editing** – the task of altering dense visual information while preserving semantic meaning.  
- **arXiv version history** – a repository of manuscript revisions that serves as a natural source of instruction‑editing data.
