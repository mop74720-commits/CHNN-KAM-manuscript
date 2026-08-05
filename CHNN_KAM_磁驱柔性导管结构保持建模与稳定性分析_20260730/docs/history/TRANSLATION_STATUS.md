> **历史记录：** 本文档反映早期迁移或双语搭建阶段，不代表当前工程状态。当前说明以根目录 `README_CN.md` 和 `docs/audits/BUILD_VALIDATION.md` 为准。

# English Translation Status

The verified Chinese manuscript in `manuscript/zh/` remains the authoritative content baseline. The English manuscript in `manuscript/en/` has now undergone a complete language-layer translation while preserving the mathematical and semantic skeleton.

| File | Translation status | Structural audit |
|---|---|---|
| `00-introduction.tex` | Complete | Passed |
| `01-rod-model.tex` | Complete | Passed |
| `02-galerkin-discretization.tex` | Complete | Passed |
| `03-hamiltonian-structure.tex` | Complete | Passed |
| `04-chnn-model.tex` | Complete | Passed |
| `05-symplectic-kam.tex` | Complete | Passed |
| `06-numerical-results.tex` | Complete language translation; experimental placeholders retained | Passed |
| `07-discussion.tex` | Complete | Passed |
| `08-conclusion.tex` | Complete language translation; experimental placeholders retained | Passed |

## Invariants preserved

- Section hierarchy and file assembly order
- All `\label` identifiers and their order
- Displayed and inline mathematical structure
- Theorem, proposition, lemma, assumption, corollary, proof, and result-placeholder environments
- `\ref`, `\eqref`, `\cref`, and `\Cref` targets
- BibTeX citation keys
- Experimental placeholders and the original boundaries of the claims

## Remaining work before submission

1. Insert stable numerical results into the Chinese baseline and mirror the approved language-layer updates in English.
2. Perform a journal-level English copyedit after the scientific content is frozen.
3. Select a target journal and implement its adapter for the document class, front matter, bibliography style, and declarations.
