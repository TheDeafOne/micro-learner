# Summary for EN.605.645.82.FA25 Artificial Intelligence – Module 7: Logic and Reasoning – Module 7 - Lectures

## https://jh.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=9fbe707f-da1f-44cb-b73c-b0c1017767ce

# Propositional Logic — Concise Summary

- Motivation and context
  - Logic provides a formal way to represent and reason about knowledge, similar to state-space/search formalisms used earlier (states, actions, transitions, goals).
  - Early AI emphasized games and theorem proving as measures of intelligence; logic supports reasoning about what an agent knows.

- Syntax (formation rules)
  - Constants: T (true), F (false).
  - Propositional symbols (sentences): P, Q, R, ...
  - If P (and Q) are sentences, then so are:
    - (P) — parenthesized sentence
    - ¬P — negation
    - P ∨ Q — disjunction (or)
    - P ∧ Q — conjunction (and)
    - P → Q — implication (material conditional)
    - P ↔ Q — equivalence (biconditional)

- Semantics
  - A model = an assignment of T/F to each propositional symbol.
  - Truth-tables enumerate all possible models (rows = models).
  - Basic truth rules:
    - ¬P true iff P is false.
    - P ∨ Q true iff at least one of P, Q is true.
    - P ∧ Q true iff both P and Q are true.
    - P → Q is false only when P is true and Q is false; otherwise true (material implication — not causal).
    - P ↔ Q true iff P and Q have the same truth value.

- Satisfiability / Validity / Unsatisfiability
  - Satisfiable: a sentence that is true in at least one model.
  - Valid (tautology): a sentence true in every model (e.g., P ∨ ¬P).
  - Unsatisfiable (contradiction): a sentence true in no model (e.g., P ∧ ¬P).

- Example truth-patterns (compact)
  - P: T, F
  - ¬P: F, T
  - P ∨ Q: T when P or Q or both T; false only when both F.
  - P ∧ Q: T only when both T; otherwise false.
  - P → Q: F only for (P = T, Q = F); otherwise T.
  - P ↔ Q: T when (P,Q) = (T,T) or (F,F).

- Common inference rules
  - Modus Ponens:
    - From P → Q and P, infer Q.
  - Modus Tollens:
    - From P → Q and ¬Q, infer ¬P.
  - De Morgan’s laws:
    - ¬(P ∧ Q) ≡ ¬P ∨ ¬Q
    - ¬(P ∨ Q) ≡ ¬P ∧ ¬Q
  - Unit resolution:
    - From (P ∨ Q) and ¬Q, infer P.
  - Resolution (binary):
    - From (P ∨ Q) and (¬Q ∨ R), infer (P ∨ R).

- Notes
  - Many logical operators can be expressed using a small basis (e.g., ¬ and ∨ suffices).
  - Truth-table proofs can be used to demonstrate validity of inference rules (e.g., show modus ponens/tollens by enumerating models).

## https://jh.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=509be047-be0d-4868-9993-b0cc008732a0

# Summary

- Domain: Wumpus (lumps) world — a grid with pits, a single Wumpus, and gold. Hazards kill the agent; getting gold wins. Percepts in a square:
  - Stench: Wumpus in a neighboring square.
  - Breeze: pit in a neighboring square.
  - Glitter: gold in the square.
  - Bump: hit a wall.
  - Scream: Wumpus killed.

- Notation:
  - Cij: cell at row i, column j.
  - Sij: stench sensed in Cij.
  - Bij: breeze sensed in Cij.
  - Wij: Wumpus resides in Cij.
  - Start at C11 with all percept booleans initially false.

- Knowledge base (KB) as propositional implications (examples):
  - ¬S11 ⇒ ¬W11 ∧ ¬W21 ∧ ¬W12 (no stench at 1,1 ⇒ no Wumpus in any neighbor)
  - ¬S12 ⇒ ¬W11 ∧ ¬W12 ∧ ¬W22 ∧ ¬W13 (similar for other cells)
  - S12 ⇒ W11 ∨ W12 ∨ W22 ∨ W13 ∨ W? (stench implies Wumpus is in one of the neighboring cells)
  - analogous implications for breezes and pits (Bij ⇒ pit in one of neighbors; ¬Bij ⇒ no pit in neighbors)

