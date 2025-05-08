# CodeAgents: AI That Doesn't Just Talk, It Does

## Key points:
- LLMs are known to produce text and code. But while they can produce code, they can't use coding to improve or validate their own answers
- CodeAgents allow LLMs to write and execute code to solve tasks. This allows LLMs more autonomy to create complex tasks
- This great potential also has new security implications. If an LLM is allowed to write code, what if it produces and runs malicious code. Restricting package access and system calls helps create secure sandbox environments for the LLM

## Learnings:
- What are CodeAgents and why are they useful
- What kinds of problems can they solve that other agents struggle with
- How can you implement them in a secure way

## Outline
1. Introduction (3 minutes)
    - Brief introduction and session objectives
    - GenAI from simple prompts to agentic workflows (quick and simple)

2. Understanding Code Agents (5 minutes)
    - Limitation of traditional Agents
    - Definition and characteristics of code agents
    - Why generating code can be superior to generating JSON

<!-- 3. Code Agent Architecture/Flow (15 minutes)
    - Core components of effective code agents
    - Tool integration framework for repository interaction
    - Memory and context management for complex codebases
    - The five essential programming tools (from CodeAgent research):
        - Information retrieval tools
        - Documentation reading tools
        - Code symbol navigation
        - Format checking
        - Code interpretation and testing -->

4. Implementation with smolagents (5 minutes)
    - Introduction to the smolagents framework
    <!-- - Building a repository-aware code agent using smolagents -->
    - Demo: Implementing the five essential tools within smolagents
    - Code walkthrough of a complete agent implementation

5. Security considerations (5 minutes)
    - Model security applies
    - Code Execution environment
    - Dependency Management
    - Secure handling of execution feedback

6. Conclusion (2 minutes)
   - Key takeaways