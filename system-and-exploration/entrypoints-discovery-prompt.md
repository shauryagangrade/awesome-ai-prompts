# Reusable prompt: entrypoints discovery

Copy-paste the block below into any AI coding agent to list every way a
codebase actually starts: servers, CLIs, workers, scheduled jobs, migrations,
and scripts. For each one it records the config it needs, the ports it opens,
and where in the code it begins. It is read-only.

Keywords: entrypoints, how to run, startup, onboarding, services map, cron jobs, workers, ports, environment variables

---

Discover every runtime entrypoint in this repository, read-only. The goal: a
verified map of how the system starts and what each part needs, good enough for
onboarding a new engineer or planning a deployment. Do not run, start, or
modify anything unless the user asks afterwards.

## Steps

1. **Define the scope** - State what you are mapping (the whole repository, one
   service in a monorepo) and the languages and frameworks you found. Read the
   README, the manifests (`package.json`, `pyproject.toml`, `go.mod`,
   `Cargo.toml`), the container and orchestration files (`Dockerfile`,
   `docker-compose.yml`, Kubernetes manifests), the process files (`Procfile`,
   `supervisord.conf`), and the CI and deploy workflows.
2. **Enumerate the entrypoints** - Find and list each of these, with a
   `file:line` reference for where it starts: web and API servers, CLI
   commands, background workers and queue consumers, scheduled jobs (cron,
   CI schedules, cloud schedulers), database migrations and seed scripts,
   one-off scripts, and test or build commands that people run by hand. Take
   the commands from the manifests' `scripts` and `bin` fields, the container
   `CMD` and `ENTRYPOINT`, and the compose and deploy definitions, then confirm
   each one in the code.
3. **Record what each one needs** - For each entrypoint, list the environment
   variables and config files it reads (follow the code that reads them), the
   ports and protocols it opens or connects to, and the services it depends on
   (database, cache, queue, external APIs). Mark each variable as required or
   optional, and note the default if the code sets one. Never copy the values
   of secrets.
4. **Map the connections** - Show how the entrypoints relate: which one calls
   or enqueues work for another, which share a database or queue, and which
   must start first. A short list or a diagram is enough.
5. **Flag what you could not confirm** - List entrypoints that appear in docs
   or config but have no matching code, code that looks like an entrypoint but
   is never referenced, and anything that needs a running system to confirm.
6. **Write the summary** - Finish with a short, ordered "how to run this"
   section: what to start, in which order, with which settings, and what a
   healthy start looks like (a log line, a health endpoint, a port).

## Verification

- [ ] Every entrypoint has a `file:line` reference and the command that starts
      it.
- [ ] Every entrypoint lists its required and optional environment variables,
      with no secret values copied.
- [ ] Ports, protocols, and service dependencies are listed for each one.
- [ ] Entrypoints named in docs or config were checked against the code, and
      mismatches are listed.
- [ ] The start order and a healthy-start signal are stated.
- [ ] Nothing was started, installed, or modified.

## Rules

- Never start a server, run a job, or execute a migration to find out what it
  does; read the code instead.
- Never print or copy secret values from `.env` files or config.
- Never list an entrypoint you only inferred; mark it unconfirmed.
- Never rely on the README alone; confirm each entry in the code or manifests.
- If the repository has several services, map each one separately instead of
  merging them.
