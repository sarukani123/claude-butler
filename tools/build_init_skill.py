"""skills/init/SKILL.md を tools/init-skill.src.md と templates/ から生成する。

templates/ を直したら、このスクリプトを実行して SKILL.md を作り直す：
    python tools/build_init_skill.py          # 生成
    python tools/build_init_skill.py --check  # 生成物が最新かだけ確かめる（最新でなければ exit 1）

雛形をスキル本文に埋め込む理由：プラグインのフォルダのファイルを Read すると、
利用者に読み取りの許可を求める確認が出る（2026-11-05 の試験で確認）。
本文に入れておけば、許可の追加（allowed-tools）なしで雛形を渡せる。
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "tools" / "init-skill.src.md"
OUT = ROOT / "skills" / "init" / "SKILL.md"

# (雛形のファイル, 利用者のフォルダでの書き先)
FILES = [
    ("CLAUDE.md", "CLAUDE.md"),
    ("profile.md", "profile.md"),
    ("waiting-on-you.md", "waiting-on-you.md"),
    ("open-items.md", "open-items.md"),
    ("projects.md", "projects.md"),
    ("journal/README.md", "journal/README.md"),
    ("knowledge/README.md", "knowledge/README.md"),
    ("specialist-agent.md", "templates/specialist-agent.md"),
    ("gitignore", ".gitignore"),
    ("gitattributes", ".gitattributes"),
]

FORBIDDEN = ("~~~~", "$", "!`")  # 囲みの区切りと、スキルの置換に当たる文字


def build() -> str:
    parts = []
    for src, dest in FILES:
        text = (ROOT / "templates" / src).read_text(encoding="utf-8").replace("\r\n", "\n")
        for bad in FORBIDDEN:
            if bad in text:
                sys.exit(f"templates/{src} に使えない文字列 {bad!r} がある")
        parts.append(f"### 書き先：`{dest}`\n\n~~~~markdown\n{text.rstrip()}\n~~~~\n")
    src_text = SRC.read_text(encoding="utf-8").replace("\r\n", "\n")
    return src_text.replace("{{TEMPLATES}}", "\n".join(parts))


def main() -> None:
    out = build()
    if "--check" in sys.argv:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if current != out:
            sys.exit("skills/init/SKILL.md が templates/ と食い違っている。build_init_skill.py を実行する")
        print("ok")
        return
    OUT.write_bytes(out.encode("utf-8"))
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
