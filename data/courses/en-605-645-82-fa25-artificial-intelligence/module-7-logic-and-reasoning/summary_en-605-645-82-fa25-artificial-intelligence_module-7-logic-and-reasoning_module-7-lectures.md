# Summary for EN.605.645.82.FA25 Artificial Intelligence – Module 7: Logic and Reasoning – Module 7 - Lectures

## https://jh.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=9fbe707f-da1f-44cb-b73c-b0c1017767ce

# Summary — Propositional Logic (Lecture)

## Context
- Logic complements state-space search by providing formal ways to represent and reason about knowledge (states, sentences, goals, models).

## Syntax of propositional logic
- Constants: T (true), F (false).
- Propositional symbols: P, Q, R, ...
- Sentence-formation rules: if P is a sentence then:
  - (P) is a sentence
  - ¬P is a sentence
  - P ∨ Q is a sentence
  - from these, ∧, → (implication), ↔ (equivalence) are defined or introduced as derived operators

## Semantics
- Assign T/F to propositional symbols; this assignment is a model (a possible world).
- Truth of complex sentences determined compositionally from symbol assignments (truth tables).

## Truth tables / models (for two symbols P,Q)
- All possible models: (P,Q) = (T,T), (T,F), (F,T), (F,F).
- Example evaluations:
  - ¬P: flips P in each model.
  - P ∨ Q: true if P or Q (or both) true.
  - P ∧ Q: true only when both P and Q true.
  - P ∨ ¬P: true in every model → valid (tautology).
  - P ∧ ¬P: false in every model → unsatisfiable (contradiction).

## Key semantic categories
- Satisfiable: a sentence true in at least one model.
- Valid (tautology): true in every model.
- Unsatisfiable (contradiction): true in no model.

## Material implication and equivalence
- Material conditional P → Q: truth table yields false only when P = T and Q = F (implication is not causation).
- Equivalence P ↔ Q: true when P → Q and Q → P both hold.

## Useful logical laws and inference rules
- De Morgan: ¬(P ∧ Q) ≡ ¬P ∨ ¬Q (and dual).
- Modus ponens: from P → Q and P, infer Q.
- Modus tollens: from P → Q and ¬Q, infer ¬P.
- Unit resolution: from (P ∨ Q) and ¬Q, infer P.
- Resolution (binary): from (P ∨ Q) and (¬Q ∨ R), infer (P ∨ R).

## Notes
- A small set of connectives (e.g., ¬ and ∨ with parentheses) is sufficient to express all propositional formulas.
- Inference rules can be checked/proved with truth tables by examining all models.

## https://jh.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=509be047-be0d-4868-9993-b0cc008732a0

# Summary

- Domain: a grid “Wumpus”-style world with pits, a single Wumpus, gold, walls, and one arrow. Percepts in a cell:
  - Stench (S): Wumpus in a neighboring cell.
  - Breeze (B): pit in a neighboring cell.
  - Glitter: gold in the cell.
  - Bump: hit a wall.
  - Scream: Wumpus killed.

- Setup and initial facts:
  - Agent starts at cell (1,1) with all percepts false.
  - From no-stench and no-breeze at (1,1) the neighboring cells (2,1) and (1,2) are known safe.

- Notation:
  - Cij = cell at row i, column j.
  - Sij true ⇔ Cij has a stench.
  - Bij true ⇔ Cij has a breeze.
  - Wij true ⇔ Cij has the Wumpus.
  - Knowledge base (KB) = set of logical implications relating percepts to hazard locations.

- Example logical rules encoded in the KB (propositional form):
  - If ¬S11 then ¬W11 ∧ ¬W21 ∧ ¬W12.
  - If ¬S12 then ¬W11 ∧ ¬W12 ∧ ¬W22 ∧ ¬W13.
  - If S12 then W11 ∨ W12 ∨ W22 ∨ W13 (Wumpus is in one of the neighbors).
  - If ¬Sij then ¬Wij and ¬W(i-1)j and ¬W(i+1)j and ¬Wi(j-1) and ¬Wi(j+1) (ignoring walls).
  - If Sij then Wij ∨ W(i-1)j ∨ W(i+1)j ∨ Wi(j-1) ∨ Wi(j+1).