- Inference process demonstrated:
  - From S11 = false and the KB, apply modus ponens to conclude W11, W21, W12 are false (and-elimination to split conjuncts).
  - Move to C21: Bij = true (breeze). From Bij and KB: pit at 31 or 22 (disjunction).
  - Move to C12: S12 = true (stench). From S12 and the KB get a disjunction for possible Wumpus locations. Using prior facts that rule out W11 and W12 (from earlier ¬S11), and using resolution to eliminate possibilities, deduce the Wumpus must be in a specific remaining cell (e.g., W13).
  - Repeated use of modus ponens, and-elimination, and resolution yields concrete safe/unsafe cell conclusions.

- Observations about representation:
  - Propositional logic with concrete atoms and implications is powerful enough to reason and derive safe moves, but it is cumbersome:
    - No variables, no functions/relations, so every cell-specific rule must be written separately.
    - Desirable compact form would use variables/quantifiers to express general rules such as:
      - ∀i,j: ¬Sij ⇒ ∧neighbors ¬Wneighbor
      - ∀i,j: Sij ⇒ ∨neighbors Wneighbor
  - This motivates moving to a more expressive representation (first-order logic or a rule schema) to avoid large, repetitive KBs.

## https://jh.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=2078e79d-1643-4987-a699-b0c6011d6834

# First‑Order Logic (Predicate Calculus) — Summary

- Language elements
  - Constants: named domain objects (e.g., John).
  - Functions: map objects to objects (e.g., leftLeg(John) returns an object).
  - Predicates: map objects (or tuples of objects) to truth values (e.g., Brother(x,y)).
  - Variables: placeholders (x, y, ...).
  - Connectives: ¬, ∧, ∨, →, ↔ (as in propositional logic).
  - Quantifiers: ∀ (for all), ∃ (there exists).
  - Equality: = for identity.

- Functions vs predicates
  - Functions return objects, not truth values. Bare terms like leftFoot(John) cannot be used as propositions.
  - Predicates are needed to assert truth about terms (e.g., HasLeftFoot(John) → HasLeftLeg(John)).

- Semantics of quantifiers
  - ∀x P(x) ≈ a (possibly infinite) conjunction: P must hold for every relevant instantiation of x.
  - ∃x P(x) ≈ a disjunction: P must hold for at least one instantiation.
  - The universe of discourse or typing matters: use predicates or implication to restrict domain (e.g., ∀x (Person(x) → LovesRaymond(x)) means “everyone (who is a person) loves Raymond”).
  - Beware of syntax differences: ∀x (AtJHU(x) → Smart(x)) asserts “everyone at JHU is smart”; ∀x (AtJHU(x) ∧ Smart(x)) wrongly asserts “everyone is at JHU and everyone is smart.”

- Quantifier properties
  - Same quantifier commutes: ∀x ∀y P ≡ ∀y ∀x (and similarly for ∃).
  - Mixed quantifiers do not commute: ∃x ∀y Loves(x,y) (someone loves everyone) ≠ ∀y ∃x Loves(x,y) (for each person there is someone who loves them).
  - Duality via negation:
    - ¬∃x P(x) ≡ ∀x ¬P(x)
    - ¬∀x P(x) ≡ ∃x ¬P(x)

- Inference with quantifiers
  - Universal elimination (instantiation): from ∀x P(x) infer P(c) for any appropriate constant c.
  - Existential elimination: from ∃x P(x) infer P(c) for some fresh constant c not used elsewhere (a Skolem constant).
  - Most propositional inference methods carry over, but quantifiers require these instantiation steps to be used effectively in proofs and reasoning.

- Practical note
  - Correct use of quantifier scope, domain restrictions (typing), and fresh constants for existential reasoning is essential to avoid unintended meanings.

