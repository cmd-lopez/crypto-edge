.PHONY: ci lookahead test

# Identical to .github/workflows/ci.yml. Tests use synthetic data only (no network, no cache).
ci:
	uv sync --frozen
	$(MAKE) lookahead
	$(MAKE) test

# Look-ahead guards, run as their own gate so a failure is unmistakable.
lookahead:
	uv run pytest -k look_ahead -v

test:
	uv run pytest
