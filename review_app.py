"""FastAPI review dashboard for AI research summaries.

Run from the wiki checkout:
    uvicorn review_app:app --reload --port 8765
"""
from __future__ import annotations

from html import escape
from pathlib import Path
from urllib.parse import quote

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from curation import bulk_delete_rejected, delete_rejected, list_candidates, profile, record_decision

app = FastAPI(title="AI Wiki Curation")


class Decision(BaseModel):
    path: str
    decision: str
    note: str = ""


class BulkReview(BaseModel):
    keep_paths: list[str] = []
    delete_paths: list[str] = []
    note: str = "bulk page review"


def _page() -> str:
    return r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>AI Wiki Curation</title>
<style>
:root{color-scheme:dark;--bg:#101216;--panel:#191c22;--line:#303641;--text:#edf0f5;--muted:#9ca5b3;--green:#43d17b;--red:#ff6f7d;--amber:#f4c95d;--blue:#7cb8ff}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:15px/1.5 system-ui,sans-serif}header{border-bottom:1px solid var(--line);padding:24px max(24px,calc((100vw - 1280px)/2));display:flex;justify-content:space-between;gap:20px;align-items:end}h1,h2,h3{margin:0 0 8px;line-height:1.15}h1{font-size:30px}h2{font-size:20px}h3{font-size:17px}p{margin:8px 0;color:var(--muted)}main{max-width:1280px;margin:0 auto;padding:24px}.layout{display:grid;grid-template-columns:300px 1fr;gap:20px}.panel,.card{background:var(--panel);border:1px solid var(--line);border-radius:12px}.panel{padding:18px;height:max-content}.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:16px 0}.stat{border:1px solid var(--line);border-radius:8px;padding:10px}.stat b{display:block;font-size:22px}.stat span{font-size:12px;color:var(--muted)}.filters{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:14px}button,select{border:1px solid var(--line);background:#232832;color:var(--text);border-radius:7px;padding:9px 12px;cursor:pointer}button:hover{border-color:#657188}.active{border-color:var(--blue);color:var(--blue)}.queue{display:grid;gap:12px}.card{padding:18px}.card-head{display:flex;justify-content:space-between;gap:18px}.card-title{font-size:18px;font-weight:650}.meta{font-size:12px;color:var(--muted);margin-top:6px;word-break:break-word}.meta a{color:var(--blue)}.score{min-width:76px;text-align:right;color:var(--amber);font-weight:700}.preview{margin:15px 0;color:#cbd1db}.tags{display:flex;gap:6px;flex-wrap:wrap}.tag{font-size:11px;color:#b8c7dc;background:#222d3d;border-radius:999px;padding:3px 8px}.actions{display:flex;gap:8px;align-items:center;margin-top:15px}.keep{background:#17472e;border-color:#296a46;color:#a6f2c1}.reject{background:#4b2028;border-color:#71303b;color:#ffb3bd}.skip{background:#2c2d31}.note{flex:1;min-width:180px;background:#11151b;border:1px solid var(--line);color:var(--text);border-radius:7px;padding:9px}.empty{padding:40px;text-align:center;color:var(--muted);border:1px dashed var(--line);border-radius:10px}.profile-list{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}.pill{font-size:12px;border-radius:999px;padding:4px 8px;background:#233c2e;color:#a6f2c1}.avoid{background:#45262b;color:#ffb3bd}.notice{color:var(--muted);font-size:13px;border-top:1px solid var(--line);padding-top:14px;margin-top:16px}@media(max-width:800px){.layout{grid-template-columns:1fr}header{display:block}.score{min-width:60px}}
</style></head><body>
<header><div><h1>AI Wiki Curation</h1><p>Review research summaries before they shape the wiki. Your decisions train a local preference profile.</p></div><div id="reviewed"></div></header>
<main><div class="layout"><aside class="panel"><h2>Your curation profile</h2><div class="stats"><div class="stat"><b id="kept">0</b><span>kept</span></div><div class="stat"><b id="rejected">0</b><span>rejected</span></div><div class="stat"><b id="pending">0</b><span>pending</span></div></div><h3>Topics you keep</h3><div id="liked" class="profile-list"></div><h3 style="margin-top:18px">Topics you reject</h3><div id="avoided" class="profile-list"></div><div class="notice">Rejecting permanently deletes the curated wiki summary and its Logseq mirror after confirmation. Raw source captures are retained for provenance.</div></aside><section><div class="filters"><button data-status="pending" class="active">Needs review</button><button data-status="all">All decisions</button><button data-status="keep">Kept</button><button data-status="reject">Rejected</button><button id="refresh">Refresh</button><button id="bulk-delete" class="reject" onclick="bulkDelete()">Keep checked / delete rest on page</button></div><div id="queue" class="queue"></div></section></div></main>
<script>
let status='pending', page=0;
const selectionKey='ai-wiki-curation-selection';
function selectedPaths(){try{return new Set(JSON.parse(localStorage.getItem(selectionKey)||'[]'))}catch{return new Set()}}
function toggleSelection(box){const paths=selectedPaths();box.checked?paths.add(box.dataset.path):paths.delete(box.dataset.path);localStorage.setItem(selectionKey,JSON.stringify([...paths]))}
const esc=s=>String(s??'').replace(/[&<>'"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]));
async function load(){const [q,p]=await Promise.all([fetch('/api/candidates?status='+status+'&limit=50&offset='+(page*50)).then(r=>r.json()),fetch('/api/profile').then(r=>r.json())]);
 document.querySelector('#reviewed').textContent=p.reviewed+' reviewed'; document.querySelector('#kept').textContent=p.kept;document.querySelector('#rejected').textContent=p.rejected;document.querySelector('#pending').textContent=q.filter(x=>x.decision==='pending').length;
 document.querySelector('#liked').innerHTML=p.liked_topics.map(x=>`<span class="pill">${esc(x)}</span>`).join('')||'<p>No learned preferences yet.</p>';document.querySelector('#avoided').innerHTML=p.avoided_topics.map(x=>`<span class="pill avoid">${esc(x)}</span>`).join('')||'<p>No rejected topics yet.</p>';
 document.querySelector('#queue').innerHTML=q.length?q.map(card).join(''):'<div class="empty">No summaries in this view.</div>';document.querySelector('#bulk-delete').disabled=status!=='pending';
 document.querySelector('#queue').insertAdjacentHTML('beforeend',`<div class="filters"><button id="prev" ${page?'':'disabled'}>Previous</button><span style="padding:9px;color:var(--muted)">Page ${page+1}</span><button id="next" ${q.length<50?'disabled':''}>Next</button></div>`);
 document.querySelector('#prev').onclick=()=>{page--;load()};document.querySelector('#next').onclick=()=>{page++;load()};}
function card(x){return `<article class="card"><div class="card-head"><div><label><input type="checkbox" class="keep-check" data-path="${esc(x.path)}" ${selectedPaths().has(x.path)?'checked':''} onchange="toggleSelection(this)"> Keep this paper</label><div class="card-title">${esc(x.title)}</div><div class="meta">${esc(x.path)}${x.source?` · <a href="${esc(x.source)}" target="_blank" rel="noreferrer">source</a>`:''}</div></div><div class="score">${Math.round(x.score*100)}% fit</div></div><div class="tags">${x.tags.map(t=>`<span class="tag">${esc(t)}</span>`).join('')}</div><p class="preview">${esc(x.preview)}</p><div class="actions"><input class="note" placeholder="Optional note" data-note="${esc(x.path)}" value="${esc(x.note)}"><button class="keep" onclick="decide('${encodeURIComponent(x.path)}','keep')">Keep</button><button class="reject" onclick="decide('${encodeURIComponent(x.path)}','reject')">Reject</button><button class="skip" onclick="decide('${encodeURIComponent(x.path)}','skip')">Skip</button></div></article>`}
async function bulkDelete(){if(status!=='pending')return;const checks=[...document.querySelectorAll('.keep-check')],keep_paths=checks.filter(x=>x.checked).map(x=>x.dataset.path),delete_paths=checks.filter(x=>!x.checked).map(x=>x.dataset.path);if(!delete_paths.length){alert('Nothing to delete — every paper on this page is checked.');return}if(!confirm(`Keep ${keep_paths.length} checked paper(s) and permanently delete ${delete_paths.length} unchecked paper(s) from the wiki and Logseq?`))return;const r=await fetch('/api/bulk-review',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({keep_paths,delete_paths})});if(!r.ok){alert(await r.text());return}localStorage.removeItem(selectionKey);load()}
async function decide(encoded,decision){const path=decodeURIComponent(encoded),note=document.querySelector(`[data-note="${CSS.escape(path)}"]`)?.value||'';if(decision==='reject'&&!confirm('Permanently delete this summary from the wiki and Logseq?'))return;const endpoint=decision==='reject'?'/api/rejections':'/api/decisions';const r=await fetch(endpoint,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({path,decision,note})});if(!r.ok){alert(await r.text());return}load()}
document.querySelectorAll('[data-status]').forEach(b=>b.onclick=()=>{status=b.dataset.status;page=0;document.querySelectorAll('[data-status]').forEach(x=>x.classList.toggle('active',x===b));load()});document.querySelector('#refresh').onclick=()=>{page=0;load()};load();
</script></body></html>'''


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    return _page()


@app.get("/api/candidates")
def candidates(status: str = "pending", limit: int = 50, offset: int = 0):
    if status not in {"pending", "all", "keep", "reject", "skip"}:
        raise HTTPException(400, "invalid status")
    return list_candidates(status, limit=limit, offset=offset)


@app.get("/api/profile")
def get_profile():
    return profile()


@app.post("/api/decisions")
def decisions(payload: Decision):
    try:
        return record_decision(payload.path, payload.decision, payload.note)
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc


@app.post("/api/rejections")
def rejections(payload: Decision):
    try:
        return delete_rejected(payload.path, payload.note)
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc


@app.post("/api/bulk-review")
def bulk_review(payload: BulkReview):
    try:
        for path in payload.keep_paths:
            record_decision(path, "keep", payload.note)
        result = bulk_delete_rejected(payload.delete_paths, payload.note) if payload.delete_paths else {}
        return {"kept": payload.keep_paths, **result}
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