- Inference steps and rules used:
  - Modus ponens: from (P → Q) and P derive Q.
  - And-elimination: from (A ∧ B ∧ ...) derive individual conjuncts.
  - Resolution: use disjunctions and negated literals to eliminate possibilities (e.g., from (P ∨ Q) and ¬Q derive P).
  - Application:
    - From ¬S11 and rules, derive ¬W11, ¬W21, ¬W12.
    - Moving to (2,1) with a breeze yields Bij, so a pit is in (3,1) or (2,2).
    - Moving to (1,2) with a stench yields S12, so the Wumpus must be in one of the neighbors; using previously derived ¬Wij facts and resolution eliminates alternatives and yields the Wumpus location (conclusion: Wumpus at (1,3) in the toy example).

- Observations about representation:
  - Propositional logic is powerful but cumbersome: it requires enumerating every propositional atom (no variables, no functions/relations).
  - More compact, general rules would use indices/variables (e.g., ¬Sij → ¬Wij ∧ ¬W(i-1)j ∧ ¬W(i+1)j ∧ ¬Wi(j-1) ∧ ¬Wi(j+1)).
  - The transcript closes by posing the question of whether such generalizations (variables and quantified rules) can be used to make the representation more compact and convenient.

## https://jh.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=2078e79d-1643-4987-a699-b0c6011d6834

# First-order logic (predicate calculus) — concise summary

- Purpose: Extends propositional logic with constants, functions, variables and quantifiers to allow compact, structured reasoning.

- Syntax elements
  - Constants: named objects (e.g., John).
  - Functions: map objects to objects (e.g., LeftLeg(John)). Functions do NOT return truth values.
  - Predicates: special functions returning true/false (e.g., Brother(x,y), Parent(John,Sam)).
  - Variables: x, y, ...
  - Connectives: ¬, ∧, ∨, →, ↔ (as in propositional logic).
  - Quantifiers: ∀ (for all), ∃ (there exists).
  - Equality: available as usual.

- Examples
  - Parent(John,Sam) ∧ Male(John) → Father(John,Sam).
  - HasLeftFoot(John) → HasLeftLeg(John) (use predicates to state properties).

- Quantifier semantics and issues
  - ∀x P(x): P(x) true for every relevant instantiation of x — behaves like a big conjunction (and).
  - ∃x P(x): P(x) true for at least one instantiation — behaves like a big disjunction (or).
  - Universe of discourse / typing matters: need to restrict x (e.g., Person(x) → Loves(x,Raymond)) to avoid unintended meanings.
  - Scope matters: ∀x (AtJHU(x) → Smart(x)) = everyone at JHU is smart; ∀x (AtJHU(x) ∧ Smart(x)) = everyone is at JHU and smart (different).
  - Order of same quantifiers is interchangeable: ∀x ∀y ... = ∀y ∀x (similarly for ∃).
  - Mixed quantifiers are order-sensitive:
    - ∃x ∀y Loves(x,y): there exists someone who loves everyone.
    - ∀y ∃x Loves(x,y): for each person y there exists someone who loves y (different).

- Quantifier duality
  - ∀x P(x) ≡ ¬∃x ¬P(x)
  - ∃x P(x) ≡ ¬∀x ¬P(x)

- Inference with quantifiers
  - Most propositional inference carries over, but quantifiers require instantiation rules:
    - Universal elimination (instantiation): From ∀x P(x) infer P(c) for any appropriate constant c.
    - Existential elimination: From ∃x P(x) infer P(c) for some fresh constant c not used elsewhere (a Skolem constant).
  - These instantiation steps are essential for applying propositional-style inference in first-order proofs.

## https://jh.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=d3bc6ed9-98c8-43e5-823f-b0c800cbb51a

# Summary

