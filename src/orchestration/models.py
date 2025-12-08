from enum import Enum
from typing import Dict, Any, List, Optional
from datetime import datetime

class NodeStatus(Enum):
    """Status of a DAG node"""
    PENDING = "pending"
    RUNNING = "running" 
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"

class DAGNode:
    """Represents a node/agent in the workflow"""
    
    def __init__(self, name: str, agent: Any, dependencies: List[str] = None):
        self.name = name
        self.agent = agent
        self.dependencies = dependencies or []
        self.status = NodeStatus.PENDING
        self.output = None
        self.started_at: Optional[datetime] = None
        self.completed_at: Optional[datetime] = None
        self.error: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert node to dictionary for monitoring"""
        return {
            "name": self.name,
            "status": self.status.value,
            "dependencies": self.dependencies,
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
            "has_output": self.output is not None,
            "error": self.error
        }

class WorkflowContext:
    """Shared context/data passed between nodes"""
    
    def __init__(self, initial_data: Dict[str, Any] = None):
        self.data = initial_data or {}
        self.execution_log: List[Dict[str, Any]] = []
    
    def set(self, key: str, value: Any):
        """Store data in context"""
        self.data[key] = value
    
    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve data from context"""
        return self.data.get(key, default)
    
    def has(self, key: str) -> bool:
        """Check if key exists in context"""
        return key in self.data
    
    def log_execution(self, node_name: str, status: str, message: str = ""):
        """Log execution step"""
        self.execution_log.append({
            "timestamp": datetime.now().isoformat(),
            "node": node_name,
            "status": status,
            "message": message
        })
    
    def get_summary(self) -> Dict[str, Any]:
        """Get workflow summary"""
        return {
            "total_steps": len(self.execution_log),
            "data_keys": list(self.data.keys()),
            "execution_log": self.execution_log[-5:]  # Last 5 steps
        }