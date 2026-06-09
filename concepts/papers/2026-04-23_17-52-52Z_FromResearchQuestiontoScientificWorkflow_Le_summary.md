# Summary: 2026-04-23_17-52-52Z_FromResearchQuestiontoScientificWorkflow_Leveragin.md
Saved: 2026-04-29 02:45
Source: 2026-04-23_17-52-52Z_FromResearchQuestiontoScientificWorkflow_Leveragin.md
Model: qwen3.6:35b

---

## Summary
This paper addresses the critical gap in scientific workflow systems: the manual, expert-driven translation of natural language research questions into executable computational workflows. The authors propose an agentic AI architecture designed to automate this semantic process, enabling seamless conversion from a high-level query to a structured, reproducible workflow DAG. By decomposing the problem into intent extraction, deterministic generation, and domain knowledge encoding, the system significantly improves automation accuracy and efficiency for complex scientific tasks.

## Key Contributions
1. **Agentic Workflow Architecture:** Proposes a novel three-layer agentic architecture that separates non-deterministic natural language interpretation from deterministic workflow execution.
2. **Domain Knowledge Integration via 'Skills':** Introduces "Skills"—markdown documents containing vocabulary mappings, parameter constraints, and optimization strategies—to ground the LLM's output and ensure reproducibility.
3. **High Accuracy and Efficiency:** Demonstrates that integrating Skills dramatically improves intent accuracy (from 44% to 83%) while maintaining low computational overhead and cost for end-to-end scientific querying.

## Methodology
The proposed system operates in three layers:
1. **Semantic Layer (LLM):** An LLM interprets the natural language research question into a structured, formal intent representation.
2. **Knowledge Layer (Skills):** Domain experts author "Skills" to provide explicit knowledge constraints and vocabulary mappings, guiding the LLM's interpretation.
3. **Deterministic Layer:** Validated generators take the structured intent and produce reproducible workflow Directed Acyclic Graphs (DAGs), ensuring that identical intents always yield identical workflows regardless of LLM variability. The system was evaluated on a 1000 Genomes population genetics workflow running

[[From Research Question to Scientific Workflow: Leveraging Agentic AI for Science Automation]]