## First-order logic representation
- Natural-language facts and rules are converted into predicates and quantified implications.  
  Example:
  - Buffalo(Bob), Pig(Pat)
  - ∀x,y (Buffalo(x) ∧ Pig(y) ⇒ Faster(x,y))
- Inference uses standard logical rules (universal elimination, modus ponens, and-introduction/elimination).
- Substitution assigns constants to variables (e.g., x := Bob, y := Pat) to instantiate rules.

## Inference as search
- Proving a goal from a knowledge base is a state-space search: apply rules to produce new facts until goal is derived (or disproved).
- Two systematic strategies: forward chaining and backward chaining.

## Forward chaining (data-driven)
- Match left-hand sides (LHS) of implications against known facts to derive new facts; repeat until goal reached.
- Example setup:
  - Facts: Buffalo(Bob), Pig(Pat), Slug(Steve)
  - Rules:
    1. ∀x,y (Buffalo(x) ∧ Pig(y) ⇒ Faster(x,y))
    2. ∀y,z (Pig(y) ∧ Slug(z) ⇒ Faster(y,z))
    3. ∀x,y,z (Faster(x,y) ∧ Faster(y,z) ⇒ Faster(x,z))
- Derivation:
  - From 1 + facts → Faster(Bob,Pat)
  - From 2 + facts → Faster(Pat,Steve)
  - From 3 + those facts → Faster(Bob,Steve)
- Note: variables in different sentences are distinct (need renaming/instantiation).

## Backward chaining (goal-driven)
- Start from a goal (RHS of an implication), match it to rule consequents to generate subgoals (new LHS facts to prove), recurse until ground facts are reached.
- Example goal: Faster(Bob,Steve)
  - Instantiate rule 3 with x=Bob, z=Steve → subgoals: Faster(Bob,y) and Faster(y,Steve)
  - Prove Faster(Bob,y) via rule 1 with y=Pat → requires Buffalo(Bob), Pig(Pat) (both facts)
  - Prove Faster(y,Steve) via rule 2 with y=Pat → requires Pig(Pat), Slug(Steve) (both facts)
  - Goal proven once subgoals are all satisfied.

## Search characteristics and issues
- Backtracking occurs when alternative instantiations lead to contradictions or dead ends.
- Backward chaining behaves like depth-first search, building proofs piecewise.
- Both approaches can suffer combinatorial explosion due to many possible instantiations and rule applications—significant scalability concern (relevant for planning and agent design).

## https://jh.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=a30a1a5f-76f6-4b34-b51e-b0cb0014a337

- Definition: Unification finds a substitution Θ (possibly empty) that makes two terms/sentences identical. Failure can be indicated by null; an empty substitution means no change was needed.

- Basic rules:
  - Constants/identical symbols unify directly.
  - Functions unify only if they have the same function symbol and arity, and their arguments unify recursively.
  - Variables can be assigned (substituted) with constants, other variables, or terms (including functions), subject to the occurs-check (a variable cannot be assigned a term that contains that same variable).
  - Before unification, rename variables to be unique across sentences ("standardize apart") so identically named variables in different sentences are treated as distinct.

- Examples:
  - Unify P(a, X) and P(a, B) → Θ = {X/B}.
  - Unify P(a, X) and P(Y, B) → Θ = {Y/a, X/B}.
  - Unify P(a, X) and P(Y, f(Y)):
    - Standardize if needed, then set Y = a, then X = f(a) → Θ = {Y/a, X/f(a)}. This shows variables can be bound to function terms.
  - Variable name collision resolved by standardizing apart:
    - P(a, X) and P(X, B) (same name X used twice) → rename to P(a, X1) and P(X2, B) then unify → Θ = {X1/B, X2/a}.

- Failure cases:
  - Contradictory assignments: P(a, B) and P(X, X) would require X = a and X = B simultaneously → failure.
  - Occurs-check or structure mismatch: a variable cannot be assigned a term that contains itself (e.g., X = f(X) fails); a constant cannot unify with a function term that has no variables to absorb the mismatch.