## https://jh.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=d3bc6ed9-98c8-43e5-823f-b0c800cbb51a

# Summary

- Conversion to first-order logic
  - Translate facts and rules into predicates and quantified implications.  
    - Example predicates: Buffalo(x), Pig(y), Slug(z), Faster(x,y).  
    - Example rules: ∀x,y (Buffalo(x) ∧ Pig(y) → Faster(x,y)); ∀y,z (Pig(y) ∧ Slug(z) → Faster(y,z)); ∀x,y,z (Faster(x,y) ∧ Faster(y,z) → Faster(x,z)).
  - Ground facts: Buffalo(Bob), Pig(Pat), Slug(Steve).

- Inference primitives
  - Use standard logical rules (universal elimination/instantiation, modus ponens, and-introduction/elim) and substitution to derive conclusions.
  - Variables are local to each sentence (the x in one rule is not automatically the same x in another).

- Forward chaining (data-driven)
  - Match the left-hand side (antecedents) of implications against known facts to produce new facts, iterating until the goal is found or no more facts can be produced.
  - Example derivation:
    1. From Buffalo(Bob) and Pig(Pat) + rule ∀x,y (Buffalo(x) ∧ Pig(y) → Faster(x,y)) derive Faster(Bob,Pat).
    2. From Pig(Pat) and Slug(Steve) + rule ∀y,z (Pig(y) ∧ Slug(z) → Faster(y,z)) derive Faster(Pat,Steve).
    3. From Faster(Bob,Pat) and Faster(Pat,Steve) + rule ∀x,y,z (Faster(x,y) ∧ Faster(y,z) → Faster(x,z)) derive Faster(Bob,Steve).

- Backward chaining (goal-driven)
  - Start with a goal and match it to the right-hand side (consequent) of implications to generate subgoals (new left-hand-side facts to prove), recursively until ground facts are reached.
  - Example for goal Faster(Bob,Steve):
    - Match to rule ∀x,y,z (Faster(x,y) ∧ Faster(y,z) → Faster(x,z)) → subgoals Faster(Bob,?y) and Faster(?y,Steve).
    - Instantiate ?y = Pat. Prove Faster(Bob,Pat) via rule 1 using Buffalo(Bob) and Pig(Pat). Prove Faster(Pat,Steve) via rule 2 using Pig(Pat) and Slug(Steve).

- Search considerations and problems
  - The inference process is a form of search (often depth-first), requiring instantiation choices and potentially backtracking when contradictions or dead ends occur.
  - Different instantiations can lead to divergent paths or contradictions; backtracking is needed to recover.
  - These choices can cause combinatorial explosion in the space of facts/rules to try—an important practical limitation (relevant to planning algorithms).

## https://jh.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=a30a1a5f-76f6-4b34-b51e-b0cb0014a337

- Definition
  - Unification: process that finds a substitution θ making two expressions identical.
  - unify(P, Q) returns a substitution list θ (possibly empty). Failure can be indicated by null (or a special failure value); an empty list means no substitution needed.

- Simple examples
  - unify(P(a, X), P(a, B)) → {X = B}
  - unify(P(a, X), P(Y, B)) → {Y = a, X = B}
  - unify(P(a, X), P(Y, f(Y))) → {Y = a, X = f(a)} (variables may be substituted by compound terms/functions)

- Standardizing apart
  - Variables with the same name in different sentences must be renamed to fresh, unique names before unification (standardize apart). Example:
    - P(a, X) and P(X, B) should be treated as P(a, X1) and P(X2, B) so X1 and X2 are distinct. Then unify → {X1 = B, X2 = a}.
  - Without standardizing, same-name variables across clauses can be incorrectly treated as the same variable.

- Failure cases
  - Conflicting assignments: attempting to assign two different constants to the same variable (e.g., trying to force a variable to be both a and b).
  - Multiple occurrences constraint: if a single variable must equal two different ground terms because it appears twice in a pattern (e.g., matching P(a, B) with P(X, X) fails if a ≠ B).
  - Occurs/check-related failures: cannot assign a variable to a term that contains that variable (avoids infinite regress), and cannot equate a constant with a non-variable function term when they are different.

