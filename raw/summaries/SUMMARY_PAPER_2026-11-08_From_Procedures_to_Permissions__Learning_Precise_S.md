---
title: From Procedures to Permissions: Learning Precise Subagent Authorization from Agent Skills
url: http://arxiv.org/abs/2611.08905v1
type: paper-summary
date: 2026-11-08
source_paper: 2026-11-06_02-46-06Z_FromProcedurestoPermissions_LearningPreciseSubagen.md
generated_at: 2026-11-08 21:24
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces a method for learning precise subagent authorization in multi-agent language systems by leveraging the procedural knowledge embedded in Agent Skills. Rather than relying solely on task outcomes or execution trajectories to supervise which tools and workspace resources a delegated subagent should access, the authors synthesize step-by-step procedures from Skills, execute them through subagent delegation in interactive environments, and use verified trajectories to construct training data for both task execution and authorization. Their approach yields substantial improvements in permission precision and task success on the ClawArena-Team benchmark while remaining competitive on Terminal-Bench 2.1 and SkillsBench.

## Key Takeaways
- Existing agent systems control tools and execution environments at a global level but fail to specify the precise resources required by each individual delegated subtask, creating a supervision gap that task outcomes and execution trajectories alone cannot fill. The authors identify this as a fundamental limitation in current multi-agent orchestration frameworks.
- Agent Skills encode procedural knowledge describing the specific operations, tools, and files required at each step of a task, making them a natural and rich source of supervision for authorization decisions. By synthesizing tasks and step-by-step procedures from these Skills and executing them through subagent delegation, the authors generate verified training trajectories that directly teach the model which permissions are appropriate for each subtask.
- On ClawArena-Team, the method improves tool permission precision by 13.4 percentage points and workspace permission precision by 24.1 percentage points, while increasing overall task success by 11.6 percentage points for Qwen3.5-35B-A3B. On Terminal-Bench 2.1 and SkillsBench, the approach remains competitive with existing agent data synthesis methods, demonstrating generalizability across evaluation settings.

## Context
As language agents increasingly tackle complex, multi-step tasks, multi-agent orchestration has become a dominant paradigm in AI systems, with specialized subagents handling distinct subtasks under a coordinating agent. However, the field has largely focused on what each subagent should do rather than precisely which tools, files, and workspace resources it should be granted access to, leaving a critical gap in safe and efficient delegation. This paper addresses that gap by connecting the growing ecosystem of Agent Skills—structured procedural knowledge used in agent frameworks—to the problem of authorization supervision, offering a principled data-synthesis pipeline that transforms procedural specifications into training signals for permission assignment.

## Implications
For practitioners building multi-agent systems, this work provides a concrete recipe for generating high-quality training data that teaches models to assign precise tool and workspace permissions to subagents, reducing both over-permissioning (security risk) and under-permissioning (task failure). For the broader AI research community, it demonstrates that structured procedural knowledge already embedded in agent frameworks can serve as a supervision source that outcome-based signals cannot replicate, suggesting a new direction for data synthesis in agent training. Industry deployments of agentic systems in software engineering, data analysis, and automation pipelines stand to benefit directly from tighter permission control, improving both reliability and safety of autonomous agent workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.08905v1)
