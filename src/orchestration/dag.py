from typing import Dict, List, Any, Optional
from datetime import datetime
from .models import DAGNode, NodeStatus, WorkflowContext

class DAGOrchestrator:
    """
    Manages DAG (Directed Acyclic Graph) workflow execution.
    Executes agents in proper order based on dependencies.
    """
    
    def __init__(self):
        self.nodes: Dict[str, DAGNode] = {}
        self.context = WorkflowContext()
        self.execution_order: List[str] = []
    
    def add_node(self, name: str, agent: Any, dependencies: List[str] = None):
        """
        Add a node/agent to the DAG.
        
        Args:
            name: Unique node name
            agent: Agent instance
            dependencies: List of node names that must complete before this node
        """
        if name in self.nodes:
            raise ValueError(f"Node '{name}' already exists")
        
        self.nodes[name] = DAGNode(name, agent, dependencies or [])
        print(f"📌 Added node: {name} (dependencies: {dependencies or []})")
    
    def build_execution_order(self):
        """Calculate execution order using topological sort"""
        print("🧮 Building execution order...")
        
        # Reset
        self.execution_order = []
        visited = set()
        temp_visited = set()
        
        def visit(node_name: str):
            if node_name in temp_visited:
                raise Exception(f"Cycle detected in DAG involving node: {node_name}")
            
            if node_name not in visited:
                temp_visited.add(node_name)
                
                # Visit all dependencies first
                node = self.nodes[node_name]
                for dep in node.dependencies:
                    if dep not in self.nodes:
                        raise Exception(f"Dependency '{dep}' not found for node '{node_name}'")
                    visit(dep)
                
                temp_visited.remove(node_name)
                visited.add(node_name)
                self.execution_order.append(node_name)
        
        # Visit all nodes
        for node_name in self.nodes:
            if node_name not in visited:
                visit(node_name)
        
        print(f"✅ Execution order: {' → '.join(self.execution_order)}")
    
    def execute(self, initial_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the complete DAG workflow.
        
        Args:
            initial_data: Initial input data
            
        Returns:
            Final context with all outputs
        """
        print("\n" + "="*50)
        print("🚀 STARTING DAG WORKFLOW EXECUTION")
        print("="*50)
        
        # Set initial data
        self.context = WorkflowContext(initial_data)
        
        # Build execution order
        self.build_execution_order()
        
        # Execute nodes in order
        for node_name in self.execution_order:
            node = self.nodes[node_name]
            
            # Check if dependencies are satisfied
            if not self._check_dependencies(node):
                node.status = NodeStatus.SKIPPED
                self.context.log_execution(node_name, "skipped", "Dependencies not met")
                continue
            
            # Execute node
            self._execute_node(node)
        
        print("\n" + "="*50)
        print("🎉 DAG WORKFLOW COMPLETED SUCCESSFULLY")
        print("="*50)
        
        # Generate final outputs
        return self._generate_final_outputs()
    
    def _check_dependencies(self, node: DAGNode) -> bool:
        """Check if all dependencies are completed"""
        for dep_name in node.dependencies:
            dep_node = self.nodes[dep_name]
            if dep_node.status != NodeStatus.COMPLETED:
                print(f"   ⏸️  Node '{node.name}' waiting for '{dep_name}'")
                return False
        return True
    
    def _execute_node(self, node: DAGNode):
        """Execute a single node/agent"""
        print(f"\n🔧 Executing: {node.name}")
        
        node.status = NodeStatus.RUNNING
        node.started_at = datetime.now()
        self.context.log_execution(node.name, "running")
        
        try:
            # Prepare input data for agent
            input_data = self._prepare_node_input(node)
            
            # All agents should have a process method now
            output = node.agent.process(input_data)
            
            node.output = output
            
            # Store output in context
            self.context.set(node.name, output)
            
            node.status = NodeStatus.COMPLETED
            node.completed_at = datetime.now()
            
            duration = (node.completed_at - node.started_at).total_seconds()
            print(f"   ✅ {node.name} completed in {duration:.2f}s")
            self.context.log_execution(node.name, "completed", f"Duration: {duration:.2f}s")
            
        except Exception as e:
            node.status = NodeStatus.FAILED
            node.error = str(e)
            node.completed_at = datetime.now()
            
            print(f"   ❌ {node.name} failed: {e}")
            self.context.log_execution(node.name, "failed", str(e))
            raise
    
    def _prepare_node_input(self, node: DAGNode) -> Any:
        """Prepare input data for node based on dependencies"""
        # For parser, use initial data
        if node.name == "parser":
            return self.context.get("initial_data")
        
        # For question_generator, need ProductData object
        if node.name == "question_generator":
            if self.context.has("parser"):
                return self.context.get("parser")  # Return ProductData directly
            else:
                raise Exception("Parser output not available for question_generator")
        
        # For content_blocks, need ProductData object
        if node.name == "content_blocks":
            if self.context.has("parser"):
                return self.context.get("parser")  # Return ProductData directly
            else:
                raise Exception("Parser output not available for content_blocks")
        
        # For template nodes, prepare structured data
        if "template" in node.name:
            return self._prepare_template_data(node)
        
        # Default: return context data
        return self.context.data
    
    def _prepare_template_data(self, node: DAGNode) -> Dict[str, Any]:
        """Prepare data for template nodes"""
        data = {}
        
        # Get product info from parser
        if self.context.has("parser"):
            product = self.context.get("parser")  # ProductData object
            data["product_info"] = {
                "name": product.name,
                "concentration": product.concentration,
                "skin_type": product.skin_type,
                "price": product.price
            }
            data["product_a"] = data["product_info"].copy()
        
        # Add questions if available
        if self.context.has("question_generator"):
            questions = self.context.get("question_generator")  # List[FAQItem]
            data["questions"] = [q.model_dump() for q in questions]
        
        # Add content blocks if available
        if self.context.has("content_blocks"):
            data["content_blocks"] = self.context.get("content_blocks")
        
        return data
    
    def _generate_final_outputs(self) -> Dict[str, Any]:
        """Generate final JSON outputs from templates"""
        outputs = {}
        
        # Get template outputs
        if self.context.has("faq_template"):
            outputs["faq"] = self.context.get("faq_template")
        
        if self.context.has("product_template"):
            outputs["product_page"] = self.context.get("product_template")
        
        if self.context.has("comparison_template"):
            outputs["comparison_page"] = self.context.get("comparison_template")
        
        # Add workflow metadata
        outputs["metadata"] = {
            "workflow_completed": True,
            "total_nodes": len(self.nodes),
            "successful_nodes": len([n for n in self.nodes.values() if n.status == NodeStatus.COMPLETED]),
            "execution_summary": self.context.get_summary()
        }
        
        return outputs
    
    def get_status_report(self) -> Dict[str, Any]:
        """Get detailed status report of all nodes"""
        report = {
            "total_nodes": len(self.nodes),
            "execution_order": self.execution_order,
            "nodes": {name: node.to_dict() for name, node in self.nodes.items()},
            "context_summary": self.context.get_summary() if self.context else {}
        }
        return report