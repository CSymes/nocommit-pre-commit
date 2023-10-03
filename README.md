# ps1-nocommit-pre-commit

A [`pre-commit`](https://pre-commit.com) hook to check staged file contents for
a specific phrase that should block the commit. This is useful for developers
to leave reminders for themselves to return to a topic before checking work in.

By default this phrase is `nocommit`, hence the repository name.  

## Usage

Make sure `pre-commit` is [installed](https://pre-commit.com#install).

Add a new repo entry to your configuration file:

```yaml
repos:

  - repo: https://github.com/CSymes/nocommit-pre-commit
    rev: <git sha or tag>
    hooks:
      - id: ps1-nocommit
        # args: ["-searchstr", "nocommit"] # optional: modify the gate phrase to something other than the default
```

You can then leave comments to yourself using this phrase and the hook
will ensure that you address the flagged issue before committing it.

e.g.

```C#
 // nocommit: document this function
```
