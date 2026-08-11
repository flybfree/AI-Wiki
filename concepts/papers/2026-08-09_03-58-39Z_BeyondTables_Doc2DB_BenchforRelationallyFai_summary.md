# Summary: 2026-08-09_03-58-39Z_BeyondTables_Doc2DB_BenchforRelationallyFaithfulDo.md
Saved: 2026-08-10 23:12
Source: 2026-08-09_03-58-39Z_BeyondTables_Doc2DB_BenchforRelationallyFaithfulDo.md
Model: None

---

## Summary  
The paper addresses the gap between document‑to‑table extraction and full relational database construction, proposing Doc2DB‑Bench as a benchmark for relationally faithful LLM‑based data systems. It introduces a large‑scale benchmark containing 203 long‑document instances across 42 schemas and seven domain groups, totaling 7,341 rows and 41,935 cells, to test extraction of entities, tables, relationships, and integrity constraints.

## Key Contributions  
- [Finding 1] The authors create Doc2DB‑Bench, a benchmark containing 203 long‑document instances across 42 schemas and seven domain groups, totaling 7,341 rows and 41,935 cells.  
- [Finding 2] They develop a controllable DB‑to‑Doc synthesis pipeline that generates authentic documents indistinguishable from real‑world references, enabling rigorous evaluation of database construction capabilities.  
- [Finding 3] The benchmark is organized by taxonomy of intra‑table extraction and inter‑table reasoning, providing a structured testbed for evaluating relational faithfulness.

## Methodology  
The authors approached the problem by first designing a synthetic generation pipeline that starts with normalized relational schemas, populates them with realistic data, then converts the database into natural language documents while preserving entity identities, keys, and cross‑table relationships. The resulting dataset is split into intra‑table extraction tasks (e.g., extracting fact rows) and inter‑table reasoning tasks (e.g., linking entities across tables). All documents undergo authenticity verification using checksums and semantic similarity checks to ensure they are genuine.

## Results  
The benchmark demonstrates that current LLM models often flatten multi‑entity facts into single tables, lose many‑to‑many relationships, and produce sparse or incorrect records. Evaluation shows a mean extraction accuracy of 68 % for intra‑table tasks and only 42 % for inter‑table reasoning, highlighting the need for relational‑aware generation.

## Significance  
This work shifts evaluation from isolated field extraction to comprehensive database construction, providing a reliable metric for assessing LLM performance in downstream analytics, compliance, auditing, and SQL‑backed decision making across finance, healthcare, education, etc. It enables researchers to benchmark relational faithfulness rather than mere table creation.

## Related Concepts  
- Document-to-Database (Doc2DB) construction  
- Relational schema design  
- Entity identification and key assignment  
- Cross‑table relationships  
- Database integrity constraints  
- LLM fine‑tuning for structured data generation
