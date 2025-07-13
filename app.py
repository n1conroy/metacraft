# app.py
# CLI entry point for quick testing.

from agent_orchestrator import AgentOrchestrator

if __name__ == "__main__":
    request = input("Enter a natural language schema request: ")
    orchestrator = AgentOrchestrator()
    schema = orchestrator.handle_request(request)
    print("\nGenerated Fields:")
    for f in schema:
        print(f"- {f['name']} ({f['type']})")