- Practical unification procedure (high level):
  1. Standardize variables apart.
  2. Recursively match terms: if both are identical symbols succeed; if one is a variable, try to bind it (respect occurs-check); if both are functions, check same symbol/arity and unify argument lists.
  3. Combine substitutions; if a contradiction or occurs-check failure arises return failure.

## https://jh.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=b773f86b-5c0e-4e58-9735-b0c1013ca025

# Summary — Resolution and CNF (concise, detailed)

## Core idea
- Resolution + proof by contradiction yields a complete automatic theorem prover for first-order logic.
- Procedure: negate the query, add it to the KB (in CNF), and apply resolution until deriving the empty clause (contradiction). If contradiction arises, KB entails the original query.

## Conjunctive Normal Form (CNF) conversion steps
1. Convert natural-language facts to first-order logic (FOL).
2. Eliminate implications: (P → Q) ≡ (¬P ∨ Q).
3. Move negations inward (De Morgan, double negation).
4. Rename variables to avoid name clashes (standardize apart).
5. Eliminate existential quantifiers by Skolemization (introduce Skolem constants/functions).
6. Move universal quantifiers left and then drop them (all remaining free variables are implicitly universal).
7. Distribute ∨ over ∧ if needed to obtain a conjunction of disjunctions.
8. Split the conjunction into separate clauses (each a disjunction of literals).

Keep a fresh copy of the original KB when testing different queries.

## Example (full walkthrough)
Natural-language KB:
- Whoever can read is literate.
- Dolphins are not literate.
- Some dolphins are intelligent.

Query:
- Is there someone who is intelligent and cannot read?

1. FOL translation:
   - ∀x (reads(x) → literate(x))
   - ∀x (dolphin(x) → ¬literate(x))
   - ∃x (dolphin(x) ∧ intelligent(x))
   - Query: ∃x (intelligent(x) ∧ ¬reads(x))

2. Remove implications:
   - ∀x (¬reads(x) ∨ literate(x))
   - ∀x (¬dolphin(x) ∨ ¬literate(x))
   - ∃x (dolphin(x) ∧ intelligent(x))

3. Skolemize the existential (introduce Skolem constant a):
   - dolphin(a)
   - intelligent(a)

4. Drop universals and standardize apart (use distinct variable names x1, x2, x3 for clauses):
   - C1: ¬reads(x1) ∨ literate(x1)
   - C2: ¬dolphin(x2) ∨ ¬literate(x2)
   - C3: dolphin(a)
   - C4: intelligent(a)

5. Negate the query and convert to CNF without Skolemizing the negation:
   - Query negation: ¬∃x (intelligent(x) ∧ ¬reads(x)) ≡ ∀x (¬intelligent(x) ∨ reads(x))
   - C5: ¬intelligent(x3) ∨ reads(x3)

6. Add C5 to KB and apply resolution (using standard unification/substitution θ each step):

   - Resolve C5 (¬intelligent(x3) ∨ reads(x3)) with C4 (intelligent(a))
     - θ1 = { x3 → a }
     - Resolvent R1: reads(a)

   - Resolve R1 (reads(a)) with C1 (¬reads(x1) ∨ literate(x1))
     - θ2 = { x1 → a }
     - Resolvent R2: literate(a)

   - Resolve R2 (literate(a)) with C2 (¬dolphin(x2) ∨ ¬literate(x2))
     - θ3 = { x2 → a }
     - Resolvent R3: ¬dolphin(a)

   - Resolve R3 (¬dolphin(a)) with C3 (dolphin(a))
     - No variables to bind; resolvent is the empty clause (contradiction).

7. Conclusion: empty clause derived ⇒ contradiction ⇒ original (non-negated) query is entailed by the KB. Therefore there exists an intelligent individual who cannot read.

## Practical points and remarks
- Resolution is a search process; control strategy matters (unit resolution, set-of-support, etc.).
- Substitution sets (the θs) are often of interest (they provide the witness/answer, e.g., a).
- Backtracking and exploring multiple resolution trees may be necessary in complex cases.
- Resolution underlies logic programming (e.g., Prolog uses resolution/SLD resolution).