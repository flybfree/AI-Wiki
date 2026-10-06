---
title: TeleGen: Improving LLM-Based Web Application Generation via Runtime Telemetry
url: http://arxiv.org/abs/2610.04981v1
type: paper-summary
date: 2026-10-05
source_paper: 2026-10-04_05-57-12Z_TeleGen_ImprovingLLM_BasedWebApplicationGeneration.md
generated_at: 2026-10-05 22:19
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
TeleGen is an observability-enhanced framework designed to improve LLM-based web application generation by instrumenting generated applications, collecting runtime telemetry during task execution, and compressing that telemetry into concise briefs to guide code repair. Evaluated on WebGen-Bench and Web-Bench, TeleGen improves task success rates by 8.5 percentage points and cumulative Pass@2 by 8.1 percentage points over baseline generate-execute-repair pipelines that lack runtime telemetry, demonstrating that interaction-level diagnostic signals are critical for resolving failures in generated web applications.

## Key Takeaways
- Existing generate-execute-repair pipelines rely on task outcomes or error messages to guide code revision, but this feedback misses the runtime behavior between a browser action and the final task outcome, making interaction-level failures such as broken navigation flows or form submission errors extremely difficult to diagnose and fix. TeleGen addresses this gap by instrumenting the generated application to capture detailed runtime telemetry during task execution.
- Raw telemetry logs can be verbose and costly to feed back into an LLM for repair. TeleGen introduces a telemetry compression step that condenses raw logs into concise briefs, making the diagnostic signal both more effective for guiding repairs and less expensive in terms of token usage. Ablation studies confirm that the briefs outperform raw telemetry in improving repair quality.
- Telemetry is especially beneficial for failures involving hidden execution paths, including multi-step navigation sequences, form workflows, and frontend-backend coordination issues. These are failure modes where the final task outcome alone provides insufficient information to identify the root cause, but intermediate runtime signals reveal exactly where the interaction chain breaks down.

## Context
This paper sits at the intersection of LLM-based code generation and software observability, two areas that have largely developed independently. As LLMs increasingly generate full-stack web applications from natural-language prompts, the bottleneck shifts from initial code synthesis to post-generation debugging and repair. TeleGen bridges this gap by treating runtime instrumentation as a first-class component of the generation pipeline rather than an afterthought, signaling a shift toward feedback-rich, observability-aware generation workflows in the broader AI-assisted software engineering landscape.

## Implications
For practitioners building LLM-powered code generation tools, TeleGen demonstrates that investing in lightweight runtime instrumentation and telemetry compression can yield substantial gains in end-to-end task success without requiring fundamentally more capable models. For the industry, this approach suggests that observability infrastructure should be integrated into AI code-generation pipelines from the outset, particularly for interactive web applications where hidden execution paths are common failure sources. The framework also points toward a future where AI-generated software is not merely produced and tested, but continuously monitored and self-corrected through structured runtime feedback loops.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.04981v1)
