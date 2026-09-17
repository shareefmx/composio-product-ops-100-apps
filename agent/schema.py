"""
Data models for the Composio AI Product Ops 100-App Research Agent.
"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class AppResearchRecord(BaseModel):
    id: int
    name: str
    category: str
    website_hint: str
    one_liner: str
    auth_methods: List[str]
    primary_auth: str
    access_model: str  # 'Self-Serve Free', 'Self-Serve Paid', 'Admin-Approval', 'Partner-Gated', 'No Public API'
    access_details: str
    api_surface: str  # 'REST', 'GraphQL', 'REST + GraphQL', 'CLI / Local', 'gRPC / SDK', 'None'
    api_breadth: str  # 'Broad (>50 endpoints)', 'Moderate (10-50 endpoints)', 'Narrow (<10 endpoints)', 'None'
    mcp_status: str  # 'Official MCP', 'Community MCP', 'Composio Native', 'None'
    buildability_verdict: str  # 'Ready Today', 'Feasible with Auth Setup', 'High Friction', 'Blocked'
    main_blocker: str
    priority_quadrant: str  # 'Quick Win (Instant Toolkit)', 'Core Enterprise Bet', 'Strategic Outreach', 'Alternative / CLI'
    evidence_url: str
    pass1_confidence: float = 0.85
    verification_notes: Optional[str] = None


class VerificationAuditItem(BaseModel):
    app_id: int
    app_name: str
    category: str
    pass1_claim: Dict[str, Any]
    pass2_finding: Dict[str, Any]
    discrepancy_type: str  # 'Auth Misclassification', 'Gating Overoptimism', 'API Breadth Misestimate', 'MCP Miss', 'Correct'
    status: str  # 'Corrected in Pass 2', 'Verified Correct', 'Human Intervention Needed'
    root_cause_explanation: str
    evidence_url: str


class PatternSummary(BaseModel):
    total_apps: int = 100
    auth_distribution: Dict[str, int]
    access_distribution: Dict[str, int]
    buildability_distribution: Dict[str, int]
    mcp_distribution: Dict[str, int]
    priority_distribution: Dict[str, int]
    category_insights: Dict[str, Dict[str, Any]]
    top_blockers: List[Dict[str, Any]]
    verification_metrics: Dict[str, Any]

