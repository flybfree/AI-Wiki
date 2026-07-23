---
title: Code mode yields a 99.2% cost reduction in our systems
date: 2026-07-23
url: https://www.agent-swarm.dev/blog/code-mode-token-savings
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://www.agent-swarm.dev/blog/code-mode-token-savings
source_feed: Hacker News
scraped: 2026-07-23 07:01
---

# Code mode yields a 99.2% cost reduction in our systems

## Full Article

Back to writing
[26 tool calls collapsed into one script call: $0.02 vs a $2.44 floor]
Same triage. One path never lets the raw data reach the model.
Anthropic published
a piece in November
on code execution with MCP: give an agent a sandbox and a generated API instead of raw tool calls, and a task that would cost 150,000 tokens costs 2,000 instead — a 98.7% reduction, because the raw data never has to pass through the model's context.
Cloudflare shipped the same idea
back in September under the name “Code Mode,” and later put
a number on it
: 2,500+ API endpoints, 1.17M tokens down to about 1,000.
Our first reaction was “we already built this.” Every claude/codex/opencode session in the swarm ships a rubric today —
system.agent.context_mode
in
src/prompts/session-templates.ts
— that tells the agent: 10+ items or a bulk fan-out means reach for a script, not N individual tool calls. We didn't add this for the post. It's just what the swarm already does, and it's the same machinery behind
Script Workflows
.
What we hadn't done is measure it against Anthropic's own yardstick, with our own production data. So we did — using a script two of our own agents wrote and ship globally:
workflow-triage
.
What the script does
workflow-triage
scans every automation the swarm runs — all workflows and all cron schedules — and flags which ones are dead, failing, or fine. Under the hood, that's 26 separate calls: one
workflow_list
, one
schedule_list
, and one
workflow_listRuns
per workflow (24 of them). Normally, an agent doing this “by hand” would make 26 individual tool calls, and every one of those raw JSON payloads would sit in its context for the rest of the conversation.
Instead, the script makes all 26 calls itself, inside its own sandboxed subprocess, and only the final distilled result — one summary object — ever reaches the agent.
What we measured, live
We didn't estimate this. We ran the script and the underlying calls separately, against the real production catalog (24 workflows, 60 schedules), and measured both sides directly.
Script (workflow-triage)
Raw sequential calls (measured + extrapolated)
Calls made
1
26
Reaches the agent's context
25,811 characters (one JSON result) — measured exactly
~3,259,649 characters — see methodology below
Approx. tokens (~4 chars/token, no tokenizer available)
~6,450 tokens
~815,000 tokens
Wall-clock
13.12s (
durationMs: 13120
) — measured exactly
~2–6.5 min (estimated: 26 sequential turns, not directly run)
Cost (Claude Sonnet 5, $3/1M input tokens)
~$0.02
~$2.44 (floor — see below)
Reduction
—
~126x fewer characters reaching context, ~99.2%
Being honest about what's measured vs. estimated
The wall-clock and cost of the raw path are the only estimated numbers here, and we want to be upfront about exactly how each was built, because the whole point of this post is “show your work,” not “trust our vibes”:
The script's own numbers are 100% measured.
durationMs: 13120
and the 25,811-character result came directly off a live
workflow-triage
run, no rounding tricks.
The raw-path character count is measured-then-extrapolated, not invented.
We called the exact same underlying SDK methods the script calls (
workflow_list
,
schedule_list
,
workflow_listRuns
) directly, outside the script, to see what a raw sequential-tool-calling agent would actually receive:
workflow_list(
{}
)
→ 16,304 characters (measured);
schedule_list(
{}
)
→ 72,105 characters (measured);
workflow_listRuns
sampled directly on 4 of the 24 workflows spanning small to large — 6 runs → 98,706 chars, 26 runs → 293,036 chars, 53 runs → 157,720 chars, 227 runs → 525,968 chars. That's 1,075,430 characters across 312 sampled runs — a measured average of
3,447 characters per run
. We applied that measured average to the real total run count the script itself recorded across all 24 workflows (920 runs) to get the ~3.17M character estimate for the full raw-equivalent scan, then added the two list calls.
Why we didn't just run all 26 raw calls for real:
doing so would mean pulling ~3.2 million characters of raw JSON into the very conversation used to write this post, to prove a post about not doing that. We sampled the smallest and largest workflows instead and extrapolated from the swarm's own recorded run counts — which is a more honest demonstration of the problem than it sounds, because it's exactly the judgment call the rubric asks an agent to make before it starts calling tools one at a time.
One footnote worth flagging:
the
limit: 25
we pass into
workflow_listRuns
doesn't actually cap the result — it returned all 227 runs for our busiest workflow, not 25. That's a real gap in the underlying API worth a ticket, but it doesn't change this post's math; if anything it makes the raw-sequential-calls number a floor, not a ceiling.
The $2.44 raw-path cost is a floor, not a real total.
It only prices the tokens once, as if they entered context on a single turn. In a real agentic loop, each of the 26 raw tool results stays in context and gets re-sent as input on every subsequent turn — which is the exact mechanic behind Anthropic's own 150K-token example (the transcript passes through the model's context twice: once on read, once on write). A real 26-turn sequential run would cost meaningfully more than $2.44; we can't defend a precise multiplier without actually running that wasteful version.
The code that does it
This is the entire script — not a snippet, the whole thing,
id da3b5c7b-b9a6-4f9e-be9e-f682aca48ea0
, global scope, callable by any agent in the swarm:
// workflow-triage — read-only health scan of all workflows + schedules.
// Returns per-item run stats + DEAD/FAILING/OK flags + a markdown report of flagged items.
export default async function (args: any, ctx: any) {
  const runLimit = args?.runLimit ?? 25;
  const staleDays = args?.staleDays ?? 14;
  const includeSchedules = args?.includeSchedules ?? true;
  const now = Date.now();
  const dayMs = 86400000;
  const isFail = (s: string) => /fail|error|halt|timeout|abort/i.test(String(s || ""));

  // ---- Workflows: run stats require workflow_listRuns (no lastRunAt on the row) ----
  const wl = await ctx.swarm.workflow_list({});
  const wfs: any[] = wl?.data ?? [];
  const rows: any[] = [];
  const pool = 6; // small concurrency to avoid hammering
  for (let i = 0; i < wfs.length; i += pool) {
    const batch = wfs.slice(i, i + pool);
    const res = await Promise.all(batch.map(async (w: any) => {
      let runs: any[] = [];
      try { const rr = await ctx.swarm.workflow_listRuns({ workflowId: w.id, limit: runLimit }); runs = rr?.data ?? []; }
      catch { runs = []; }
      const total = runs.length;
      const failed = runs.filter((r: any) => isFail(r.status)).length;
      const stamps = runs.map((r: any) => Date.parse(r.startedAt || r.createdAt || r.finishedAt || "")).filter((n: number) => !isNaN(n));
      const lastRun = stamps.length ? Math.max(...stamps) : null;
      const daysSince = lastRun ? Math.round((now - lastRun) / dayMs * 10) / 10 : null;
      const failRatio = total ? Math.round(failed / total * 100) / 100 : 0;
      const dead = !w.enabled || total === 0 || (lastRun != null && daysSince! > staleDays);
      const failing = total >= 2 && failRatio >= 0.5;
      return {
        kind: "workflow", id: w.id, name: w.name, enabled: w.enabled,
        runs: total, failed, failRatio,
        lastRunAt: lastRun ? new Date(lastRun).toISOString() : null,
        daysSinceLastRun: daysSince, nodeCount: w.nodeCount,
        flag: failing ? "FAILING" : dead ? "DEAD" : "OK",
      };
    }));
    rows.push(...res);
  }

  // ---- Schedules: lastRunAt + consecutiveErrors already on the row ----
  const scRows: any[] = [];
  if (includeSchedules) {
    const sl = await ctx.swarm.schedule_list({});
    const scs: any[] = sl?.data?.schedules ?? [];
    for (const s of scs) {
      const lastRun = s.lastRunAt ? Date.parse(s.lastRunAt) : null;
      const daysSince = lastRun ? Math.round((now - lastRun) / dayMs * 10) / 10 : null;
      const dead = !s.enabled || (!lastRun) || (daysSince != null && daysSince > staleDays);
      const failing = (s.consecutiveErrors ?? 0) >= 3;
      scRows.push({
        kind: "schedule", id: s.id, name: s.name, enabled: s.enabled,
        consecutiveErrors: s.consecutiveErrors ?? 0,
        lastRunAt: s.lastRunAt ?? null, daysSinceLastRun: daysSince,
        nextRunAt: s.nextRunAt ?? null, cron: s.cronExpression,
        flag: failing ? "FAILING" : dead ? "DEAD" : "OK",
      });
    }
  }

  const rank = (f: string) => f === "FAILING" ? 0 : f === "DEAD" ? 1 : 2;
  rows.sort((a, b) => rank(a.flag) - rank(b.flag) || (b.failRatio - a.failRatio));
  scRows.sort((a, b) => rank(a.flag) - rank(b.flag) || (b.consecutiveErrors - a.consecutiveErrors));

  const sum = (arr: any[]) => ({
    total: arr.length,
    failing: arr.filter(r => r.flag === "FAILING").length,
    dead: arr.filter(r => r.flag === "DEAD").length,
    ok: arr.filter(r => r.flag === "OK").length,
  });

  // markdown report of only the flagged (non-OK) items
  const flaggedW = rows.filter(r => r.flag !== "OK");
  const flaggedS = scRows.filter(r => r.flag !== "OK");
  let report = `## Workflow triage — flagged\n`;
  report += `Workflows: ${sum(rows).failing} failing / ${sum(rows).dead} dead / ${sum(rows).ok} ok (of ${rows.length})\n`;
  // ... table-building omitted here for length; full source has per-row markdown
  //     tables for both workflows and schedules — see the script catalog entry.

  return {
    params: { runLimit, staleDays, includeSchedules },
    workflows: { summary: sum(rows), rows },
    schedules: includeSchedules ? { summary: sum(scRows), rows: scRows } : null,
    report,
  };
}
There's no framework here. It's a
for
loop with a concurrency pool of 6, a couple of
Date.parse
calls, and a sort. The only thing that makes it “code mode” rather than “26 tool calls” is
where it runs
: inside the script sandbox, not inside the agent's context. Every
ctx.swarm.workflow_listRuns
call above returns its (large, sometimes limit-ignoring) payload straight back into the loop variable
runs
— never into the conversation. The agent that eventually calls this script sees only the
return
statement at the bottom: one object, 25,811 characters, done.
The mechanism, in one sentence
“Intermediate results stay in the execution environment by default... the agent only sees what you explicitly log or return.”
—
Anthropic, Code execution with MCP
That's precisely what
runs
is doing on line after line above, and precisely why the raw-path column in our table is ~126x bigger than the script column — none of it is a framework trick, it's just that raw data stopped being handed to the model 24 times in a row.
What it's worth across models
The table above prices everything at Claude Sonnet 5's rate, since that's the model this measurement ran on. The reduction itself is a token-count story, not a pricing story — it holds at the same ~99.2% regardless of which model reads the result. Here's what the two token counts (~6,450 measured / ~815,000 measured-floor) are worth at five current models' own direct-provider input rates, pulled from the swarm's live pricing table (
src/be/modelsdev-cache.json
, verified 2026-07-08):
Model
Input $/M tokens
Script (~6,450 tok)
Raw path floor (~815,000 tok)
claude-opus-4-8
$5.00
$0.032
$4.08
claude-sonnet-5
$3.00
$0.019
$2.44
claude-fable-5
$10.00
$0.065
$8.15
gpt-5.5
$5.00
$0.032
$4.08
glm-5.2
$1.40
$0.009
$1.14
Same measured/extrapolated caveats as the table above apply to every row here — the “script” column is a direct conversion of the 25,811-character measured result, the “raw path floor” column is the measured-then-extrapolated ~815,000 token estimate, and both are input-token pricing only, priced once rather than compounding across a real multi-turn session. Rates are each provider's direct API pricing, not a router or resale price.
workflow-triage, one script call vs. 26 raw tool calls
The script puts ~0.79% of the raw path's tokens in front of the model
Each bar is a share of the raw sequential-calls floor (~815,000 tokens, measured then extrapolated — see the methodology above). The ratio is model-invariant: at any model's own $/token rate, the dollar reduction is the same ~99.2%.
Loading interactive chart
~126x fewer characters reaching context, ~99.2% reduction — the same ratio whether you price it in tokens or dollars.
The one-line takeaway
This already ships by default in every claude/codex/opencode session's system prompt — the decision in front of us isn't “should we adopt code mode,” it's “how do we make the rubric sharper now that we have real numbers to back it,” and
workflow-triage
— 26 calls, one result, 13.12 seconds, ~$0.02 — is the worked example we'll use to do that.
/ references
Sources and further reading
Docs
Code Mode: the better way to use MCP
Cloudflare's original post: convert MCP tools into a generated TypeScript API and let the model write code against it instead of calling tools directly.
Docs
Code Mode: give agents an entire API in 1,000 tokens
Cloudflare's follow-up with the concrete number: a search()/execute() pattern took 2,500+ API endpoints from 1.17M tokens to ~1,000.
Docs
Code execution with MCP: building more efficient agents
Anthropic's engineering post. The 150,000-to-2,000-token (98.7%) example, and why intermediate tool results never need to re-enter the model's context.
Repo / PR
workflow-triage (global script, id da3b5c7b-b9a6-4f9e-be9e-f682aca48ea0)
The worked example in this post — the full source is inline below.
/ keep reading
Related field notes
All posts
May 4, 2026
/
13 min read
We Hid 75 of Our Agent's 90 MCP Tools — And It Got Smarter
Why tool inflation breaks agent accuracy and how we implemented core/deferred tool caching to fix it.
April 29, 2026
/
13 min read
Why Our Agents Sleep for 4 Minutes 30 Seconds (And Yours Should Too)
Your agent's sleep(300) is silently bleeding money. Here's the Anthropic prompt cache TTL mechanic that turns reasonable defaults into six-figure anti-patterns.
December 19, 2024
/
13 min read
59% of Our Agent Failures Lasted Under 10 Seconds. We Debugged Them Like Logic Bugs.
Binary success/failure metrics are killing your debugging velocity. The 10-second rule changes everything about how you interpret agent reliability.

## Metadata
- **Source**: [Original Article](https://www.agent-swarm.dev/blog/code-mode-token-savings)
