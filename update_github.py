import requests
import os

USERNAME = "hisao5232"
OUTPUT_FILE = "content/repos/_index.md"

API_URL = f"https://api.github.com/users/{USERNAME}/repos"

def fetch_repos():
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()

def generate_markdown(repos):
    md = "---\n"
    md += 'title: "GitHub リポジトリ"\n'
    md += "---\n\n"
    md += "こちらは自動取得している GitHub リポジトリ一覧です。\n\n"
    md += "（この下は update_github.py により自動更新されます）\n\n"

    for repo in repos:
        name = repo.get("name")
        desc = repo.get("description") or "（説明なし）"
        url = repo.get("html_url")

        md += f"## [{name}]({url})\n"
        md += f"{desc}\n\n"

    return md

def main():
    repos = fetch_repos()
    md = generate_markdown(repos)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(md)

    print("GitHub リポジトリ一覧を更新しました！")

if __name__ == "__main__":
    main()
