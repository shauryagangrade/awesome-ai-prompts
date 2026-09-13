# Reusable prompt: database schema & migrations

Copy-paste the block below into any AI coding agent to design or evolve a
database schema safely - backward-compatible migrations and a clean rollout.

---

Design/update the database schema for `[feature/change]` in this repository
and write the migrations. Treat the schema like a public API: changes must be
backward-compatible unless the migration plan explicitly says otherwise.

## Steps

1. **Understand the data** - Read the existing schema, models, and the code
   that reads/writes this data. Understand current constraints, indexes, and
   how queries are actually made. Don't design in a vacuum.
2. **Design the change** - Keep it minimal and consistent with existing
   naming and conventions. Consider: types, nullability, defaults, indexes for
   the real query patterns, constraints, and referential integrity.
3. **Write backward-compatible migrations** - Apply the migration framework
   the repo already uses (check for Alembic, Prisma, Django, Knex, Flyway,
   etc.). Default rule: old code must keep working against the new schema.
   Follow this pattern:
   - **Expand**: add new columns/tables without breaking existing reads and
     writes; make new columns nullable or defaulted first.
   - **Migrate data**: backfill new columns in a separate step where needed,
     in a transaction.
   - **Contract**: only then drop old columns/tables (often in a later
     migration after the old code is gone).
   - Down migration must safely reverse the up migration (drop what you
     added, restore what you removed).
4. **Watch for the classic failures** - Adding `NOT NULL` to a populated
   table, renaming columns (use add + migrate + drop instead), changing a
   column type that breaks comparisons, adding an index that locks a big
   table. Flag any that apply.
5. **Verify** - Run the migration up and down against a local database, run
   the test suite, and confirm the new code paths work against the migrated
   schema. Confirm existing tests still pass on the new schema.

## Rules

- Never write a migration that drops or renames data without a stated,
  approved plan.
- Never run destructive migrations against a real database without explicit
  confirmation.
- Keep each migration focused on one logical change.
- If the schema change can't be made backward-compatible, stop and flag the
  coordination needed instead of hiding it.
