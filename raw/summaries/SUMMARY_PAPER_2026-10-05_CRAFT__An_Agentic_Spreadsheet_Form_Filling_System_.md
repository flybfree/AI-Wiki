---
title: CRAFT: An Agentic Spreadsheet Form Filling System with Template Awareness
url: http://arxiv.org/abs/2610.04437v1
type: paper-summary
date: 2026-10-05
source_paper: 2026-10-03_10-56-50Z_CRAFT_AnAgenticSpreadsheetFormFillingSystemwithTem.md
generated_at: 2026-10-05 22:03
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
CRAFT is a template-aware agentic framework designed to address the challenges of spreadsheet form filling, where agents must consolidate external evidence, ground values to precise cells, and preserve irregular template structures without corrupting labels or misaligning fields. The system introduces a Rectangle-Aware Slot Grounder (RASG) and a reflective validation pipeline that constrains local repair rather than regenerating entire workbooks, yielding improvements of 8.51 and 23.38 percentage points in pair accuracy over the strongest baselines on two benchmark tracks.

## Key Takeaways
- CRAFT replaces free-form regeneration with structured, region-grounded repair: when errors are detected, the system identifies the specific spreadsheet region affected, restores corrupted template state, and re-grounds plausible writable slots before any subsequent edits are applied. This prevents cascading errors where early misalignments propagate and overwrite critical labels or field structures.
- The Rectangle-Aware Slot Grounder (RASG) component proposes candidate writable cells while label-slot hints and protected regions constrain which cells the agent may modify. This structural adjudication ensures that the agent respects the irregular geometry of real-world spreadsheet templates rather than treating them as uniform grids, and component-removal experiments confirm that both structural adjudication and slot re-grounding are essential to the pipeline's performance.
- The authors introduce FormFillBench, a new benchmark comprising 327 forms split into Instruction-Only and Multi-File tracks, providing a standardized evaluation harness for spreadsheet form-filling agents. CRAFT demonstrates that its relative advantage persists even when paired with a second backbone model, suggesting the framework's gains are architectural rather than dependent on a specific language model.

## Context
Agentic systems that interact with structured data formats like spreadsheets represent a growing frontier in AI research, bridging the gap between large language model reasoning and precise, layout-sensitive document manipulation. Prior approaches typically treat spreadsheet editing as a free-form generation task, which fails to account for the rigid template structures, merged cells, and label-field relationships that characterize real-world forms. CRAFT's contribution lies in formalizing template awareness as a first-class architectural constraint within an agentic pipeline, aligning with broader trends toward structured tool use, constrained generation, and verification-guided editing in autonomous agents.

## Implications
For practitioners in finance, legal compliance, and enterprise data management who routinely fill structured forms from heterogeneous source documents, CRAFT offers a principled method to reduce costly manual correction cycles caused by misaligned or overwritten fields. The public availability of both the code and FormFillBench lowers the barrier for downstream researchers to benchmark and improve spreadsheet-grounding agents, potentially accelerating the deployment of reliable AI assistants in document-heavy workflows where template integrity is non-negotiable.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.04437v1)
