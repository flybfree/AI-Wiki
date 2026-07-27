---
title: PGSimCity - How PostgreSQL Works
date: 2026-07-26
url: https://nikolays.github.io/PGSimCity/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://nikolays.github.io/PGSimCity/
source_feed: Hacker News
scraped: 2026-07-26 20:28
---

# PGSimCity - How PostgreSQL Works

## Full Article

PGSimCity one PostgreSQL cluster

Buffer pool (shared_buffers)a 1,024-frame sample of the page cache every backend reads through+8

Backends one process per connection+17

Storage the platters — everything above exists to avoid this+29

Standby a second cluster, replaying+11

Clients+4

WAL+6

Maintenance+2

Query lab

**PG**SIMCITY 16.0 s

TPS

7

Cache hit

73.6%

WAL

23.5 KiB/s

Dirty pages

55

Repl lag

0.0s

22 Checkpoint in 21.2 s

Sound off Day[Source](https://github.com/NikolayS/PGSimCity "View the PGSimCity source code on GitHub")View[](http://nikolays.github.io/PGSimCity/observability/ "Diagnose — start from a symptom, end at the pg_stat_* column that proves it")Walk

18 FPS 217 particles

View & destinations

Labels on Home Overview Fly

Fly to a district Swipe →

1 Clients 2 Backends 3 Buffer pool (shared_buffers)4 WAL 5 Storage 6 Query lab 7 Maintenance 8 Standby

Console

Defaults

Workload

What the application is asking for

Transactions / sec 10 tps

How hard the application hammers the database. Everything downstream scales from here.

Writes 20%

Share of statements that modify data. Reads are cheap; writes create WAL, dirty pages and dead tuples.

Updates vs inserts 60%

An UPDATE in Postgres writes a new row version and leaves the old one behind for vacuum.

Sequential scans 15%

Reads that walk the whole table instead of using an index — watch the buffer cache churn.

Memory

How much of the database fits in RAM

shared_buffers 2 GiB

Postgres's own page cache, sized here in real MiB/GiB. The plaza is a fixed 1,024-frame sample of that pool; each MiB implies 128 8 KiB buffers.

Background writer on- [x] 

Trickles dirty pages out just ahead of the clock sweep so backends rarely have to write a victim themselves. There is no on/off GUC — in Postgres you disable it with bgwriter_lru_maxpages = 0, the slider below; bgwriter_delay only changes how often it wakes.

bgwriter_lru_maxpages 100 pages/round

Ceiling on how much the background writer may clean per round.

Write-ahead log

Durability, and what it costs

synchronous_commit on

How long COMMIT waits before telling the client yes. The single biggest latency/durability trade-off in Postgres.

wal_level replica

How much detail goes into the WAL. More detail means more bytes, and more things you can build on it.

full_page_writes on- [x] 

The first write to a page after a checkpoint logs the entire 8 KiB page — protection against torn writes, and the reason WAL volume surges from the moment each checkpoint starts.

Checkpoints

Getting dirty pages onto disk

max_wal_size 256 MiB

When WAL grows past this, a checkpoint is forced whether it was due or not.

checkpoint_timeout 60 s 1m 00s

Maximum time between checkpoints. Longer means less write amplification but slower crash recovery.

checkpoint_completion_target 0.90

Spreads the checkpoint write phase over this fraction of the interval instead of dumping it all at once.

Autovacuum

Reclaiming dead rows

autovacuum on- [x] 

Turn it off and watch dead rows pile up until the tables are mostly corpses. Never do this in production.

autovacuum_vacuum_scale_factor 0.02

A table is vacuumed once this fraction of its rows are dead. Lower means more frequent, cheaper vacuums. PostgreSQL defaults to 0.2; this city starts at 0.02, the kind of per-table setting the docs recommend for a busy relation, so the yard is not idle for a whole visit.

Replication

Keeping a second copy

Standby connected on- [x] 

Whether a physical standby is streaming from this primary.

Network latency 30 ms

One-way network delay to the standby. synchronous_commit = on waits for a LOCAL flush and pays none of it; only remote_apply makes a commit wait for the round trip.

Slow replay off- [x] 

The standby receives WAL fine but cannot apply it fast enough — the classic source of replication lag.

Long standby query off- [x] 

A long read on the standby reports its xmin through hot_standby_feedback and pins cleanup on the primary.

Break something

The failure modes worth recognising

Long-running transaction off- [x] 

One forgotten open transaction pins the xmin horizon, so vacuum can no longer remove row versions whose deleting transaction has not fallen behind it. Bloat forever.

Lock contention off- [x] 

A conflicting lock on a hot table. Watch the waiters queue up and latency go vertical.

Playback

Simulation controls

Speed 1.0×

Simulation speed. Slow it down to watch a single commit; speed it up to watch a day of checkpoints.

Pause off- [x] 

Freeze the city mid-flight and fly around it.

Restore defaults stock configuration

Fly to

## Nothing selected

Click a building to open it up

Click any building.

Every structure in the city is one real mechanism inside Postgres. Open one and it explains itself, with its own live counters and the parameters that govern it.

Start here

Buffer pool (shared_buffers)a 1,024-frame sample of the page cache every backend reads through checkpointer writes every dirty page, then fsyncs — the latency spike you feel autovacuum worker 0 scans a table and removes what MVCC left behind — if allowed to Standby a second cluster, replaying

1–8 jump between districts · T takes the guided tour

Where this comes from

The explanations lean on the PostgreSQL documentation, Bruce Momjian’s talks and slides, Hironobu Suzuki’s “The Internals of PostgreSQL”, and Egor Rogov’s “PostgreSQL 14 Internals”. With thanks — and to be clear, none of them is involved in this project or has reviewed it. Every mistake you find here is this project’s own.

1×

Reset◈Scenarios

Scenarios

No scenario free running

13 · scroll →

◈Steady state◐Checkpoint storm▦Cache thrash◍Bloat and vacuum◔The xmin horizon◼Lock pile-up◎Replication lag◇The commit trade-off◫Index scan vs seq scan◒Without the bgwriter◉Connection storm◊Logical decoding▩Full-page writes

First time here?
Take the guided tour — the whole city in 14 chapters, about 4 minutes.

Start the tour Dismiss

Scenario

01/ 14

Guided tour
## A client connects

Everything starts with a TCP connection. The postmaster has been listening since the server booted: it checks who you are, checks the database exists, and then does something no thread pool would ever do — it forks an entire new process to serve you, and steps out of the way. Watch the pulse leave the tower and land in the row of buildings ahead.

16s

Exit

## Controls & legend

Everything you can press, and what every colour in the city means

Controls Colours Reading

### Camera

LMB drag Pan — grab the ground and move it RMB drag Orbit around the city MMB drag or Ctrl+LMB Pan and orbit, for model-viewer habits Wheel Zoom 1 finger Pan the map 2 fingers Pinch to zoom · twist to turn · drag up or down to tilt Left thumb Walk — a small stick push walks; a full push runs Right thumb Look — drag while the left thumb keeps moving Jump Crouch Jump / toggle crouch · while swimming, hold to rise / dive Click Select a building — in fly mode, capture the mouse W A S D Fly — arrow keys work too Space or E Rise C or Q Descend Shift Boost Alt Precision — slow, fine movement PgUp PgDn Change altitude Esc Leave pointer lock
### Application

K or P Pause / resume the simulation,.Slower / faster (0.1× – 5×)T Guided tour R Reset — restart with default settings F Toggle fly / orbit camera · desktop; touch uses Walk mode G Get down — walk the city on foot, 1.7 m tall Walk button Touch equivalent of G; Exit walk returns to the map H Establishing shot of the whole city · View menu O Overview — straight down on the plate · View menu/or Ctrl K Command palette?This panel L Toggle floating labels · View menu N Daylight / night · theme control beside Sound M Sound on / off — audio starts off and remembers your choice Esc Close the topmost overlay 1…8 Jump to a district · View menu on phones

1 – 8 Clients · Backends · Buffer pool (shared_buffers) · WAL · Storage · Query lab · Maintenance · Standby

* * *

### Colour legend

Client`#5f96c4`Application connections and the rows travelling back to them

Postmaster`#6a63d9`The supervisor process, and every fork it performs

Backend`#0089b5`One OS process per connection — your query runs in here

Shared memory`#4b2fd0`Structures every backend can see: ProcArray, locks, CLOG

Clean page`#1d5fcb`A buffer that matches what is on disk — free to evict

Dirty page`#e02b46`Modified in memory only. Somebody must write it out

Pinned page`#efbc16`In use right now — the clock sweep may not take it

WAL`#b8720a`Write-ahead log records: the durability contract

Archive`#7d6018`Completed WAL segments shipped to archive storage

Storage`#17954f`Heap files, the data directory, and physical disk I/O

Index`#05a47e`B-tree and GIN structures, and index-only lookups

TOAST`#c9451f`Oversized values pushed out of the main heap

Vacuum`#8b2bc0`Autovacuum workers and the dead tuples they collect

Checkpoint`#c42d92`The checkpointer flushing dirty pages to disk

bgwriter`#0e8f8c`Background cleaning ahead of the clock sweep

Replication`#e2690d`WAL on the wire, and the standby replaying it

Lock`#c62f28`A heavyweight lock, and the queue of backends waiting on it

* * *

### How to read the city

**The plaza** — The lit grid in the centre is `shared_buffers` — one tile per 8 KiB page, blue when it matches disk, red when it has been modified in memory and not yet written. The rotating hand is the clock sweep looking for a frame to reuse.

**The pit** — The ground is cut away beneath the plaza. That excavation is the data directory: heap files, indexes, TOAST and the disks. Every trip down there is a page that was not in cache.

**The WAL district** — Everything east of the plaza is the write-ahead log. Changes go there **before** they reach the data files, and a commit waits for that amber stream to be flushed — never for the pages themselves.

**The ground** — The city stands on a poured plate with a kerb and an edge light, and beyond that kerb there is nothing. The plate is cut to the outline of Slonik, the PostgreSQL elephant: the trunk runs north over the client terminal, the ear lies south-west over the standby and recovery sites, and the brow reaches east over the WAL district. Press `O` to look straight down at it.

**The standby** — South of the city, one TCP connection carries WAL to a second cluster where a single process replays it in order. When it cannot keep up, that gap is your replication lag.

**Early, unreviewed prototype.** PGSimCity is a teaching model, not a real server: the mechanisms are modelled, the numbers are simulated, and no PostgreSQL source code runs here. It was built quickly and **almost certainly contains inaccuracies and mistakes**, in both the simulation and the explanations.

Found one? Corrections from people who know the engine are exactly what this needs — please [open an issue](https://github.com/NikolayS/PGSimCity/issues/new) or send a [pull request](https://github.com/NikolayS/PGSimCity/pulls).

# PG SimCity

A working model of the PostgreSQL engine

ready

**Early, unreviewed prototype.** It almost certainly contains inaccuracies in both the model and explanations. Found one? [Open an issue](https://github.com/NikolayS/PGSimCity/issues/new) or send a [pull request](https://github.com/NikolayS/PGSimCity/pulls).

MOVE DRAG TO LOOK

Crouch Jump

↑Exit walk

esc

↑↓navigate⏎open esc close

POSTGRESQL · PHYSICAL ANATOMY
## Heap page anatomy

One 8 KiB page · byte-scaled · live relation state

8 KiB page Data directory

live simulation · selected relation

**sessions**block 15

latest resident block · occupancy from relation counters

live tuples**29.4k**

dead tuples**610**

relation bloat**2.0%**

page free**818 B**

VM signal**clear / unknown**

R
**Representative, not decoded.** Relation counters drive density and deadness; a real resident block number is used when available. The simulation does not retain each block’s tuple bytes.

one heap page · exact byte proportions
### 0 → 8,192 bytes

BLCKSZ = 8192

0 304 · pd_lower pd_upper · 1122 8192

line pointers grow forward →← tuples grow backward

PageHeaderData 24 B · 0…23 Line pointers 70 × 4 B · 280 B Free space 818 B · 304…1122 Heap tuples 7,070 B · grow backward Special 0 B on heap

bytes 0…23
### PageHeaderData

24 B

pd_lsn 8 B pd_checksum 2 B pd_flags 2 B pd_lower 2 B pd_upper 2 B pd_special 2 B pd_pagesize_version 2 B pd_prune_xid 4 B

slot array
### ItemIdData[]

70 slots · 69 normal · 1 dead

lp_off 15 bits lp_flags 2 bits lp_len 15 bits

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70

LP_UNUSED 0 · reusable LP_NORMAL 1 · tuple LP_REDIRECT 2 · HOT LP_DEAD 3 · cleanup

tuple opened · HOT teaching example
### HeapTupleHeaderData → bitmap → user data

23 B fixed

t_xmin 4 B xid 100,017 t_xmax 4 B xid 100,023 · updated t_cid / t_xvac 4 B union cid 0 · shared word t_ctid 6 B(15,2) → newer t_infomask2 2 B natts 6 · HOT_UPDATED t_infomask 2 B HASNULL · XMIN_COMMITTED t_hoff 1 B 24 · MAXALIGN null bitmap 1 B example 111110 · 6 attrs user data from t_hoff id · status · payload…

index → LP[1]→old tuple · t_ctid→new tuple on same page

8,192 bytes · one slotted page

### The page fills from both ends

The 24-byte header and 4-byte line pointers advance from byte 0. Tuple bodies are allocated backward from byte 8192. The untouched interval between pd_lower and pd_upper is free space.

The long strip is byte-scaled. The larger cards below it are readable controls, not a second scale.

Follow it to the source

Documentation

[PostgreSQL manual · Database Page Layout](https://www.postgresql.org/docs/current/storage-page-layout.html)

PostgreSQL source

[bufpage.h · PageHeaderData](https://github.com/postgres/postgres/blob/master/src/include/storage/bufpage.h)[bufpage.c · page operations](https://github.com/postgres/postgres/blob/master/src/backend/storage/page/bufpage.c)

Suzuki

[Suzuki · Chapter 1 §1.3, “Heap Table Structure”](https://www.interdb.jp/pg/pgsql01/03.html)

Rogov · text only

Rogov, PostgreSQL 14 Internals · Part I · Chapter 3, “Pages and Tuples”

physical cluster storage
### The data directory, opened

Select any entry to learn what owns it and follow the documentation and source.

heap pages**11.0k**

modeled heap bytes**85.8 MiB**

WAL segments**3**

TERMINOLOGY
**Data directory** names the storage structure. `PGDATA` names an environment variable. Configuration can be elsewhere, so the two are not synonyms.

postgres@cluster/data/directory focused map · illustrative OIDs

●▣data directory/cluster storage root├·PG_VERSION├▣base/└▣16384/database OID · illustrative└▤12345 main fork · filenode└▤12345.1 · 12345.2 1 GiB segments└▤12345_fsm free space map└▤12345_vm visibility map├▣global/├▣pg_wal/├▣pg_xact/├▣pg_multixact/├▣pg_subtrans/├↗pg_tblspc/├▣pg_stat/├▣pg_stat_tmp/├▣pg_logical/├▣pg_replslot/├▣pg_twophase/├·postgresql.conf traditional location├·pg_hba.conf traditional location├·postmaster.pid while server runs

≠

#### OID is identity; filenode is a current physical name

A rewrite can keep relation OID `18740` while changing `relfilenode` from `18740` to `18812`. Ask `pg_relation_filepath()`; do not infer paths from OIDs.

one database cluster · physical storage root

### The data directory

This directory holds the cluster’s durable state. PGDATA is an environment variable used to help locate a cluster; it is not the name of the structure. Configuration files may be elsewhere, and the data_directory setting can select a different storage location.

This is a focused map of the requested entries. A current cluster also contains other state directories and files documented by the server version.

Follow it to the source

Documentation

[PostgreSQL manual · Database File Layout](https://www.postgresql.org/docs/current/storage-file-layout.html)

PostgreSQL source

[relpath.h · database, tablespace and fork paths](https://github.com/postgres/postgres/blob/master/src/include/common/relpath.h)[md.c · relation files and segments](https://github.com/postgres/postgres/blob/master/src/backend/storage/smgr/md.c)

Suzuki

[Suzuki · Chapter 1 §1.2, “Physical Structure of Database Cluster”](https://www.interdb.jp/pg/pgsql01/02.html)

Rogov · text only

Rogov, PostgreSQL 14 Internals · Introduction · “Data Organization” (Files and Forks)

## Metadata
- **Source**: [Original Article](https://nikolays.github.io/PGSimCity/)
