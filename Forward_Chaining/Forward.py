facts = [
    ("Human", "John"),
    ("Human", "Alice")
]

# Rules
rules = [
    {
        "forall": ["x"],
        "if": [("Human", "?x")],
        "exists": [],
        "then": ("Mortal", "?x")
    },
    {
        "forall": ["x"],
        "if": [("Human", "?x")],
        "exists": ["y"],
        "then": ("Parent", "?y", "?x")
    }
]

# Store generated existential witnesses
witnesses = {}


# Match a pattern with a fact
def match(pattern, fact, sub):
    if pattern[0] != fact[0]:
        return None

    new_sub = sub.copy()

    for p, f in zip(pattern[1:], fact[1:]):

        if p.startswith("?"):
            if p in new_sub:
                if new_sub[p] != f:
                    return None
            else:
                new_sub[p] = f

        elif p != f:
            return None

    return new_sub


# Generate a unique witness for existential variables
def get_witness(rule_id, var, sub):
    key = (rule_id, var, tuple(sorted(sub.items())))

    if key not in witnesses:
        witnesses[key] = f"{var.upper()}_{len(witnesses) + 1}"

    return witnesses[key]


# Forward Chaining
def forward_chaining(query):
    changed = True

    while changed:
        changed = False

        for rule_id, rule in enumerate(rules):

            substitutions = [{}]

            # Match all premises
            for premise in rule["if"]:
                new_subs = []

                for sub in substitutions:
                    for fact in facts:
                        result = match(premise, fact, sub)

                        if result is not None:
                            if result not in new_subs:
                                new_subs.append(result)

                substitutions = new_subs

            # Apply the rule to matching substitutions
            for sub in substitutions:

                final_sub = sub.copy()

                # Handle existential variables
                for var in rule["exists"]:
                    final_sub["?" + var] = get_witness(
                        rule_id, var, sub
                    )

                # Generate conclusion
                conclusion = tuple(
                    final_sub.get(item, item)
                    for item in rule["then"]
                )

                if conclusion not in facts:
                    facts.append(conclusion)
                    print("Derived:", conclusion)
                    changed = True

    # Check query
    for fact in facts:
        if match(query, fact, {}) is not None:
            return True

    return False


# Queries
queries = [
    ("Mortal", "John"),
    ("Parent", "?y", "John"),
    ("Mortal", "Alice")
]

for query in queries:
    print("\nQuery:", query)

    if forward_chaining(query):
        print("Query proved!")
    else:
        print("Query not proved.")

print("\nFinal Knowledge Base:")
for fact in facts:
    print(fact)