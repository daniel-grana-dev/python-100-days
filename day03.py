# Day 03 - if/elif/else control flow
# Project: Nexus - Self-hosted AI Inference Platform
 
# BASIC IF/ELIF/ELSE 
temperature = 20
 
if temperature > 30:
    print("Hot day")
elif temperature > 20:
    print("Nice day")   
elif temperature > 10:
    print("Cool day")   # This will print but my spanish side says 20 is cold
else:
    print("Cold day")
 
# COMPARISON OPERATORS 
x = 10
print(x == 10)   # True  (equal)
print(x != 5)    # True  (not equal)
print(x > 8)     # True  (greater than)
print(x <= 10)   # True  (less than or equal)
 
# LOGICAL OPERATORS 
is_sensitive = True
has_long_query = False
 
print(is_sensitive and has_long_query)   # False (both must be True)
print(is_sensitive or has_long_query)    # True  (at least one True)
print(not is_sensitive)                  # False (inverts)
 
# PRACTICAL EXAMPLE - ROUTING LOGIC 
# This is similar to what decide_model() does
query_length = 1500
is_private = False
 
if is_private:
    model = "ollama"
    reason = "privacy"
elif query_length > 2000:
    model = "openai"
    reason = "long query"
else:
    model = "openai"
    reason = "default"
 
print(f"Model: {model} | Reason: {reason}")
