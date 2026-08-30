# `infrastructure/` — Local Generic-Layer Copy

Project-local minimal Layer-1 utilities. This is a small vendored copy, not
the full template `infrastructure/` tree.

```
infrastructure/
└── core/
    └── logging/
        └── utils.py     # get_logger() — root-configured logging helper
```

Imported by `src/` per the project rule that the only external Layer-1
imports allowed are from `infrastructure.core.*`.
