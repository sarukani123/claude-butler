# Claude Butler（専属バトラー）

Claude Code を「専属バトラー」にするプラグインです。
セッション、PC、モデルが変わっても、それまでの経緯を覚えたまま続きから相談できるようにします。

解説記事：[Claude Code に、経緯を覚えている「専属バトラー」を作る（Zenn）](https://zenn.dev/sarukani/articles/claude-code-butler-memory)

## 導入（3 ステップ）

```bash
# 1. プラグインを入れる（1 回だけ）
claude plugin install butler --marketplace sarukani123/claude-butler

# 2. 記録用の空のフォルダを作り、そこで Claude Code を開く
mkdir my-butler && cd my-butler && claude

# 3. Claude Code の中で
/butler:init
```

- Claude Code のセッション内からは `/plugin install butler --marketplace sarukani123/claude-butler` でも入れられます。
- 上のコマンドが使えない版では、`claude plugin marketplace add sarukani123/claude-butler` のあとに `claude plugin install butler@sarukani` を実行してください。
- `/butler:init` は 3 つだけ質問します（話す言語・主な用途・Git で同期するか）。終わったら「はじめまして。バトラーとしてよろしく」など、普段どおりに話しかけてください。

## できること
- **経緯を引き継ぐ**：Claude がセッションを始めるときに記録を読み、終わるときに書き足します。あなたが記録を頼む必要はありません。
- **あなた待ちを覚えておく**：確認や判断をお願いしたことを `waiting-on-you.md` に残し、関係する話題になったときにそっと思い出させます。
- **記憶を整理する**：`/butler:tidy` で、片付いた項目・食い違い・古い記録の整理**案**を作ります。記録はあなたが承認するまで書き換えません。
- **別の PC やクラウドでも続けられる**：記録はフォルダ内のファイルなので、Git で同期すればどこでも同じ記録を使えます。
- **Git に上げたくない情報を分けられる**：`private/` は Git の管理外です。
- **重い作業は専門エージェントに任せる**：バトラーは中継に専念します。雛形（`templates/specialist-agent.md`）付き。

## スキル
| スキル | 内容 |
|---|---|
| `/butler:init` | 今のフォルダに、バトラーのルール（`CLAUDE.md`）と記録ファイル一式を作る。既に記録があるフォルダでは何もしない |
| `/butler:tidy` | 記録を見直し、整理の案を `tidy/` に書く（記録そのものは書き換えない） |

## 作られるファイル
| ファイル | 内容 |
|---|---|
| `CLAUDE.md` | バトラーの役割と、記録・同期・委任のルール（Claude Code が毎回自動で読み込む。自由に直せます） |
| `profile.md` | あなたについて分かったこと（環境・好み・関心） |
| `waiting-on-you.md` | バトラーがあなたの確認・判断・操作を待っているもの |
| `open-items.md` | バトラー側で進めている作業・結果待ち |
| `journal/` | 日ごとのやりとりの要点 |
| `knowledge/` | 調べて答えた内容（テーマ別・確認日付き） |
| `projects.md` | 専門エージェントや別プロジェクトに任せている案件の一覧 |
| `templates/specialist-agent.md` | 専門エージェントの雛形 |
| `.gitignore` | `private/` などを Git に上げない設定 |

ルールはあなたのフォルダの `CLAUDE.md` にあるので、プラグインを外しても記録とバトラーはそのまま使えます。

## プライバシー
- このプラグインは、記録をどこにも送りません。記録はあなたのフォルダの中だけにあり、読むのはあなたの Claude Code のセッションだけです。
- 利用状況を集める仕組みは入っていません。
- 記録には会話の内容が残ります。Git のリモートを付けるときは、必ず**非公開**のリポジトリにしてください。
- パスワードや API キーなどの秘密情報は、記録に書かないでください。

## 更新
自前のマーケットプレイスは、自動更新が既定で OFF です。新しい版を取り込むには：

```bash
claude plugin update butler@sarukani
```

`/plugin` の画面で、このマーケットプレイスの自動更新を ON にすることもできます。更新で変わるのはスキルと雛形だけで、あなたのフォルダの `CLAUDE.md` や記録は変わりません。

## リポジトリから始めたい人へ
プラグインを使わずに、GitHub の雛形リポジトリから始めることもできます：[claude-butler-template](https://github.com/sarukani123/claude-butler-template)

## ライセンス
MIT

---

## English summary

**Claude Butler** turns Claude Code into a personal butler that remembers your history across sessions, machines, and models.

- Install: `claude plugin install butler --marketplace sarukani123/claude-butler`
- In an empty folder, run `/butler:init`. It asks three questions (language, main use, whether to sync with Git) and writes a `CLAUDE.md` plus plain Markdown memory files (`profile.md`, `waiting-on-you.md`, `open-items.md`, `journal/`, `knowledge/`, `projects.md`). Claude reads them at the start of each session and appends to them as you talk.
- `/butler:tidy` reviews the records and writes a cleanup *proposal* to `tidy/`; nothing is changed until you approve.
- Everything stays in your folder. The plugin sends nothing anywhere and collects no usage data. If you sync with Git, use a **private** repository.
- The generated files are in Japanese by default; choose another language during `/butler:init` and they are written in that language.

License: MIT
