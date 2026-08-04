# Summary: 2026-08-03_08-51-50Z_HarnessCompass_GuidingAutomaticHarnessEvolutiontow.md
Saved: 2026-08-03 23:46
Source: 2026-08-03_08-51-50Z_HarnessCompass_GuidingAutomaticHarnessEvolutiontow.md
Model: None

---

## Summary  
HarnessCompass is a novel automatic harness evolution framework that improves how large language models interact with executable environments. It tackles the problems of over‑fitting to specific tasks, reliance on trajectory data alone, and cross‑component interference by integrating constrained evolution, proactive first‑person feedback, and component‑wise optimization. The method enables rapid, effective harness refinement on SWE‑bench Verified with GPT‑5.4, raising Pass@1 from 54 % to 66 % in only five iterations while preserving strong generalization across tasks.

## Key Contributions  
- [Finding 1] HarnessCompass introduces constrained evolution that restricts modifications to task‑agnostic changes, thereby promoting generalization beyond the particular evolution tasks.  
- [Finding 2] The framework augments trajectory‑derived evidence with proactive first‑person feedback from the agent about harness usage, yielding richer signals for improvement.  
- [Finding 3] It decouples the optimization of different harness components before consolidation, reducing cross‑component interference while preserving component synergy.

## Methodology  
HarnessCompass follows three stages. First, it defines global constraints that limit evolution to changes not specific to a single task, ensuring broader applicability. Second, during each iteration the agent supplies first‑person feedback on its harness usage; this feedback is merged with trajectory data to guide targeted modifications. Third, optimization of each component (e.g., prompt template, tool selection) is performed independently using separate loss functions; after convergence, components are merged into a unified harness.

## Results  
On SWE‑bench Verified with GPT‑5.4, HarnessCompass achieves Pass@1 = 66 % in five evolution steps, outperforming the baseline AHE (Automatic Harness Evolution) which typically reaches ~58 %. Moreover, the evolved harness transfers effectively to held‑out tasks and other models, demonstrating substantially stronger generalization than prior automatic harness evolution methods.

## Significance  
This work advances automatic harness design by making evolution more efficient, less prone to overfitting, and better at transferring performance across diverse tasks and models. It reduces development time for LLM agents in executable environments and opens a path toward truly generalizable AI assistants.

## Related Concepts  
Harnesses, automatic harness evolution, constrained optimization, trajectory‑derived signals, first‑person feedback, component‑wise optimization, generalization, SWE‑bench Verified, GPT‑5.4.
