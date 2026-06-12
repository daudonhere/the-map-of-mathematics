from __future__ import annotations

from themap.core.repository import Repository


class TestRepository:
    def test_add_and_get(self, sample_repo: Repository) -> None:
        c = sample_repo.get_by_id("algebra")
        assert c is not None
        assert c.name == "Algebra"

    def test_get_nonexistent(self, sample_repo: Repository) -> None:
        assert sample_repo.get_by_id("nonexistent") is None

    def test_search(self, sample_repo: Repository) -> None:
        results = sample_repo.search("geo")
        assert len(results) == 1
        assert results[0].id == "geometry"

    def test_search_empty(self, sample_repo: Repository) -> None:
        assert sample_repo.search("zzzzz") == []

    def test_get_related(self, sample_repo: Repository) -> None:
        related = sample_repo.get_related("algebra")
        assert len(related) == 2
        ids = {r.id for r in related}
        assert ids == {"geometry", "number-theory"}

    def test_get_all(self, sample_repo: Repository) -> None:
        all_concepts = sample_repo.get_all()
        assert len(all_concepts) == 4
