openai.api_key = "AIzaSyBDuRoIuRmYgrcfg2vazG_V8xvIK1VIPOM"

prompt = f"""
Explain the following code error in simple English for a beginner.
Also suggest how to fix it.

Code:
{code}

Error:
{error}
"""

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)

st.write(response["choices"][0]["message"]["content"])
