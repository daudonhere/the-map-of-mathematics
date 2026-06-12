from __future__ import annotations

from themap.core.repository import Repository
from themap.core.service import MapService


class TestMapService:
    def test_search(self, sample_repo: Repository) -> None:
        service = MapService(sample_repo)
        results = service.search("number")
        assert len(results) == 1
        assert results[0].id == "number-theory"

    def test_explore_existing(self, sample_repo: Repository) -> None:
        service = MapService(sample_repo)
        graph = service.explore("algebra")
        assert len(graph.nodes) == 3
        assert len(graph.edges) == 2

    def test_explore_nonexistent(self, sample_repo: Repository) -> None:
        service = MapService(sample_repo)
        graph = service.explore("unknown")
        assert graph.nodes == []
        assert graph.edges == []

    def test_visualize(self, sample_repo: Repository) -> None:
        service = MapService(sample_repo)
        graph = service.visualize(["algebra", "geometry"])
        assert len(graph.nodes) >= 3
