# Day 04 - Lists
# Project: Nexus - Self-hosted AI Inference Platform
 
# CREATE AND ACCESS LISTS 
models = ["ollama", "openai", "anthropic"]
 
print(models[0])    # ollama  (first element, index 0)
print(models[-1])   # anthropic  (last element)
print(len(models))  # 3
 
# MODIFY LISTS 
models.append("gemini")         # add at end
print(models)  # ["ollama", "openai", "anthropic", "gemini"]
 
models.remove("anthropic")      # remove by value
print(models)  # ["ollama", "openai", "gemini"]
 
models.insert(1, "claude")      # insert at position 1
print(models)  # ["ollama", "claude", "openai", "gemini"]
 
# CHECK IF ELEMENT IS IN LIST 
print("ollama" in models)   # True
print("gpt-4" in models)    # False
 
# ITERATE 
print("\nAll available models:")
for model in models:
    print(f"  - {model}")
 
# PRACTICAL EXAMPLE - SENSITIVE KEYWORDS 
# A list of keywords that trigger privacy routing
sensitive_keywords = ["password", "token", "secret", "api_key", "credit_card", "dni", "ssn", "potato"]
 
test_queries = [
    "My dog didn't let me sleep today at all, intravenous coffee please",
    "My password is abc123",
    "Explain how RAG works",
    "My api_key is sk-proj-123",
]
 
for query in test_queries:
    query_lower = query.lower()  # always compare in lowercase
    is_sensitive = False
 
    for keyword in sensitive_keywords:
        if keyword in query_lower:
            is_sensitive = True
            break  # no need to check more keywords
 
    model = "ollama" if is_sensitive else "openai"
    print(f"Query: {query} | Sensitive: {is_sensitive} | Model: {model}")
