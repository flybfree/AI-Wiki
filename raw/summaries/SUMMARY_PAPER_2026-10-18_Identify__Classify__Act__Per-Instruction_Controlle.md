---
title: Identify, Classify, Act: Per-Instruction Controlled Compliance for LLMs over External Data
url: http://arxiv.org/abs/2610.22874v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-16_03-24-08Z_Identify_Classify_Act_Per_InstructionControlledCom.md
generated_at: 2026-10-18 21:00
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces EDIC (External-Data Instruction Classification), a framework that addresses the critical challenge of per-instruction compliance when LLMs process external data containing a mix of legitimate directives and adversarial prompt injections. Rather than applying blanket suppression or blanket trust to all external instructions, EDIC decomposes the problem into an identify-classify-act pipeline that attributes compliance credit at the individual instruction level. The authors demonstrate that this approach simultaneously improves safety (up to 7.7% higher harmful-rejection) and utility (up to 12.5% higher Arena-Hard-Auto scores) compared to the strongest prior defenses, evaluated across two model backbones and five benchmarks.

## Key Takeaways
- The core insight is that existing defenses fail because they treat all external instructions uniformly, collapsing the safety-utility frontier into a binary choice between over-refusal and over-compliance. EDIC formalizes the missing capability as per-instruction credit attribution, requiring the model to identify each embedded directive, classify it as beneficial or harmful, and act accordingly on a per-instruction basis rather than at the document or tool-return level.
- The training pipeline is deliberately decomposed: a scene-grounded data generation stage injects mixed beneficial and harmful instructions with counterfactual filtering to create realistic adversarial scenarios, while a generative judge model is first initialized via supervised fine-tuning (SFT) and then refined using GRPO (Group Relative Policy Optimization) to perform instruction-level compliance attribution. The judge produces a dual-component reward that separately encourages beneficial compliance and penalizes harmful compliance, enabling reinforcement learning training that optimizes both objectives without the typical trade-off.
- Empirical results on Qwen3-4B show EDIC lifts harmful-rejection by up to 7.7% and Arena-Hard-Auto utility by 12.5% over the strongest prior defense, evaluated across five benchmarks and two backbones, demonstrating that the approach generalizes beyond a single model architecture and that the gains in safety do not come at the cost of reduced task utility.

## Context
As LLMs increasingly interact with external data sources such as retrieved documents, tool outputs, and multi-turn conversation histories, the risk of adversarial prompt injection embedded within otherwise legitimate content has become a dominant security concern. Prior defenses typically operate at the document or system level, either filtering out all external instructions or trusting them wholesale, which creates a fundamental tension between safety and usefulness. This paper matters because it reframes prompt injection defense as a fine-grained classification and attribution problem rather than a binary trust decision, aligning with the broader research trend toward compositional and decomposed reasoning in language model safety.

## Implications
For practitioners deploying LLM agents in retrieval-augmented generation, tool-use pipelines, or multi-agent systems, EDIC offers a practical path toward maintaining high task performance while selectively rejecting adversarial instructions embedded in external data, reducing the operational pressure to over-refuse useful content. The decomposed reward structure and the use of GRPO for judge refinement suggest a scalable training recipe that could be adapted to domain-specific compliance policies, making it relevant for regulated industries such as finance, healthcare, and legal AI where per-instruction auditability of model behavior is increasingly required. The open-source code repository further lowers the barrier for the community to validate, extend, and integrate these techniques into production agent frameworks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.22874v1)
