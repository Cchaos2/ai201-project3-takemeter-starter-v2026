# Acceptance criteria — TakeMeter

Five criteria that say what "working" means for this classifier, written in
unit 5 **before** anything was trained.

**All five are yours this time.** None are given. You've had two projects of
practice.

An acceptance criterion names a number. *"The model is accurate"* is an
opinion. *"Every label has an F1 of at least 0.60 on the held-out set"* is a
criterion.

Under each, write a sentence or two on **why that number**. A reason that says
something about your data or your taxonomy earns credit — *"I picked 0.60 F1
for `reaction` because it's my smallest label and I only have about 50
examples of it"*. A reason that could be attached to any project does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

Not numbers that sound impressive. Three labels means a coin-flip guesser gets
about 33%, so a target of 0.40 is barely a target. Your number should sit
somewhere you'd honestly call useful.

**Cover at least three of these five areas.** They're here as prompts, not as a
form to fill in — a criterion that fits none of them is fine if it names a
number.

| Area | A question it could answer |
|---|---|
| Overall accuracy | How often does it need to be right to be worth using? |
| Per-label performance | Is one label allowed to be much worse than the others? |
| Balance | How lopsided can your label counts get before it's a problem? |
| Consistency | If someone else labelled the same posts, how often should you agree? |
| Confidence | Should a confident prediction be right more often than an unsure one? |

Two things worth knowing before you pick numbers, because both will affect
whether you hit them:

- **Your smallest label will have the jumpiest score.** If a label has 50
  examples, about 8 land in the test split. An F1 computed on 8 examples moves
  a lot between seeds. A target for that label should be looser than one for
  your biggest label, and saying so is a good reason.
- **Unit 6 tests across three seeds, and the target has to hold across all
  three.** A target of 0.65 against results of 0.71, 0.62, 0.68 is a **miss**.
  Pick with that in mind — it is stricter than it first sounds.

---

## 1. Overall accuracy of at least 0.65 on the held-out test split, on every one of the three seeds (42, 7, 2024).


<!-- Your criterion. It must name a number. -->



**Why this target:**
Two floors to beat: random guessing on 3 labels is ~33%,
and always predicting my biggest label (`claim`, 86/200 = 43%) is 43%.
Anything under 0.43 means the model learned nothing beyond the label counts.
0.65 is 22 points above the majority floor. The test split is only 30 posts,
so one post is 3.3 points, the target has to hold on all three seeds, not
just a friendly draw.



---

## 2. Every label has an F1 of at least 0.55 on the held-out test split, on every seed.

<!-- Your criterion. -->



**Why this target:**
`banter` is my smallest label (50/200 = 25%), so about
7–8 of them land in the test split and one or two misses move its F1 by 10+
points. A floor of 0.55 is deliberately below the accuracy target because it
has to hold for the thinnest label across three draws. It still rules out a
model that scores well overall by ignoring `banter`.


---

## 3. At most 30% of true `analysis` posts in the test split are predicted as `claim`, on every seed.

<!-- Your criterion. -->



**Why this target:**
`claim` vs `analysis` is my hardest boundary, the only
difference is whether a checkable specific is present and load-bearing, and it
produced 6 of my 7 hard cases. This is read straight off the confusion matrix
(row `analysis`, column `claim`, divided by the `analysis` row total). With
~10 `analysis` posts in test, 30% means 3 posts; a model that pushes 4 or more
into `claim` has not learned the boundary the taxonomy is built on.


---

## 4. Agreement with the staff labels on the 30-post staff set is at least 70% (21 of 30), measured by `agreement.py`.

<!-- Your criterion. -->



**Why this target:**
If I can't apply somebody else's written rule the way
its authors did, my own 200 labels probably aren't consistent either, and the
model's ceiling is my labelling, not its capacity. The staff set deliberately
includes ambiguous posts, so 100% is not realistic; 70% is the point where
most disagreements should be arguable from the definitions rather than
careless.


---

## 5. Accuracy on the most-confident third of test predictions exceeds accuracy on the least-confident third by at least 0.20, on every seed.

<!-- Your criterion. -->



**Why this target:**
`results.json` records `accuracy_most_confident_third`
and `accuracy_least_confident_third`. If the model's softmax confidence means
anything, its sure guesses should be right more often than its unsure ones. A
model that is 95% confident and wrong is worse to use than one that says it
isn't sure. Each third is ~10 posts, so 0.20 is two posts of separation, 
enough to be real, not just noise from one row.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 6 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Every label performs acceptably

         The model performs well on all labels.

         **Why this target:** ...

         > **Revised in unit 6:** Every label has an F1 of at least 0.60 on
         > the held-out set.
         >
         > **Why revised:** "performs well" gave me nothing to check. I
         > couldn't produce a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "Overall accuracy of at least 0.65" → "at least 0.55", because
            0.65 turned out to be optimistic for 200 examples.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
