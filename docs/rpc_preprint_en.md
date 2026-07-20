# From Declaration to Evidence: Research Provenance Card as Version-Bound Infrastructure for AI-Involved Research

Jan Nehyba  
Faculty of Education, Masaryk University, Brno  
ORCID: 0000-0003-4159-5576

Preprint, version 2 (July 2026). Not peer reviewed.

## Abstract

Current AI disclosure in research is often reduced to one generic sentence: AI was used in manuscript preparation. Such wording cannot distinguish language polishing from core intellectual work, is not machine-auditable, and is not bound to a concrete file version. This paper proposes the Research Provenance Card (RPC), a small but practical infrastructure component for AI-involved scholarship. RPC records roles instead of unverifiable percentages, assigns each process claim to a four-level evidence ladder (declared, artifact linked, independently attested, reproduced), binds all checks to SHA-256 content fingerprints, and separates provenance records from truth certification. The model introduces a compensation principle for opaque systems: lower process transparency requires stronger output verification. The paper situates RPC in the ecosystem of publisher policies, reporting guidelines, integrity hubs, AI transparency regulation, and emerging cross-publisher standardization efforts. The manuscript also applies the method reflexively by publishing its own first RPC card.

Keywords: research integrity, provenance, AI-generated research, scholarly communication, metadata standards, attestation

## 1. Introduction

The current disclosure sentence fails in four structural ways.

First, it is semantically weak. It does not distinguish grammar assistance from experimental design, source selection, statistical processing, or interpretation.

Second, it collapses declaration and evidence. A self-report is treated as a record even when no artifact or reproducible trace exists.

Third, verification can float. Checks are commonly tied to a manuscript label, not to immutable content; a file can change while prior verification claims remain visible.

Fourth, there is an authorship gap in fully autonomous outputs. AI cannot be an author under dominant accountability frameworks, while a human with no substantial intellectual contribution may fail authorship criteria.

RPC addresses these issues with version-bound process metadata, evidence levels, and explicit actor-role records.

## 2. Landscape

Publisher policies exist but are fragmented. Some allow only language-level assistance in writing sections; others permit broader generative use if disclosed in methods. This creates a multi-policy burden for authors.

Integrity infrastructure is strong at detecting suspicious submissions but weaker at representing positive, auditable provenance for legitimate AI-assisted work.

Regulatory transparency expectations are increasing, including machine-readable disclosures for generative systems. Journal-level provenance records can complement, but not replace, model-provider obligations.

In parallel, international standardization efforts are defining practical disclosure taxonomies and archival expectations for prompts, logs, and verification responsibilities. RPC is designed as an implementation profile for this emerging consensus.

Reporting-guideline traditions in medicine and related fields (for example PRISMA, CONSORT, SPIRIT, TRIPOD families) demonstrate that checklists improve reporting quality. RPC is not a replacement for domain checklists; it is a cross-domain machine-readable carrier for process claims and evidence levels.

Backward AI-text detection has known limitations and false-positive risks. Provenance-by-design is a forward approach: record process traces at creation time instead of inferring hidden process from final text.

Persistent identifiers matter: ORCID for people, organizational identifiers for institutions, and optional agent identifiers for AI agents.

## 3. Design Principles

### 3.1 Roles, Not Percentages

RPC records role assignments using CRediT-compatible and RPC extension roles. It avoids percentages of intellectual contribution because such percentages are not operationally measurable or auditable.

### 3.2 Evidence Ladder

Each activity claim uses exactly one level:

1. declared
2. artifact_linked
3. independently_attested
4. reproduced

The ladder exposes absence of evidence explicitly; it does not hide uncertainty.

### 3.3 Version Binding by Content Hash

`paper.pdf_sha256` is mandatory. Every check and attestation includes `subject_sha256`. If content changes, the hash changes, and old claims are visibly tied to older content.

### 3.4 Provenance Is Not Truth Certification

RPC does not compute a global truth score, quality score, or acceptance verdict. It records process claims and evidence states only.

### 3.5 Compensation Principle

When process internals are not fully disclosed for legitimate reasons, stronger independent output verification should be required proportionally.

### 3.6 Reference Resolution vs Claim Support

Automated reference checks can verify discoverability and metadata consistency. They cannot, by themselves, guarantee that a citation supports a specific scientific claim. RPC keeps these notions separate.

### 3.7 Agent Identity Continuity

An optional agent identifier can persist while concrete model snapshots evolve over time. The card stores concrete system details per work instance.

## 4. RPC Card Structure and Author Workflow

An RPC card is one JSON document with these major blocks:

- paper
- human_guarantor
- ai_systems
- activities
- artifacts (optional)
- checks (optional)
- attestations (optional)

Artifacts can be public, embargoed, on request, restricted, or not retained, with mandatory rationale for all non-public states.

Practical workflow:

1. Collect process traces already created during work (logs, prompts, code, data records).
2. Fill card fields manually or semi-automatically.
3. Validate against schema.
4. Generate outlet-specific disclosure text from templates.
5. Submit manuscript with card reference.

The design goal is to make honest reporting operationally cheaper than ambiguous disclosure.

## 5. Deployment Strategy

A two-track deployment strategy is useful.

Permissive track: pilot in a community context to measure usability, completion time, missing fields, and reader comprehension.

Strict track: high-integrity venue requiring empirical grounding, explicit run-count disclosure policies, and stricter reproducibility gates.

Predefined stop criteria are important: if evidence levels collapse mostly to declared without practical uplift, effort should shift toward tooling usability and interoperability first.

## 6. Limitations

RPC does not prevent dishonest declarations at level declared.

Independent attestation quality depends on attestor credibility.

Run-selection bias remains a risk without stronger protocol controls.

Provenance does not detect training-data contamination by itself.

Adoption can fail if workflow cost is perceived as extra bureaucracy.

Standard alignment can evolve; mapping layers are required over time.

## 7. Discussion

If successful, the key cultural question shifts from Was AI used? to What evidence level supports each process claim?

Institutionally, RPC can help represent autonomous and mixed workflows while preserving human accountability boundaries.

Machine-readable provenance is increasingly relevant for AI-assisted literature synthesis and review pipelines, where process metadata can influence automated trust routing without claiming scientific truth.

## 8. Conclusion

A single disclosure sentence is insufficient for auditable AI-era scholarship. A minimal infrastructure response is a version-bound, evidence-graded provenance card that records who did what and what was evidenced, without pretending to certify truth. RPC aims to be practical, open, and interoperable with emerging disclosure standards while remaining explicit about its limits.

## AI Use Statement

This manuscript was developed through extensive human-AI collaboration. AI systems supported conceptual exploration, drafting support, and iterative refinement. Final responsibility, framing decisions, and accountability remain with the human guarantor.

## Data and Code Availability

RPC specification, schema, validator, reference-resolution utility, disclosure generator, and registry implementation are available in the project repository under permissive licenses.

## Appendix A: RPC Card for This Manuscript

The manuscript includes an RPC card in the repository registry. Status values indicate process evidence states and do not represent a truth certificate.