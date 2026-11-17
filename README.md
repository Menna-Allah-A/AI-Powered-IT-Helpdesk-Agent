# AI-Powered-IT-Helpdesk-Agent
# AI Agents – Session 1 Deliverable

**1. Use Case: AI-Powered IT Helpdesk Agent**

An agent that understands employees' IT problems, searches for solutions, creates support tickets, and checks ticket status.


**2. LLM & Provider**
- Provider: GroqCloud
- Model: GPT-OSS 120B

**3. Agent Tools**

**Tool 1: `search_knowledge_base`**
- Description: Searches internal IT documentation.
- Inputs: `query` (string), `category` (string).
- Outputs: `found` (boolean), `results` (array).

**Tool 2: `create_support_ticket`**
- Description: Creates tickets for unresolved issues.
- Inputs: `employee_id` (string), `issue_description` (string), `priority` (string), `category` (string).
- Outputs: `ticket_id` (string), `status` (string), `success` (boolean).

**Tool 3: `get_ticket_status`**
- Description: Retrieves existing ticket information.
- Inputs: `ticket_id` (string).
- Outputs: `status` (string), `assigned_to` (string), `last_updated` (string).


**4. System Prompt**

Defines the agent's role, objective, available tools, instructions, and response format.

It instructs the agent to understand requests, select appropriate tools, provide troubleshooting steps, escalate unresolved issues, and avoid inventing results.

**Expected Outcome:** An AI agent capable of automating IT support interactions using an LLM, external tools, and a system prompt.
