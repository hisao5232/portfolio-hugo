import feedparser
import os

# -------------------------
# 設定項目：ここだけ変更すればOK
# -------------------------
ZENN_FEED_URL = "https://zenn.dev/hisao5232/feed"
ZENN_OUTPUT = "content/zenn/_index.md"
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


# ============== Markdown 書き込み処理 ==============
def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


# ============== メイン処理 ==============
if __name__ == "__main__":
    print("Zenn 記事を取得中...")
    zenn_md = fetch_zenn_articles()
    write_file(Z_