- Key points
  - Unification can bind variables to constants or to compound terms (functions).
  - Always standardize apart before attempting unification to avoid accidental variable name clashes.
  - Unification succeeds when a consistent substitution exists; otherwise it fails for the above reasons.

## https://jh.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=b773f86b-5c0e-4e58-9735-b0c1013ca025

# Summary — Resolution and CNF (concise, technical)

- Resolution rule(s)
  - Unit resolution: from (p ∨ q) and (¬q) infer p.
  - General resolution: from (p ∨ q) and (¬q ∨ r) infer (p ∨ r).
  - Add proof by contradiction: negate the query, add it to the KB, and derive a contradiction (empty clause) to show the KB entails the query.

- Conjunctive Normal Form (CNF)
  - CNF = conjunction of disjunctions (clauses). Clauses can be written one per line.
  - Standard CNF conversion steps:
    1. Eliminate implications: (P ⇒ Q) ≡ (¬P ∨ Q).
    2. Move negations inward (De Morgan, double negation).
    3. Rename variables to avoid name clashes (standardize apart).
    4. Eliminate existential quantifiers via Skolemization (introduce Skolem constants/functions).
    5. Move universal quantifiers to front and then drop them for clause form.
    6. Distribute OR over AND as needed to obtain conjunction of clauses.
    7. Split conjunction into separate clauses and standardize variables across clauses.

- Handling a query
  - Convert the query to FOL, negate it, then convert that negation to CNF.
  - Use duality to change an existential-negated query into a universal form (so you add universally quantified clauses). Keep variables fresh to avoid accidental unification with KB constants.
  - Add the negated query clauses to a fresh copy of the KB for the proof attempt.

- Worked example (KB and query)
  - KB (text → FOL):
    - ∀x (Read(x) ⇒ Literate(x))
    - ∀x (Dolphin(x) ⇒ ¬Literate(x))
    - ∃x (Dolphin(x) ∧ Intelligent(x))
  - Query: ∃x (Intelligent(x) ∧ ¬Read(x))
  - Negated query → CNF:
    - ¬∃x (Intelligent(x) ∧ ¬Read(x)) ≡ ∀x (¬Intelligent(x) ∨ Read(x))
  - Skolemize existential in KB: introduce constant a for the existential dolphin:
    - Dolphin(a)
    - Intelligent(a)
  - Clauses (standardized apart):
    - ¬Read(x1) ∨ Literate(x1)
    - ¬Dolphin(x2) ∨ ¬Literate(x2)
    - Dolphin(a)
    - Intelligent(a)
    - ¬Intelligent(x3) ∨ Read(x3)   (negated query clause)

- Resolution proof sequence (with unifiers θ shown)
  1. Resolve Intelligent(a) with ¬Intelligent(x3):
     - θ1 = {x3/a} → derive Read(a).
  2. Resolve Read(a) with ¬Read(x1):
     - θ2 = {x1/a} → derive Literate(a).
  3. Resolve Literate(a) with ¬Literate(x2):
     - θ3 = {x2/a} → derive ¬Dolphin(a).
  4. Resolve ¬Dolphin(a) with Dolphin(a):
     - derive empty clause (contradiction).
  - Conclusion: empty clause → original (non-negated) query is entailed by KB.

- Practical notes and strategies
  - Resolution is a search procedure; common control strategies include:
    - Unit resolution (prioritize unit clauses).
    - Set-of-support (start with clauses derived from the negated query and only resolve against their descendants).
  - Maintain and show substitution lists (θ) during unification; substitution sets can be the desired answers.
  - Backtracking and multiple resolution trees may be necessary; sometimes several partial trees unify to produce the final contradiction.
  - Resolution underlies logic programming (e.g., Prolog) and provides an automatic theorem-proving method.