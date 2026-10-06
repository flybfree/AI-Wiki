---
title: SkillScriptBench: Benchmarking Self-Evolution of Executable Agent Skill Packages Beyond Markdown
published: 2026-10-02T20:10:12Z
authors: Yuxuan Liu, Haoran Li, Yuhao Zhang, Jiahe Guo, Hongyu Luo, Wenbin Hu, Huihao Jing, Kawai Chung, Junle Chen, Changxuan Fan, Qing Zong, Lingyun Xie, Yangqiu Song
url: http://arxiv.org/abs/2610.04008v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SkillScriptBench: Benchmarking Self-Evolution of Executable Agent Skill Packages Beyond Markdown

## Abstract
Executable Agent Skills combine natural-language instructions and scripts into reusable packages for LLM agents, and revising them requires fixing errors without breaking correct behavior. Existing benchmarks do not systematically distinguish documentation repair, script repair, and preservation when evaluating skill self-evolution. We introduce SkillScriptBench, a 350-task benchmark designed to evaluate these capabilities separately. From a survey of over 35,000 GitHub-hosted Skill roots, we select 100 packages and construct 150 repair tasks. Each task pairs a package containing injected script faults with a maintenance request and executable checks of the required behavior. A complementary controlled track contains 200 tasks from 50 packages, each evaluated under the same maintenance request in four states: clean, documentation faults, script faults, and faults in both. Across four LLMs, methods that edit both documentation and scripts can repair script faults but do not consistently outperform Markdown-only revision on documentation repair or preservation. We therefore introduce AST-Guided Skill Revision, which uses abstract syntax trees and calling relationships to link maintenance requirements to relevant code locations. It restricts script edits to these locations and updates the documentation to match the revised scripts. Averaged across models, this revision stage yields absolute gains in repair success of 21.9% for Raw Package and 27.7% for CoEvoSkills on faulty packages. Absolute gains in the proportion of tasks solved in all three runs reach 20.8% and 31.5%, respectively, indicating more consistent repair success across repeated runs.

## Metadata
- **Published**: 2026-10-02T20:10:12Z
- **Authors**: Yuxuan Liu, Haoran Li, Yuhao Zhang, Jiahe Guo, Hongyu Luo, Wenbin Hu, Huihao Jing, Kawai Chung, Junle Chen, Changxuan Fan, Qing Zong, Lingyun Xie, Yangqiu Song
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04008v1)