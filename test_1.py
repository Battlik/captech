import json
with open("name.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def parse(response: dict) -> list[str]:
    return [p["login"] for p in response.get("people", {}).get("result", []) if p.get("login")]

print(parse(data))