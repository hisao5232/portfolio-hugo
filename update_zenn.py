import feedparser
from datetime import datetime

# ZennユーザーのRSS URL
ZENN_FEED = "https://zenn.dev/hisao5232/feed"

# Hugoで表示するMarkdownファイルのパス
OUTPUT_MD = "content/zenn/_index.md"

# RSSを取得
feed = feedparser.parse(ZENN_FEED)

# Markdownを書き出す
with open(OUTPUT_MD, "w", encoding="utf-8") as f:
    f.write("---\ntitle: 'Zenn 記事一覧'\n---\n\n")
    f.write("最新のZenn記事です。\n\n")
    for entry in feed.entries[:10]:  # 最新10件だけ表示
        date = datetime(*entry.published_parsed[:6]).strftime("%Y-%m-%d")
        f.write(f"- [{entry.title}]({entry.link}) ({date})\n")

print(f"✅ Zenn記事を {OUTPUT_MD} に書き出しました。")
