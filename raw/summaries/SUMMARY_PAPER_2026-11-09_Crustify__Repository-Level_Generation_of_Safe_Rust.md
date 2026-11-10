---
title: Crustify: Repository-Level Generation of Safe Rust Bindings with LLM Agents and Coverage-Guided Testing
url: http://arxiv.org/abs/2611.10394v1
type: paper-summary
date: 2026-11-09
source_paper: 2026-11-07_02-00-16Z_Crustify_Repository_LevelGenerationofSafeRustBindi.md
generated_at: 2026-11-09 21:24
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
Crustify is an agentic co-translator system that automatically generates safe Rust bindings for repository-level C libraries, addressing the long-standing challenge of manually writing error-prone, unsafe C-to-Rust interop code. The system schedules C symbols into dependency-ordered waves processed concurrently by LLM agents, validates bindings through coverage-guided equivalence and undefined-behavior testing under sanitizers and Miri, and achieved coverage of approximately 42% of public APIs on libgit2 and ffmpeg within roughly 52–59 hours of human-in-the-loop development.

## Key Takeaways
- Crustify introduces three novel supporting tools: ffibox provides Rust primitives for C/Rust interop that mirror Box, Arc, and Vec semantics for C objects while never forming a reference to memory that C may alias; Wavefront is a neuro-symbolic static analyzer that orders target items by their true dependencies, including those hidden behind casts and type-erased pointers; and ffimap is a rustc-based analysis mapping the unsafe surface of generated bindings. These tools collectively enable safe, automated binding generation at repository scale.
- The agentic pipeline organizes a target library's types and symbols into dependency-ordered waves of independent batches that agents bind concurrently, derive ownership and lifecycle contracts for every pointer and type, and undergo wave-level review. This structured scheduling prevents agents from generating bindings out of order and ensures correctness dependencies are respected across the entire repository.
- Validation is rigorous: coverage-guided equivalence tests and UB tests run under sanitizers and Miri, achieving 98.92% and 99.07% Rust code coverage on libgit2 and ffmpeg respectively. Human reviewers fixed 8 and 13 defects that caused undefined behavior reachable from Rust, demonstrating that automated generation still benefits from targeted human review for subtle UB issues.

## Context
This work sits at the intersection of LLM-based program synthesis, formal verification, and systems programming. Safe Rust bindings for C libraries have historically been written by hand because the Rust compiler cannot verify the correctness of unsafe code blocks, making a single mistake a source of undefined behavior. By combining LLM agents with neuro-symbolic static analysis and runtime verification tools like Miri and sanitizers, Crustify demonstrates that the automation gap between C and Rust interop can be closed. It is, to the authors' knowledge, the first work to automate safe Rust binding generation for C libraries at repository scale, establishing a new benchmark for AI-assisted systems programming.

## Implications
For industry practitioners migrating C codebases to Rust, Crustify offers a practical path to incremental, safe interop without requiring teams to hand-write thousands of unsafe binding functions, reducing both development time and the risk of subtle UB bugs. For the AI research community, the paper validates a hybrid neuro-symbolic approach where LLM agents handle creative binding generation while deterministic static and dynamic analyzers enforce correctness, suggesting a template for future agentic software engineering systems. The low residual unsafe surface (1.6% and 0.4% of public functions) indicates that fully safe bindings are achievable at scale, potentially accelerating the broader Rust ecosystem's adoption of existing C libraries.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.10394v1)
