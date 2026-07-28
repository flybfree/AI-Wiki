# Summary: 2026-07-27_14-01-32Z_FromExecutiontoCapability_ScientificExperienceCons.md
Saved: 2026-07-27 23:00
Source: 2026-07-27_14-01-32Z_FromExecutiontoCapability_ScientificExperienceCons.md
Model: None

---

## Summary  
This paper addresses a critical limitation in large language models' scientific computing capabilities: while these models can solve individual problems, their runtime experiences do not reliably translate into durable procedural knowledge that improves performance on new tasks. The authors introduce SciConsolidate, a novel framework for converting verified execution outcomes—both successes and failures—into transferable computational procedures. By synthesizing such procedural knowledge without requiring pre-existing reference answers, they enable persistent model improvement through abstraction-execution gap bridging.

## Key Contributions  
- [Finding 1] The authors demonstrate that concrete procedural synthesis from runtime experience significantly enhances model performance on subsequent scientific-computing tasks, establishing a pathway from execution to capability.  
- [Finding 2] They identify the abstraction-execution gap as a key obstacle: target models may fail to operationalize valid abstractions derived from source tasks, even when those procedures are correct and executable by stronger models.  
- [Finding 3] Experimental results show that procedure-guided concretization improves Qwen3.6-27B by +3.85/+6.26 sub-step/main-problem points but yields minimal gain for the smaller Qwen3.5-9B model, providing strong evidence of the gap and the necessity of stronger models to concretize procedures.

## Methodology  
The authors approach the problem by contrasting verified successes and failures across tasks to extract computational mechanisms that are task-general rather than source-specific. They use a development-validation gate to select only those procedures that transfer well between tasks, then employ failure-informed, answer-free query synthesis to generate new consolidation data without relying on human-written references. A stronger model serves as a "concretizer," translating abstract procedures into executable code supervision for standard SFT, while a matched no-procedure teacher branch isolates the value of procedural guidance.

## Results  
On SciCode benchmark, procedure injection improves Qwen3.6-27B by +3.85/+6.26 sub-step/main-problem points but yields almost no aggregate main-problem gain for Qwen3.5-9B, confirming the abstraction-execution gap. After procedure-guided concretization, the 9B model improves under procedure-free deployment by +3.89/+6.25 over SFT control and +5.62/+11.25 over its original baseline, showing that procedural knowledge can compensate for weaker models.

## Significance  
This work establishes a scalable mechanism for scientific experience consolidation, moving beyond isolated task solving to persistent model improvement through procedural synthesis. It provides empirical evidence of the abstraction-execution gap and offers a practical foundation for self-improving scientific assistants, potentially enabling long-term learning from individual executions.

## Related Concepts  
- Procedural knowledge synthesis  
- Abstraction-execution gap  
- Task generalization in AI  
- Self-consolidating models  
- Scientific computing with LLMs
