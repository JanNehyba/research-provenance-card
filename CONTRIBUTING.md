# Contributing

## Development
- Python 3.12+
- Install dependencies:
  - `pip install -r requirements.txt`

## Quality Gates
- Run tests: `pytest`
- Validate examples: `python tools/validate.py "schema/examples/*.json"`

## Pull Requests
- Keep PRs small and focused.
- Use clear commit messages.
- For schema changes, include:
  - rationale
  - compatibility note
  - updated examples/tests
