import json
import time
import random

def call_api(prompt, options, context):
    prompt_lower = prompt.lower()
    
    # 1. SIMULATE LATENCY
    time.sleep(random.uniform(0.1, 0.4))

    # SCENARIO A: JSON Request
    if "json" in prompt_lower or "transfer" in prompt_lower:
        intent = "transfer" if "transfer" in prompt_lower else "check_balance"
        return {
            "output": json.dumps({
                "intent": intent,
                "account_type": "savings",
                "confidence": 0.98
            })
        }

    # SCENARIO B: Harmful Requests (expanded list)
    harmful_keywords = ["steal", "hack", "fraud", "phish", "illegal"]
    if any(keyword in prompt_lower for keyword in harmful_keywords):
        return {
            "output": "I cannot assist with illegal activities. I am a banking assistant."
        }

    # SCENARIO C: Educational/Fact Requests
    if "tfsa" in prompt_lower:
        if "rrsp" in prompt_lower:
            return {
                "output": "A TFSA has tax-free growth while an RRSP provides tax deductions on contributions."
            }
        return {
            "output": "A TFSA (Tax-Free Savings Account) allows Canadians to earn tax-free investment income."
        }

    # SCENARIO D: Account Help
    if "password" in prompt_lower or "reset" in prompt_lower:
        return {
            "output": "Contact customer support or use the password reset link on our login page."
        }

    # FALLBACK
    return { "output": "I am a banking assistant. How can I help?" }