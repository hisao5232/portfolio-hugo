import feedparser
import requests
import os
from datetime import datetime

# -------------------------
# 設定項目：ここだけ変更してOK
# -------------------------
ZENN_FEED_URL = "https://zenn.dev/hisao5232/feed"
GITHUB_USERNAME = "hisao5232"
ZENN_OUTPUT = "content/zenn/_index.md"
GITHUB_OUTPUT = "content/github/_index.md"
# -------------------------


# ============== Zenn記事一覧を取得 ==============
def fetch_zenn_articles():
    feed = feedparser.parse(ZENN_FEED_URL)
    items = feed.entries

    md = "# 📘 Zenn Articles\n\n最新の記事一覧です。\n\n"

    for item in items:
        title = item.title
        url = item.link
        date = item.published[:10]

        md += f"- [{title}]({url}) ({date})\n"

    return md


# ============== GitHubリポジトリ一覧を取得 ==============
def fetch_github_repos():
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
    repos = requests.get(url).json()

    md = "# 💻 GitHub Repositories\n\n公開リポジトリ一覧です。\n\n"

    for repo in repos:
        name = repo["name"]
        desc = repo["description"] or "説明なし"
        html_url = repo["html_url"]
        stars = repo["stargazers_count"]

        md += f"## [{name}]({html_url})\n"
        md += f"- ⭐ Stars: {stars}\n"
        md += f"- 📝 {desc}\n\n"

    return md


# ============== 書き込み処理 ==============
def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


# ============== メイン処理 ==============
if __name__ == "__main__":
    print("Zenn 記事を取得中...")
    zenn_md = fetch_zenn_articles()
    write_file(ZENN_OUTPUT, zenn_md)

    print("GitHub リポジトリを取得中...")
    github_md = fetch_github_repos()
    write_file(GITHUB_OUTPUT, github_md)

    print("更新完了！")
