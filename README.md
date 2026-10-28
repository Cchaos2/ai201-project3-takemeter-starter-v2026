# TakeMeter

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, the
> notebook, the baseline, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> head -5 data/practice_labels.csv     # the shape your labels.csv needs
> ```
>
> Then open `takemeter.ipynb` **in this folder** — in VS Code, or with
> `jupyter notebook` if you prefer. Pick the kernel: the `.venv` inside this
> project. Run section 1, which reports the hardware you'll be training on.
> Everything else waits until you have data.
>
> Nothing to upload, nothing to connect, no accounts and no keys. The notebook
> runs on your machine and writes next to your code.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     Unit 5 asks for the first five sections. Unit 6 adds the five below them.

     Everything is pasted as TEXT. No screenshots, no images.

     ⚠️ The confusion matrix especially. The notebook prints one as a markdown
     table, ready to copy. A screenshot of a matrix earns nothing. Paste the
     table.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 5 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- Your community, and what your classifier sorts posts into. Three or four
     sentences. -->
TakeMeter sorts comments from r/chess, collected from the threads about the
2022 Carlsen–Niemann cheating controversy. It classifies each comment into one
of three labels: `analysis` (a sincere point backed by something a reader can
check — a number, a date, a named source, a link, or chess moves), `claim`
(a sincere point with no checkable support), or `banter` (jokes, sarcasm and
parody that aren't arguing a point at all). 


---

## Label Taxonomy

<!-- Each label: a one-sentence definition and two real examples from your
     reading. Then your decision rule for the hardest boundary.

     The decision rule is worth a point on its own and it's the thing most
     people leave out. Every taxonomy has a hardest boundary. Name yours. -->

Three labels. Two questions decide every post, in this order:
(1) Is the author sincere? If not → `banter`.
(2) If sincere, does the post back its point with something a reader could
check? Yes → `analysis`. No → `claim`.

### `analysis`

**Definition:** A sincere post that backs its point with at least one
checkable specific: a number, a date, a named source or quote, a link to
evidence, or concrete chess moves.

**Example 1:**
> As the best researchers can tell, and in my own experience as an FBI Special Agent (now retired), detecting deception is very difficult. Every study conducted since 1986, when the famed researcher Paul Ekman first wrote about this, has demonstrated that we humans are no better than chance at detecting deception (Ekman & O'Sullivan 1991, 913-920; Granhag & Strömwall, 2004, 169; Mann & Vrij 2004). That means that if you toss a coin in the air you will be as likely to detect deception as the truth. And while it is true that a very few people are better at detecting deception than others, they are barely above chance. In fact, those that are really good are only correct somewhere around 60% of the time; that means that 40% of the time they are wrong and you would not like them sitting on a jury judging you." Joe Navarro
 "Most people think that they are really good at detecting deception, especially with a loved one (a spouse or boyfriend or girlfriend).  Again, the exact opposite is more likely to be true (see Levine & McCornack; McCornack & Parks; DePaulo; Charlton; Cooper; Lindsay; and Muhlenbruck)." "If you are confident that you can catch a lover lying, that is a good sign that you are probably not very good at it " https://www.truthaboutdeception.com/site-info-and-resources/sources-and-references.htmlme talking now let's just keep this in mind when using his interview cues to damn him or anyone for that matter of tv interviews or whatever we SUCK AT THIS

**Example 2:**
> No. The position after move 5 is the main line Romanishan variation of the Nimzo-Indian. The standard continuation is 6. Nf3 dxc4 7. a3 Bxc3 8. bxc3 c5 which is the same position reached in the game vs Hans, just a different move order.


### `claim`

**Definition:** A sincere post that makes a point — an opinion, accusation,
prediction or defence, with no checkable support offered; it may be right,
but nothing in the post lets a reader verify it.

**Example 1:**
> Highly suspicious. No real proof, but its hard to think how all of this could happen without him cheating.


**Example 2:**
> Seems to be a play for media attention tbh. Chess has never had the attention that its players feel it deserves.


### `banter`

**Definition:** A post whose main purpose is to be funny (a joke, sarcasm,
parody, pun or meme) rather than to sincerely argue a point, even if it
mentions real facts.

**Example 1:**
> A Bishop, a White Knight and a GM walk into a bar. The bartender asks, "Is this some kind of joke?"

**Example 2:**
> chess.com should add a Hans bot and just have it be stockfish

### The hardest boundary

**Which two labels:** `claim` vs `analysis`.

The borderline post:
> Has anyone ever thought that Magnus dropped out because he freaking lost his match in 52 traditional games? He was embarrassed and rage quit?

It reads like a hot opinion, but "52 traditional games" is a specific number
the point leans on. Posts like this came up constantly: numbers that are
estimates ("<10%"), personal anecdotes ("like 6 youth players"), or links
that point at the thing being judged rather than at evidence.

**The decision rule I used every time:**
<!-- e.g. "If the post names a specific checkable fact, it's `analysis`, even
     if the tone is heated." -->
A post is `analysis` only if it contains a specific that a reader could go
and check (a count, a date, a rating, a named person's statement, a link to
evidence, or actual moves) and the point depends on it. Tone does not
matter: a heated or rude post with a checkable number is still `analysis`.
Numbers that are the author's own estimate or anecdote ("I think at least
3 of them", "<10% chance") are not checkable, so the post is `claim`.
The number may turn out to be wrong; what matters is that it can be checked.
And the sincerity test always runs first, real statistics inside a parody
make the post `banter`, not `analysis`.


---

## The Dataset

<!-- Where you collected from, how you labelled, your counts, and three hard
     cases. -->

**Where the posts came from:**
r/chess, a public subreddit. All 200 rows are
comments copied by hand from several threads about the 2022 Carlsen–Niemann
cheating controversy. Whole comments, not trimmed. One file, not split.

**How I labelled them:** <!-- Cold first? Pre-labelled with AI and corrected?
Say so plainly — the disclosure is required, not penalised. -->
I labelled 20 comments cold first, no tools, just
my three definitions and the decision rule, and marked them `cold` in the
note column. I then gave Claude my definitions and decision rule and had it
pre-label the remaining 180 in batches. I read every one of those 180 and
corrected the ones I disagreed with; those rows are marked
`prelabeled-AI (Claude), reviewed by me`. Seven rows that made me pause are
marked `hard case` in the note column with which two labels it could have
been and what I decided.

**Counts per label:**

| Label | Count | Share |
|---|---|---|
| `claim` | 86 | 43% |
| `analysis` | 64 | 32% |
| `banter` | 50 | 25% |
| **Total** | 200 | 100% |

No label is above the 70% cap. `banter` is the thinnest label, so it will
have only ~7–8 examples in the test split.

**Three hard cases**

<!-- Any post that made you pause: what it was, which two labels it could have
     been, and what you chose. These are worth more than the easy 190. -->

**1.**
> *The post:* "Has anyone ever thought that Magnus dropped out because he freaking lost his match in 52 traditional games? He was embarrassed and rage quit?"
>
> *Could have been:* `claim` or `analysis`. It reads like a hot opinion with a rhetorical question.
>
> *I chose, because:* `analysis`. "52 traditional games" is a specific, checkable number and the point leans on it. By my decision rule, tone doesn't matter — a checkable specific the argument depends on makes it `analysis`.

**2.**
> *The post:* "holy shit guys this conspiracy goes all the way to the top / GM Daniel Naroditsky (!!!) / 2019 US Masters Chess Championship (Live Broadcast): 2723 TPR / 6th Annual Washington International (No Live Broadcast): 2521 TPR / and just look at this photo […] clearly frustrated that he doesn't have his engine assistance?? / (i have nothing against any of these players, just presenting objective facts that cannot be interpreted any other way)"
>
> *Could have been:* `analysis` or `banter`. It contains real, checkable tournament performance ratings and a link.
>
> *I chose, because:* `banter`. The sincerity test runs first. The whole post is a parody of the "look at his TPR" accusations — the numbers are real but they're used to mock the argument, not make it.

**3.**
> *The post:* "It's almost as if the world wasn't locked down for 18 months and these kids had nothing to do but study chess and there were no tournaments to update their progress. What's more plausible... all these kids are cheating or lockdowns and lack of tournaments negatively skewed the progress for a lot players?"
>
> *Could have been:* `banter` or `claim`. The opener "It's almost as if…" is sarcastic.
>
> *I chose, because:* `claim`. The sarcasm is only the delivery; the author sincerely means the point (lockdowns explain the rating jumps). "18 months" is roughly right but not a specific the argument depends on, so it isn't `analysis` either.

---

## The Training Run

<!-- Your starting model, your settings, and anything you changed and why. -->

**Base model:** `distilbert-base-uncased`

**Settings:** <!-- epochs, learning rate, batch size, seed -->
3 epochs, learning rate 2e-5, batch size 16, max_length 128,
seed 42. Device: `mps` (Apple Silicon GPU), torch 2.14.1.

**Anything I changed from the defaults, and why:**
Nothing. I kept the
notebook defaults so the Unit 6 comparison across seeds starts from the
standard configuration.

**Split sizes:** <!-- train / val / test, and per-label counts in the test
split. If a label had fewer than about 8 in test, say so — it explains a lot
of next unit's variance. -->
train 139 / val 31 / test 30. Per-label in test:
`claim` 13, `analysis` 10, `banter` 7. The notebook flagged that `banter`
has only 7 test examples, so its F1 will move a lot between seeds — one
missed post is ~14 points.

---

## How I Used AI

<!-- Two specific moments — what you asked, what came back, what you changed.

     ⚠️ Plus disclosure of any pre-labelling. If you had a model pre-label a
     batch and then read and corrected every one, say that. It's an allowed
     workflow and disclosing it costs you nothing. Not disclosing it is the
     problem. -->

**Moment 1**: pre-labelling the batch

- *What I asked for:* I gave Claude my three definitions, the decision rule
  for `claim` vs `analysis`, and the 180 comments I had not labelled cold, in
  batches, and asked for one label per comment plus a one-line reason.
- *What came back:* Labels for every comment. Most matched what I would
  have chosen.
- *What I changed:* I read every one of the 180 and corrected the ones that
  broke my rule, numbers that aren't checkable went back to `claim`, and the
  parody went to `banter` because the sincerity test runs first. The ones
  that made me pause became my hard cases, and the pattern of its mistakes
  is what made me add "the number has to be checkable, not an estimate" to
  the decision rule.

**Moment 2**: understanding the first training run

- *What I asked for:* After section 5 printed accuracy 0.500, macro F1
  0.322 and `banter` F1 0.000, I pasted the per-epoch loss table and the
  results and asked whether something was wrong with my setup.
- *What came back:* That nothing was broken. The progress bar showed 27/27
  steps, 139 training rows at batch size 16 over 3 epochs is only 27
  gradient updates, and the final training loss of 1.006 and validation
  loss of 1.025 are barely below ln(3) ≈ 1.10, the loss of random guessing
  on three labels. The model had learned to predict the majority label
  (`claim`, F1 0.63) and never predicted `banter` once. 
- *What I changed:* Nothing in the notebook — my criteria were already
  filed and retraining after seeing the test numbers is the thing the course
  warns against.

**Pre-labelling disclosure:**
20 of the 200 rows were labelled by me alone,
with no tools, before any AI was involved; they are marked `cold` in the
`note` column. The remaining 180 were pre-labelled by Claude from my
definitions and decision rule, then read and corrected one by one by me;
they are marked `prelabeled-AI (Claude), reviewed by me`.

<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

Baseline: `facebook/bart-large-mnli`, zero-shot, using the definitions in
`label_definitions.txt`. 

Trained: my fine-tuned `distilbert-base-uncased` from
unit 5 (seed 42, `results.json`). Both scored on the same 30 held-out posts in
`test_split.csv` (13 `claim`, 10 `analysis`, 7 `banter`).

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy | 0.367 | 0.500 | +0.133 |
| Macro F1 | 0.358 | 0.322 | -0.035 |
| F1 — `analysis` | 0.421 | 0.333 | -0.088 |
| F1 — `banter` | 0.417 | 0.000 | -0.417 |
| F1 — `claim` | 0.235 | 0.634 | +0.399 |

**What I predicted before I looked:**
<!-- Milestone 1 asks you to write this BEFORE seeing the trained numbers. A
     prediction made afterwards isn't one. -->
I predict the trained model will beat the baseline only on claim, because it predicts
claim for almost everything, and that the baseline will beat it on banter, since the 
trained model never predicted banter once.

**Definitions vs. bare label names:** With my definitions the baseline scored
0.367 accuracy and 0.358 macro F1; with bare label names only it scored 0.467
accuracy and 0.326 macro F1. So my definitions cost 0.100 of accuracy but added
0.032 of macro F1, and the difference is almost all `banter`: 0.417 F1 with
definitions, 0.000 without. With bare names the baseline behaves like my
trained model, leaning on `claim` (F1 0.579) and never getting a `banter` post
right; the definitions are what made it use all three labels. I report the
definitions run as my baseline in the table above, because that is the fair
opponent the brief describes, and its result is in `baseline_results.json`. The
bare-names run is in `baseline_bare_results.json`.

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->
My prediction was mostly right: the trained model beats the baseline on `claim`
(+0.399) and loses badly on `banter` (-0.417). What I didn't predict is that the
baseline also beats it on `analysis` (-0.088), and that the trained model's
`claim` advantage is big enough to win on overall accuracy (+0.133) while still
losing on macro F1 (-0.035). That accuracy win is not evidence that fine-tuning
taught it my taxonomy. The trained model predicted `claim` for 28 of 30 posts,
so it catches all 13 real `claim` posts while scoring 0.000 on `banter` and
0.333 on `analysis`. Always guessing `claim` would score 0.433 on this split, so
the trained model is only 2 posts better than a majority-class guesser. The
baseline is worse overall (0.367, below that majority floor and barely above
the 0.33 of random guessing), but it is the only one of the two that uses all
three labels. Neither model has learned the distinctions my taxonomy draws:
fine-tuning on 139 posts for 27 gradient steps mostly learned the label counts,
not the labels. 


---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

**Device:** `mps` (Apple Silicon GPU), torch 2.14.1. All three seeds were run
on this machine in one execution of section 6. Settings unchanged from unit 5:
`distilbert-base-uncased`, 3 epochs, lr 2e-5, batch 16, max_length 128.
Every test split has 30 posts: 13 `claim`, 10 `analysis`, 7 `banter`.

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1. Overall accuracy | ≥ 0.65 on every seed | 0.500 | 0.433 | 0.433 | MISSED |
| 2. Every label F1 (lowest label shown) | ≥ 0.55 on every seed | 0.000 (`banter`) | 0.000 (`analysis`, `banter`) | 0.000 (`analysis`, `banter`) | MISSED |
| 3. True `analysis` predicted as `claim` | ≤ 30% on every seed | 80% (8/10) | 100% (10/10) | 100% (10/10) | MISSED |
| 4. Agreement with staff labels | ≥ 70% (21/30) | pending (Milestone 3) | — | — | pending |
| 5. Most-confident third minus least-confident third (accuracy) | ≥ +0.20 on every seed | +0.400 (0.800 vs 0.400) | +0.500 (0.700 vs 0.200) | +0.600 (0.700 vs 0.100) | MET |

**Spread across seeds** (from section 6):

| Measure | Seed 42 | Seed 7 | Seed 2024 | Spread |
|---|---|---|---|---|
| Overall accuracy | 0.500 | 0.433 | 0.433 | 0.067 |
| Macro F1 | 0.322 | 0.202 | 0.202 | 0.121 |
| F1 — `analysis` | 0.333 | 0.000 | 0.000 | 0.333 |
| F1 — `claim` | 0.634 | 0.605 | 0.605 | 0.029 |
| F1 — `banter` | 0.000 | 0.000 | 0.000 | 0.000 |

Accuracy moved only 0.067 across seeds, under the 10-point instability line,
but that stability is not a sign the measure is trustworthy. On seeds 7 and
2024 the model predicted `claim` for all 30 posts, and every split has exactly
13 `claim` posts, so both score exactly 13/30 = 0.433. The numbers are stable
because the model is doing the same trivial thing on every split. Seed 42 is
the only run where it predicted anything other than `claim` (2 `analysis`
posts, both correct).

### Confusion matrix

<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.
     An image of a matrix earns nothing. -->

Seed 42 (the matrix section 7 prints):

| true \ predicted | analysis | claim | banter |
|---|---|---|---|
| **analysis** | 2 | 8 | 0 |
| **claim** | 0 | 13 | 0 |
| **banter** | 0 | 7 | 0 |

Seed 7:

| true \ predicted | analysis | claim | banter |
|---|---|---|---|
| **analysis** | 0 | 10 | 0 |
| **claim** | 0 | 13 | 0 |
| **banter** | 0 | 7 | 0 |

Seed 2024:

| true \ predicted | analysis | claim | banter |
|---|---|---|---|
| **analysis** | 0 | 10 | 0 |
| **claim** | 0 | 13 | 0 |
| **banter** | 0 | 7 | 0 |

**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->

8 real `analysis` posts were called `claim` on seed 42 (10 of 10 on the other
two seeds) and 0 went the other way, so the model never learned the
`analysis`/`claim` boundary my taxonomy is built on: it treats "no checkable
specific" as the default for everything, and all 7 `banter` posts also fall
into `claim` on every seed.


---

## Verdicts and Diagnoses

<!-- MET or MISSED against LAST UNIT's target. The target has to hold across
     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

**Diagnoses**

<!-- For each miss: the cause, and how you know. The four common causes are:
     too few examples for a label, a boundary you applied inconsistently, a
     genuinely hard label pair, and a task the model can't reach from this
     much data.

     ⚠️ Use your agreement report as evidence. It is the only instrument you
     have that can tell a LABELLING problem from a MODEL problem, and this
     section is graded on whether you used it that way. -->



---

## Agreement Report

<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in
     data/staff_taxonomy.md, not your own — so every argument below is made
     from those definitions and those decision rules. -->

**Agreement rate:** ___ / 30 = ___%

<!-- Nobody grades this number. A 60% who argues every disagreement from the
     stated rules beats a 95% who wrote "staff was right" nine times. Several
     of the 30 were chosen because they're genuinely ambiguous — you should be
     winning some of these. -->

**Disagreements**

<!-- Three lines each: the post, both labels, and who you think is right and
     why — grounded in the staff definitions you were both applying.

     Then sort each into one of three piles:
       (a) the rule covered it and I applied it loosely → a consistency problem
       (b) the rule genuinely doesn't say               → a gap in the definitions
       (c) the rule is ambiguous here and my reading is defensible → argue it.
           This is a legitimate win.

     Pile (a) is the one that matters most for your diagnosis: if you applied a
     written rule two different ways on 30 posts, that is direct evidence about
     what you did across your own 200. -->

**1.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**2.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**What the pattern in my disagreements tells me:**



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Did it help, and how do I know:**

<!-- If it didn't, say so. Relabelling that didn't help is a genuinely
     interesting result and earns full credit. -->



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped. -->



**The gap between what I meant my labels to capture and what the model
learned:**
<!-- Two sentences. Your confusion matrix is the evidence. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 5

       [ ] criteria.md has five numbered criteria, each naming a NUMBER
       [ ] Each has a reason underneath tied to your data or taxonomy
       [ ] labels.csv: at least 150 rows, text/label/note, ONE file not split
       [ ] No label above 70%
       [ ] All five unit 5 sections have real content
       [ ] Label Taxonomy includes the decision rule for your hardest boundary
       [ ] The Dataset includes three hard cases
       [ ] results.json and test_split.csv committed (the notebook does this)
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 6

       [ ] Baseline vs. Trained table, with your prediction written beforehand
       [ ] Run Log — Before, five criteria across three seeds
       [ ] Confusion matrix TYPED AS A MARKDOWN TABLE
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, using the agreement report as evidence
       [ ] Agreement Report with every disagreement adjudicated
       [ ] One improvement, with Run Log — After
       [ ] What's Still Broken
       [ ] results_three_seeds_before.json, results_three_seeds_after.json,
           baseline_results.json and
           agreement_results.json committed
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
