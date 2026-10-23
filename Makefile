install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/*.whl
lint:
	uv run ruff check brain_games
tool :
	uv tool install --force dist/*.whl

brain-even:
	uv run brain-even
brain-calc:
	uv run brain-calc
brain-gcd:
	uv run brain-gcd
brain-progression:
	uv run brain-progression
brain-prime:
	uv run brain-prime
fixe:
	uv run ruff check --fix brain_games