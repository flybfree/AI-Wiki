# Summary: 2026-07-20_04-08-06Z_CanAIAgentsReallyCompleteRTL_to_GDS_LessonsfromBen.md
Saved: 2026-07-24 00:12
Source: 2026-07-20_04-08-06Z_CanAIAgentsReallyCompleteRTL_to_GDS_LessonsfromBen.md
Model: None

---

## Summary  
The paper investigates whether general‑purpose AI agents can reliably execute an end‑to‑end RTL‑to‑GDS flow that includes synthesis, physical implementation, and ECO optimization using commercial EDA tools. It evaluates several LLM‑based agent architectures against four foundation models on a PicoRV32 design under two timing targets, measuring progress with design scores, stage completion, and Token ROI—a cost‑efficiency metric linking runtime to quality. The study finds that while domain‑specific skills help agents understand individual subtasks, they do not guarantee successful completion of the long‑horizon workflow. Moreover, even when agents reach comparable design stages, their Token ROI can vary by up to 141×, highlighting large differences in efficiency and cost. Finally, low‑level tool‑interface mismatches—especially version‑dependent Tcl commands—lead to frequent physical‑design failures.

## Key Contributions  
- [Finding 1] Domain‑specific skills improve agents’ comprehension of individual subtasks but do not ensure reliable completion of a long‑horizon EDA flow.  
- [Finding 2] Agents that achieve similar design progress can differ by up to 141 times in Token ROI, revealing substantial variations in runtime and cost efficiency.  
- [Finding 3] Low‑level tool‑interface mismatches are a major source of physical‑design failures, particularly when Tcl commands depend on the tool version or execution mode.

## Methodology  
The authors constructed a benchmark workflow for the PicoRV32 RTL‑to‑GDS flow using two commercial EDA tools. They deployed three AI agent architectures and four foundation models to run the entire synthesis‑implementation chain under both timing targets. Progress was quantified by an end‑to‑end design score, stage completion percentages, and Token ROI (runtime × cost). The agents were compared on these metrics across all model versions.

## Results  
Design scores ranged from 0.62 to 0.89, with most agents completing synthesis but stalling at physical implementation. Stage completion varied widely; only one architecture reached >75% of the full flow. Token ROI differences spanned up to a factor of 141, indicating that agents with similar design quality could have vastly different operational costs. Additionally, several designs failed due to Tcl command mismatches caused by tool‑version dependencies.

## Significance  
The findings suggest that robust Agentic EDA is not achieved merely through stronger foundation models; it also requires structured tool interfaces, persistent design context, controlled execution, and process‑level evaluation. Without these safeguards, even advanced agents cannot guarantee reliable or cost‑effective RTL‑to‑GDS completions.

## Related Concepts  
LLM agents, EDA workflow automation, RTL‑to‑GDS flow, synthesis, physical implementation, ECO optimization, Token ROI, tool‑interface mismatch, Tcl command dependencies, version‑specific execution modes.
