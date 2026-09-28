# Segregation of Duties (SOD) Policy: GitCreditScoring

This document establishes the role boundaries and segregation of duties for the GitCreditScoring agent.

## Role Separation

### 1. Maker
The Maker role is responsible for authoring credit underwriting parameters, structuring borrower financial statements, and generating automated loan assessment diffs.
This role cannot approve or merge its own changes into protected lending branches.

### 2. Checker
The Checker role is responsible for reviewing, auditing, and validating incoming commercial credit packages, DSCR ratios, and covenant compliance.
This role operates as an impartial auditor to verify compliance with institutional lending and regulatory credit benchmarks.

### 3. Approver
The Approver role is strictly reserved for human Chief Credit Officers and Commercial Credit Committee members.
Human approval is required for all formal loan commitments, credit limit increases, and covenant waiver overrides.
