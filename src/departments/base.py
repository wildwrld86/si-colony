"""Base department interface for modular colony structure."""

from abc import ABC, abstractmethod
from typing import Dict, Any

class Department(ABC):
    """Abstract base for spawnable colony departments."""

    def __init__(self, name: str, colony_kernel):
        self.name = name
        self.kernel = colony_kernel

    @abstractmethod
    def act(self, plan: Dict) -> Dict[str, Any]:
        """Execute department responsibilities given current plan."""
        pass

    def report(self) -> Dict:
        return {"department": self.name, "status": "active"}
