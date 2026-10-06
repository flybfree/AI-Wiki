---
title: Runaway Reaction: When Benign Skills Compose into Malicious Behavior
url: http://arxiv.org/abs/2610.05943v1
type: paper-summary
date: 2026-10-05
source_paper: 2026-10-05_07-59-28Z_RunawayReaction_WhenBenignSkillsComposeintoMalicio.md
generated_at: 2026-10-05 22:54
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates a critical security gap in agent skill marketplaces: individually vetted, benign skills can compose together to produce malicious behaviors that no single skill could exhibit alone. The authors introduce CRIME (Compositional Risk Induction via Multi skill Execution), a systematic framework that decomposes target malicious behaviors into complementary skill requirements, iteratively refines skill selections through execution feedback, and validates outcomes in a sandboxed environment. They also construct a benchmark of 4,000 public skills spanning eight cybersecurity behaviors to evaluate composition-induced vulnerabilities at scale.

## Key Takeaways
- Direct composition of individually benign skills can already induce malicious behaviors, even when every constituent skill passes standalone security vetting. This means current marketplace vetting pipelines, which evaluate skills in isolation, systematically miss emergent risks that arise only when skills interact within an agent's execution loop.
- The CRIME framework addresses this gap through three coordinated modules: Malicious Plot Casting (MPC) decomposes a target malicious behavior into complementary capability requirements and identifies candidate benign skill compositions from public repositories; Runaway Reaction Steering (RRS) iteratively refines skill selections using execution feedback while enforcing that each skill remains benign under standalone vetting; and the Skill Reaction Chamber (SRC) executes the composed skill pair in a sandbox and examines environmental consequences to confirm whether the target behavior actually occurred.
- Some target malicious behaviors remain difficult to realize through direct composition even when the selected skills collectively provide the required capabilities, highlighting that capability availability does not guarantee behavioral emergence. The iterative refinement loop in RRS is specifically designed to bridge this gap, and unsuccessful compositions are fed back for further adjustment.

## Context
As agent skill marketplaces proliferate, agents increasingly assemble task-specific knowledge and procedures from public repositories to handle complex workflows. Existing security research has focused on evaluating individual skills for safety, but the compositional dimension—how benign capabilities interact to unlock behaviors unavailable to any single skill—has remained largely unexplored. This paper fills that gap by formalizing composition-induced risk as a first-class security concern and providing both a methodological framework and a large-scale benchmark to study it.

## Implications
For practitioners deploying agents in production, this work signals that per-skill security audits are insufficient; marketplace operators and enterprise buyers must adopt composition-aware vetting pipelines that test skill interactions in sandboxed environments before deployment. The 4,000-skill benchmark across eight cybersecurity behaviors provides a concrete starting point for stress-testing agent pipelines against emergent malicious behavior. For the broader AI safety community, the finding that capability composition can unlock behaviors no individual skill exhibits suggests that alignment and safety evaluation must shift from unit-level to system-level analysis as agent architectures grow more modular and composable.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.05943v1)
