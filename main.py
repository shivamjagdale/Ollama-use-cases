# Using ollama with python

import ollama

response = ollama.chat(model="gemma:2b",
                       messages=[{"role":"system", "content":"You are an helpful AI Assistant"},
                                 {"role":"user", "content":"What is Machine Learning?"},

                                 {"role":"assistant", "content":"Machine learning is a subset of Artifical Intelligence"},

                                 {"role":"user", "content":"Why is the sky blue?"}])
print(response["message"]["content"])