---
title: Software Engineering LLMs: Why We Need Them and How Software Engineering Helps Build Them
url: http://arxiv.org/abs/2610.33851v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-24_18-45-18Z_SoftwareEngineeringLLMs_WhyWeNeedThemandHowSoftwar.md
generated_at: 2026-10-26 20:36
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper presents an industrial case study demonstrating how established software engineering (SE) knowledge can be systematically integrated into the training pipeline of a 92-billion-parameter coding LLM serving over 100,000 developers. The authors develop RefactorForge, a pipeline that leverages refactoring expertise, SE tooling, and verification techniques to construct high-quality training data for repository-level refactoring capabilities. Incremental supervised fine-tuning on just 0.46% of the preceding coding mixture's tokens yielded substantial improvements across multiple engineering benchmarks, validating that targeted SE-informed data construction is a highly efficient path to capability enhancement.

## Key Takeaways
- RefactorForge combines refactoring knowledge, established SE tools, and verification techniques to generate 5,704 executable tasks and retain 4,572 verified teacher trajectories totaling 72.51 million tokens across 306 Python repositories, demonstrating that rigorous SE-grounded data construction produces verifiable, high-quality training signals rather than relying on unfiltered synthetic data.
- Incremental supervised fine-tuning on these capability-focused trajectories, representing only 0.46% of the preceding coding mixture's tokens, improved RefactorBench performance by 18.00 percentage points and SWE-Bench ProMax by 7.06 points, showing that small, well-targeted SE-informed datasets can produce outsized capability gains compared to broad, undifferentiated training.
- The improvements generalized across multiple coding-agent harnesses under OpenCode, extending to SWE-Bench Verified (4.97 points) and SWE-Bench Pro (1.23 points), though greenfield repository generation showed mixed results, indicating that capability-focused training benefits targeted engineering tasks more reliably than open-ended generation tasks.

## Context
This work sits at the intersection of large language model training methodology and software engineering practice, addressing a critical gap in how coding LLMs are developed. Most current LLM training pipelines treat code as a generic text modality, without encoding the structured knowledge, verification practices, and engineering workflows that define professional software development. By grounding training data construction in established SE tools and verification techniques, this paper demonstrates a principled alternative to purely statistical or synthetic data generation approaches, and proposes a broader research agenda for transforming coding LLMs into true SE LLMs with defined engineering capabilities.

## Implications
For industry practitioners building and deploying coding LLMs, this research provides a concrete, reproducible methodology for injecting domain-specific engineering capabilities into model training without requiring massive data or compute budgets, offering a cost-effective path to improving developer-facing tools. For the broader AI research community, the proposed agenda of incorporating SE knowledge into model training, applying engineering methods to model development and maintenance, and systematically defining target engineering capabilities establishes a framework that could guide the next generation of specialized LLMs, shifting the field from general-purpose code generation toward verifiable, capability-targeted software engineering assistance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.33851v1)
