# 企画書 v0.4：Settings as Play Protocol

> Publication note: この文書は SaPP v0.4 の元企画書です。現在のリポジトリ実体では、法的ライセンスを CC BY 4.0、文化的作法を SaPP Commons Agreement として分離しています。テンプレートは、SaPP 利用者に特定ライセンスを強制しない形へ調整されています。

**日本語仮称：設定で遊ぶプロトコル**
**略称候補：SaPP / SAPP**
**旧仮称・通称候補：設定コモンズ / Settings as Play / 遊び方コモンズ**
**Version:** v0.4
**作成日:** 2026-05-07
**位置づけ:** 公開提言 / RFC / 実験リポジトリ案
**ステータス:** 名称・テンプレート・運用形式は変更可能
**前提:** 新規プラットフォーム事業ではなく、まずは「設定・文脈を共有するための軽量プロトコル」の提案として公開する。

---

## 0. v0.4での主な変更点

v0.3では、Settings as Play Protocolを創作・エンタメから教育・仕事・研究・コミュニティまで広げて整理した。
ただし、公開文としては射程が広がりすぎると、読む人に「結局なにをするものなのか」が伝わりにくくなる。

v0.4では、次のように整理し直す。

### v0.4の方針

- 入口は **AI創作・画像生成・キャラクター設定・世界観づくり** に絞る。
- ただし、企画の芯は **設定・文脈・由来・派生を扱う情報構造** として設計する。
- SaPP本体は巨大な仕様にせず、**SaPP Core** として最小項目に絞る。
- ゲーム、映画、教育、仕事、研究などは、SaPP Coreに足す **Optional Modules** として扱う。
- 「Play」は娯楽だけでなく、試す、演じる、動かす、変奏する、シミュレーションする、という広い意味を含める。
- 将来的には、`Settings as Game Protocol`、`Settings as Film Protocol`、`Settings as Learning Protocol` のように、Playの部分を差し替えた派生も可能とする。
- 葉桜環界譚は、全設定を開放するのではなく、SaPP Core + Optional Module の **サンプル実装** として一部を切り出す。
- GitHubは「原本・系譜・ルール置き場」として使い、noteやSNSを「発信・参加入口」として使う。
- プラットフォーム化は長期の可能性に留め、初期は **プロトコル提言 + テンプレート + 実例** に集中する。

### v0.4の一文

> **Platformではなく、Protocol。**
> 完成品ではなく、派生可能な「設定の芯」を共有する。

### v0.4のもう一つの一文

> SaPPは、作品やサービスを作る前の「設定の芯」を、軽く共有・派生・移植するための形式である。

---

## 1. この文書の目的

AI画像生成やAI創作をしていると、完成した画像や文章だけでなく、その背後にある **設定そのもの** が楽しくなることがある。

たとえば、ただの「猫耳の女の子」ではなく、

> 朝は寝ぼけていて、夜は活動的になる猫耳ちゃん

という設定があるだけで、連続生成、日課、派生、物語化、アーカイブ化が起きる。

ここで面白いのは、完成画像だけではない。
その画像を生む **遊び方、ルール、文脈、変化の余地** である。

本企画の目的は、すぐに新しい投稿サイトを作ることではない。
まずは、AI創作時代において、設定や遊び方をどう共有し、どう派生させ、どう由来を残すかを言語化する。

そのために、以下を公開する。

1. **マニフェスト**：設定で遊ぶ文化の考え方
2. **SaPP Core**：設定の芯を共有するための最小フォーマット
3. **Optional Modules**：画像生成、物語、ゲーム、映画など用途別の追加項目
4. **Derivation Card**：派生元・変えたところ・残したところを記録する形式
5. **Credit Block**：由来や作者を軽く残す形式
6. **Commons Agreement**：改変・派生・クレジットの文化的作法
7. **葉桜環界譚のサンプル設定**：実際の世界観から切り出した実例
8. **ロードマップ**：初動、短期、中期、長期の進め方
9. **周辺調査**：pixiv、GitHub、プロンプト市場、AIモデル共有サービスなどとの関係整理

これは「場所」を作る前に、「作法」を作る企画である。

---

## 2. エグゼクティブサマリー

### 2.1 コンセプト

> **設定は売り切るものではなく、蒔いて育てるもの。**

Settings as Play Protocolは、キャラクター設定、世界観、プロンプト、生成手順、遊び方を、閉じた資産ではなく、**派生可能な“種”** として共有するための小さなプロトコルである。

ただし、v0.4ではこれをさらに整理する。

> SaPPは、設定を「そのまま使う素材」ではなく、別の遊び・媒体・企画へ移植できる **設定の芯** として記述する。

完成画像や完成作品を投稿するだけではなく、次の情報を残す。

- これは何の設定なのか
- 何を感じる / 試す / 起こすための設定なのか
- どんな文脈で成立するのか
- どこを守るとその設定らしくなるのか
- どこを自由に変えてよいのか
- 何から派生したのか
- 誰に由来するのか

### 2.2 これは何ではないか

これは、初期段階では以下ではない。

- 新しい投稿サイト
- 画像ギャラリー
- プロンプト販売サービス
- 設定販売マーケット
- 大規模コミュニティ運営
- すべての設定を無条件に自由素材化する運動
- 法的ライセンスの代替
- 医療・法務・金融など高リスク判断の代替手段

### 2.3 これは何か

これは以下である。

- AI創作時代の「設定で遊ぶ文化」への提言
- 設定や遊び方を共有するための軽量テンプレート
- 派生元と由来を残すための作法
- 既存プラットフォームにも載せられるプロトコル
- 葉桜環界譚を使った小さな実験
- 将来、ゲーム・映画・教育・仕事などへ派生できる情報構造のたたき台
- 誰かがより良い実装を作るための公開RFC

### 2.4 最初のゴール

初期のゴールは、ユーザー数や収益ではない。

最初のゴールは、次の問いに答えることである。

> SaPP Core、派生カード、クレジット作法、派生マップという最小形式だけで、どれくらい「設定で遊ぶ / 受け渡す / 別媒体へ移植する」ことができるのか。

---

## 3. 背景と問題意識

### 3.1 完成物より「遊び方」が価値を持つ

AI画像生成では、1枚の絵を作るコストが下がる。結果として、完成画像単体の希少性は下がりやすい。

一方で、次のようなものは価値を持ち続ける。

- どんな設定で遊ぶか
- どんな変化ルールを持たせるか
- どんなキャラクター性を継続させるか
- どんな世界観の中で生成するか
- どんなプロンプトやワークフローで再現するか
- どんな派生が起きたか
- 誰がどう遊んだか

ここで価値を持つのは、画像単体ではなく、**画像を生む遊び方** である。

### 3.2 「設定を売る」の限界

設定やプロンプトを売る動きは短期的には自然であり、否定する必要はない。

ただし、設定そのものを売るモデルには限界がある。

- 似た設定は簡単に作れる
- 設定の魅力は「使われ方」「派生のされ方」に依存する
- モデル更新や流行変化でプロンプトの価値は変動する
- 売買だけに寄せると、共有や派生が萎縮する
- 囲い込みが強いほど、文化ではなく市場になりやすい

このため、短期的には先行公開、有料解説、編集版設定集などがあってもよい。
しかし長期的には、設定は独占資産ではなく、**共有される遊びの種** として扱う方が強い。

### 3.3 独占プラットフォームへの違和感

この領域は、短期的には「独占プラットフォームを作って、人を集めて、お金にする」という発想になりがちである。

しかし、この企画の本質はそこではない。

もし設定で遊ぶ文化が本当に重要なら、それは一社・一個人・一サービスに閉じるより、さまざまな場所で使える **横断プロトコル** になった方がよい。

つまり、理想はこうである。

> みんなが同じ場所に集まる必要はない。
> でも、どこで遊んでも「派生元」「設定カード」「共有作法」が残る。

### 3.4 エンタメから始めるが、エンタメに閉じない

この提言は、最初はAI創作・キャラクター・世界観・画像生成から始める。
その方が具体的で、直感的で、参加しやすいからである。

ただし、SaPPの芯はエンタメ専用ではない。

ゲームを作るときも、映画を作るときも、教育ワークショップを作るときも、仕事のプロジェクトを設計するときも、最初に必要なのはしばしば次の情報である。

- 何の話か
- どんな文脈か
- 何を守るとそれらしくなるか
- どこを変えてよいか
- 何から派生したか
- 誰に由来するか

これはSaPP Coreそのものである。

つまり、入口は創作でよい。
しかし、設計としては他領域にも移植できるようにしておく。

---

## 4. Settings as Play Protocolとは何か

### 4.1 プロトコルの定義

ここでいうプロトコルとは、通信規格のような厳密な技術仕様ではない。

設定を共有し、派生し、継承するための **最小限の作法・テンプレート・記録形式** のことである。

Settings as Play Protocolは、次の要素で構成される。

1. **SaPP Core**
   設定の芯を記述する最小フォーマット。

2. **Optional Modules**
   画像生成、キャラクター、世界観、物語、ゲーム、映画、教育、仕事など用途別の追加項目。

3. **Derivation Card / 派生カード**
   何を元に、どこを変え、どこを残したかを記録するカード。

4. **Credit Block / クレジット表記**
   元設定名、作者、派生元リンク、利用条件を簡潔に残す形式。

5. **Derivation Map / 派生マップ**
   設定がどこからどこへ広がったかを見える化する系譜図。

6. **Commons Agreement / 共有合意文**
   改変・再解釈・派生を歓迎しつつ、由来を残すための文化的合意文。

7. **Repository / 原本置き場**
   GitHubなどに、マニフェスト、テンプレート、サンプル、派生マップを置く。

### 4.2 なぜ「Protocol」なのか

「Platform」は場所を作る言葉である。
そこには、人を集める、投稿を管理する、利用規約を整える、モデレーションする、収益化する、という運営責任が伴う。

一方で、「Protocol」は作法を作る言葉である。
どの場所でも使える形式、由来の残し方、派生の記録方法を定義する。

本企画では、初期段階でプラットフォームを作らない。
代わりに、既存の場所でも、新しい場所でも、個人の小さなコミュニティでも使える **共通言語** を作る。

### 4.3 なぜ「Play」なのか

ここでいうPlayは、単なる娯楽を意味しない。

Playには、次のニュアンスを含める。

- 遊ぶ
- 試す
- 演じる
- 動かす
- 変奏する
- シミュレーションする
- 参加する
- 別の文脈へ移植する

そのため、Settings as Play Protocolは最初は「創作・遊び」のプロトコルとして始めるが、将来的にはPlayの部分を用途に応じて読み替えることもできる。

例：

- Settings as Game Protocol
- Settings as Film Protocol
- Settings as Learning Protocol
- Settings as Workshop Protocol
- Settings as Simulation Protocol
- Settings as Project Protocol

ただし、初期公開では名称を増やしすぎない。
本体は **Settings as Play Protocol** とし、派生可能性として `Settings as X Protocol` を許容する。

---

## 5. SaPP Core

### 5.1 SaPP Coreの考え方

SaPPは、すべての用途を一つの巨大なテンプレートに詰め込むことを目指さない。

中心に置くのは、設定を共有・派生・継承するための最小フォーマットである。

これを **SaPP Core** と呼ぶ。

SaPP Coreは、設定の「完成資料」ではない。
他の人が受け取り、変え、別の媒体へ移植できる **設定の芯** である。

### 5.2 SaPP Core v0.4

SaPP Coreは、原則として次の7項目に絞る。

```md
# SaPP Core

## 1. Name
設定名

## 2. One-liner
一言でいうと

## 3. Intent
この設定で何を起こしたいか / 何を感じてほしいか / 何を試したいか

## 4. Context
前提・世界・状況・関係性

## 5. Core Rules
守るとその設定らしさが残るルール

## 6. Variables
変えてよいところ / 派生しやすいところ

## 7. Derivation & Credit
派生元・作者・リンク・利用条件
```

この7項目を埋めれば、まずはSaPPとして成立する。

すべてを完璧に書く必要はない。
空欄があってもよい。
雑でもよい。
あとから育ててもよい。

SaPPは設定を固定するためではなく、派生しやすくするための最小メモである。

### 5.3 Core Rules と Variables の違い

SaPPで最も重要なのは、**Core Rules** と **Variables** の区別である。

#### Core Rules

Core Rulesは、変えると別物になってしまう芯である。

言い換えると、

> 変えないことで同一性を保つもの。

#### Variables

Variablesは、変えてもその設定らしさが残る余白である。

言い換えると、

> 変えることで派生を生むもの。

### 5.4 例：朝夜で変わる猫耳ちゃん

```md
# SaPP Core：朝夜で変わる猫耳ちゃん

## 1. Name
朝夜で変わる猫耳ちゃん

## 2. One-liner
朝は寝ぼけていて、夜は活動的になる猫耳キャラクター設定。

## 3. Intent
同じキャラクターが時間帯によって変化する楽しさを、画像生成や短い物語で遊ぶ。

## 4. Context
日常の中にいる猫耳キャラクター。朝・昼・夜の変化が、表情や服装や背景に現れる。

## 5. Core Rules
- 同じキャラクターであることがわかる
- 朝は眠そう、夜は活動的
- 耳や尻尾に時間帯の変化が出る
- 変化はかわいさや物語性につながる

## 6. Variables
- 服装
- 年齢感
- 背景
- 季節
- 口調
- 朝夜以外の時間帯
- 天気や曜日との組み合わせ

## 7. Derivation & Credit
元設定：朝夜で変わる猫耳ちゃん
派生歓迎：天気、曜日、月齢、感情、成長記録など
クレジット：元設定名と派生元リンクを可能な範囲で残す
```

### 5.5 例：葉桜環界譚 / 境界の街

この例は、葉桜環界譚の全設定を公開するものではない。
SaPPのサンプル実装として、一部の世界観要素を切り出す。

```md
# SaPP Core：葉桜環界譚 / 境界の街

## 1. Name
葉桜環界譚 / 境界の街

## 2. One-liner
春が終わった後も、葉桜だけが舞い続ける境界の街。

## 3. Intent
懐かしさ、喪失感、再会、異界感を、明るい風景の中に少しだけ混ぜる。

## 4. Context
現実の街と異界が重なっている。人々は気づかないまま境界を行き来している。葉桜は、その境界を示す象徴である。

## 5. Core Rules
- 桜ではなく葉桜が象徴である
- 明るさと寂しさが同居する
- 現実と異界の境界が曖昧である
- キャラクターは街に飲み込まれすぎず、少し距離を持つ

## 6. Variables
- 季節
- 時間帯
- 天気
- キャラクター
- 神社 / 駅 / 商店街 / 海辺などの舞台
- 画像生成、短編、ゲーム導入、映画風シーン、TRPG舞台などの媒体

## 7. Derivation & Credit
元設定：葉桜環界譚
公開範囲：このカードに書かれた範囲のみ派生歓迎
非公開範囲：物語の核心、重要キャラクターの結末、未公開固有名詞など
クレジット：元設定名と派生元リンクを可能な範囲で残す
```

---

## 6. Optional Modules

### 6.1 Optional Modulesの考え方

SaPP Coreだけで、多くの設定は共有できる。

しかし、用途によっては追加情報が必要になる。

たとえば、画像生成なら構図やプロンプトの注意が欲しい。
ゲームならプレイヤーの役割やループが欲しい。
映画ならテーマ、葛藤、キービジュアル、重要シーンが欲しい。

そこで、SaPPではCoreを太らせるのではなく、用途別の **Optional Modules** を付け足す。

```text
SaPP Core
├─ Character Module
├─ Worldbuilding Module
├─ Image Generation Module
├─ Story / Film Module
├─ Game Module
├─ Learning Module
├─ Project Module
└─ Workshop Module
```

SaPPは完成品の仕様書ではない。
異なる分野に移植できる「設定の芯」を扱い、用途別の詳細はモジュールに逃がす。

### 6.2 Character Module

```md
## Character Module

### Appearance
外見・服装・特徴

### Personality
性格・口調・反応

### Relationship
他者との関係性

### Change Pattern
変化のルール

### Do / Do Not
やってよい表現 / 避けたい表現
```

### 6.3 Worldbuilding Module

```md
## Worldbuilding Module

### Place
場所・地理・環境

### Era
時代・文明レベル

### Social Rules
社会のルール・常識

### Mystery
謎・隠された前提

### Symbols
象徴・モチーフ
```

### 6.4 Image Generation Module

```md
## Image Generation Module

### Visual Keywords
見た目のキーワード

### Composition
構図

### Mood
雰囲気

### Prompt Notes
プロンプト上の注意

### Negative Constraints
避けたい要素

### Example Prompts
作例プロンプト
```

### 6.5 Story / Film Module

```md
## Story / Film Module

### Theme
テーマ

### Protagonist
主人公

### Conflict
葛藤

### Visual Motif
映像モチーフ

### Key Scene
核になる場面

### Ending Direction
結末の方向性
```

### 6.6 Game Module

```md
## Game Module

### Player Role
プレイヤーは何者か

### Goal
何を達成するのか

### Mechanics
どんな操作・ルール・遊びがあるか

### Loop
繰り返し遊ぶ流れ

### Win / Lose / Change Conditions
成功・失敗・変化条件

### Progression
成長・解放・変化
```

### 6.7 Learning Module

初期公開では中心にしないが、将来的には教育・学習にも応用できる。

```md
## Learning Module

### Learner
誰が学ぶか

### Learning Goal
何を理解するか

### Activity
どう試すか

### Reflection
何を振り返るか

### Assessment
何ができれば成功か
```

### 6.8 Project Module

仕事や研究に使う場合の追加項目。初期公開では参考扱いにする。

```md
## Project Module

### Stakeholders
関係者

### Goal
目的

### Constraints
制約

### Decisions
決めること

### Open Questions
未解決の問い

### Next Actions
次の行動
```

---

## 7. SaPPのテンプレート

### 7.1 軽量版テンプレート

SNS、note、短い共有向け。

```md
# SaPP Core

## Name

## One-liner

## Intent

## Context

## Core Rules

## Variables

## Derivation & Credit
```

### 7.2 詳細版テンプレート

GitHub、アーカイブ、作品設定の継承向け。

```md
# SaPP Setting Card

## 1. Name

## 2. One-liner

## 3. Intent

## 4. Context

## 5. Core Rules

## 6. Variables

## 7. Derivation & Credit

---

## Optional Modules

### Character Module

### Worldbuilding Module

### Image Generation Module

### Story / Film Module

### Game Module

---

## Notes

### Safety / Limits

### Non-public Area

### Example Outputs

### Revision History
```

### 7.3 派生カードテンプレート

```md
# Derivation Card

## Derived From
派生元の設定名・リンク

## New Name
派生後の設定名

## What Changed
変えたところ

## What Stayed
残したところ

## New Variables
新しく増えた派生余地

## Credit
元設定・作者・リンク
```

### 7.4 クレジットブロックテンプレート

```md
## Credit

Based on: [元設定名](https://example.com/source)
Original by: 作者名
Derived by: 派生者名
Legal License / Permission: CC BY 4.0 / CC BY-NC 4.0 / All rights reserved / 個別許諾 / 未定 など
Cultural Agreement: SaPP Commons Agreement
Notes: 由来を可能な範囲で残してください
```

### 7.5 Commons Agreement 草案

```md
# SaPP Commons Agreement

この設定は、派生・改変・再解釈を歓迎します。
使うときは、可能な範囲で元設定名と派生元リンクを残してください。
あなたの派生も、また誰かの遊びの種になることを歓迎します。

ただし、すべての利用を無条件に許可するものではありません。
各設定カードに書かれた公開範囲、非公開範囲、ライセンス、注意事項を尊重してください。
```

---

## 8. 葉桜環界譚をどう混ぜるか

### 8.1 全開放ではなく、サンプル実装にする

葉桜環界譚は、Settings as Play Protocolの実験場として使える。

ただし、すべての設定を自由素材化する必要はない。

むしろ、次のように切り分ける。

```text
葉桜環界譚
├─ 公開サンプル：SaPP Coreとして切り出す設定
├─ 派生歓迎領域：画像生成・短編・ゲーム導入などに使ってよい要素
├─ 保留領域：今後の作品化や未公開設定のために残す要素
└─ 非公開領域：物語の核心、重要キャラクターの結末など
```

### 8.2 葉桜環界譚で試すこと

- SaPP Coreだけで世界観の魅力が伝わるか
- 画像生成モジュールを足すと作例が作りやすくなるか
- Story / Film Moduleを足すと短編や映像企画にしやすいか
- Game Moduleを足すと探索ADVやノベルゲームの種になるか
- 派生元と非公開範囲を明示することで、安心して共有できるか

### 8.3 例：葉桜環界譚 + Image Generation Module

```md
## Image Generation Module

### Visual Keywords
葉桜、境界の街、春の終わり、淡い光、少し寂しい通学路、現実と異界の重なり

### Composition
キャラクターは画面中央から少し外し、背景に葉桜と街の奥行きを見せる。

### Mood
明るいが、どこか取り残されたような静けさ。

### Prompt Notes
桜満開ではなく、葉桜を強調する。幻想的にしすぎず、日常の中に違和感を混ぜる。

### Negative Constraints
過度にホラーにしない。桜吹雪中心にしない。街を完全な異世界にしすぎない。
```

### 8.4 例：葉桜環界譚 + Game Module

```md
## Game Module

### Player Role
境界の街に迷い込んだ観察者、または街の違和感に気づき始めた住人。

### Goal
街に残された小さな違和感を集め、現実と異界の境界に近づく。

### Mechanics
- 街を探索する
- 葉桜が舞う場所を記録する
- 同じ場所の昼と夕方の差分を見る
- 住人の発言の変化を追う

### Loop
探索 → 違和感の発見 → 記録 → 新しい場所の解放 → 境界の変化

### Win / Lose / Change Conditions
勝敗よりも、街の見え方が変わることを重視する。
```

### 8.5 例：葉桜環界譚 + Story / Film Module

```md
## Story / Film Module

### Theme
春が終わった後に残るもの。忘れたはずの約束。境界に立つ人の孤独。

### Protagonist
街に戻ってきた人物、または街から出られない人物。

### Conflict
日常に戻りたい気持ちと、境界の向こうに残したものを確かめたい気持ち。

### Visual Motif
葉桜、通学路、駅、夕方の光、風に揺れる木々、誰もいない商店街。

### Key Scene
葉桜が舞う道で、主人公が「ここは昔と同じなのに、何かが違う」と気づく。

### Ending Direction
解決よりも、受け入れ。境界が消えるのではなく、共に生きる方向。
```

---

## 9. リポジトリ構成案

### 9.1 最小構成

```text
settings-as-play-protocol/
├── README.md
├── MANIFESTO.md
├── COMMONS_AGREEMENT.md
├── LICENSE.md
├── templates/
│   ├── sapp-core.md
│   ├── derivation-card.md
│   └── credit-block.md
├── modules/
│   ├── character.md
│   ├── worldbuilding.md
│   ├── image-generation.md
│   ├── story-film.md
│   └── game.md
├── examples/
│   ├── morning-night-nekomimi.md
│   └── hazakura-kankaitan/
│       ├── 001-border-town-core.md
│       ├── 002-border-town-image-module.md
│       ├── 003-border-town-game-module.md
│       └── 004-border-town-story-film-module.md
└── maps/
    └── derivation-map-sample.md
```

### 9.2 READMEに書くこと

```md
# Settings as Play Protocol

Settings as Play Protocolは、AI創作時代におけるキャラクター設定・世界観・プロンプト・遊び方を、
所有物として囲い込むのではなく、派生可能な「設定の芯」として共有するための実験です。

## これは何か

- 設定で遊ぶ文化への提言
- SaPP Coreという軽量テンプレート
- 派生元と由来を残す作法
- 葉桜環界譚を使ったサンプル実装

## これは何ではないか

- 新しい投稿サイト
- 作品販売マーケット
- すべてを自由素材化する運動
- 法的ライセンスの代替

## 基本コピー

Platformではなく、Protocol。
完成品ではなく、派生可能な「設定の芯」を共有する。
```

---

## 10. 運用方針

### 10.1 GitHubは「玄関」ではなく「原本置き場」

GitHubは、次の用途に向いている。

- READMEで目的や使い方を伝える
- Issueでアイデアや改善案を追う
- Discussionsで方向性やコミュニティの会話をする
- LICENSEで利用条件を示す
- Pull Requestでテンプレートや実例を改善する

ただし、GitHubは一般の創作ユーザーには硬い。

そのため、GitHubは「参加の玄関」ではなく、**原本・系譜・ルール置き場** として使う。

### 10.2 note / SNSは「発信・参加入口」

noteやSNSでは、GitHubの用語を前面に出しすぎない。

たとえば、こう伝える。

> 設定を共有して、誰かが派生できるようにするための小さなテンプレートを作りました。
> まずはこのカードを使って、あなたならどう遊ぶか試してみてください。

最初からPRを求めない。
ハッシュタグ投稿やコメントで十分にする。

### 10.3 PRやIssueは必須にしない

初期参加者に「GitHubでPRしてください」と言うとハードルが上がる。

初期導線はこうする。

1. noteやSNSで知る
2. 軽量版テンプレートをコピーする
3. 自分の場所で遊ぶ
4. 派生元リンクやハッシュタグをつける
5. 必要に応じて運営者がGitHubに記録する
6. 慣れた人だけIssueやPRを使う

### 10.4 ライセンスと文化的合意文を分ける

SaPP Commons Agreementは、法的ライセンスそのものではない。

法律上の利用条件は、必要に応じてCreative Commonsなどのライセンスを使う。Creative Commonsライセンスは、作者が著作権を保持したまま、一定条件で作品の流通やリミックスを許可する意思表示として使える。[^cc-license]
一方で、文化的な作法として、SaPP Commons Agreementを添える。

整理するとこうである。

```text
法的ライセンス：何をしてよいかを法的に示す
文化的合意文：どう扱うと気持ちよく派生できるかを示す
```

初期候補としては、次のような組み合わせが考えられる。

- このリポジトリの公開物：CC BY 4.0[^cc-by]
- SaPPを使う外部設定：設定カードごとに法的ライセンスを明記
- 文化的作法：SaPP Commons Agreement
- 未公開・保留領域：ライセンス対象外
- コードが入る場合：MIT Licenseなど

---

## 11. 初動ロードマップ

### 11.1 0〜7日：最小公開セット

目的：SaPPを「言葉」ではなく「使える型」にする。

作るもの：

```text
README.md
MANIFESTO.md
COMMONS_AGREEMENT.md
LICENSE.md
templates/sapp-core.md
templates/derivation-card.md
templates/credit-block.md
modules/image-generation.md
modules/story-film.md
modules/game.md
examples/morning-night-nekomimi.md
examples/hazakura-kankaitan/001-border-town-core.md
```

やること：

- GitHubリポジトリを作る
- READMEで企画の一文を明示する
- SaPP Coreを公開する
- 葉桜環界譚の一部をサンプル実装として置く
- note記事の下書きを作る

### 11.2 8〜30日：発信と自分での実験

目的：人を集める前に、型が実際に動くことを見せる。

やること：

- noteで提言記事を公開する
- SNSで軽量版テンプレートを流す
- 自分で3〜5個の設定カードを作る
- 葉桜環界譚にImage / Game / Story Moduleを足してみる
- 派生マップのサンプルを作る
- 反応があればIssueやDiscussionsに整理する

この段階では、参加者数を追いすぎない。
重要なのは、**型が遊べることを見せること** である。

### 11.3 1〜3か月：テンプレートの改善

目的：SaPP Coreを軽く保ちながら、使いやすくする。

やること：

- Core項目が多すぎないか検証する
- Core RulesとVariablesの書き分け例を増やす
- Optional Modulesを増やしすぎないよう整理する
- 派生カードの実例を作る
- クレジット表記を短くする
- note記事やREADMEをv0.5に更新する

成果物：

- SaPP Core v0.5
- 公式サンプル5〜10枚
- 派生マップv0.1
- よくある質問

### 11.4 3〜12か月：外部利用と小さな共同実験

目的：自分以外の人・場で使えるかを見る。

やること：

- 画像生成ユーザーに軽量版を試してもらう
- 小さな創作企画でSaPPを使ってみる
- ゲーム企画の種としてGame Moduleを試す
- 映像・短編向けにStory / Film Moduleを試す
- 既存サービスが採用しやすいように仕様を整える
- 日本語版と英語版のREADMEを分ける

成果物：

- SaPP Core v1.0 draft
- Optional Modules v0.5
- 外部利用例の一覧
- 採用ガイド

### 11.5 1〜3年：プラットフォーム化は「必要になったら」

目的：自分で運営を背負う前に、プロトコルとして広がる可能性を見る。

長期的には、どこかにSaPP的な仕組みを扱うプラットフォームができるとよい。

ただし、それは必ずしも自分で作る必要はない。

可能性：

- pixivのような創作プラットフォームが派生元・設定カード機能を持つ
- noteやブログがSaPPテンプレートを埋め込みやすくする
- GitHub風の設定リポジトリサービスが生まれる
- ゲーム制作ツールやAI動画制作ツールがSaPP Coreを読み込む
- 個人コミュニティがSaPPをローカルルールとして使う

自分で作る場合も、最初から巨大サービスにしない。

まずは、次のような軽いツールで十分である。

- SaPPカード作成フォーム
- 派生元リンク生成ツール
- 派生マップ生成ツール
- MarkdownからJSONへの変換ツール
- SaPP Coreバリデーター

---

## 12. 成功指標

SaPPの初期成功は、ユーザー数や売上では測らない。

### 12.1 初期指標

- SaPP Coreを使って設定カードを作れるか
- Core RulesとVariablesを分けて書けるか
- 他人が読んで派生できるか
- 派生元やクレジットを自然に残せるか
- 葉桜環界譚のサンプルが理解されるか
- テンプレートが重すぎないか

### 12.2 中期指標

- 自分以外の人がSaPPを使うか
- GitHub以外の場所でも使われるか
- 派生マップが面白く見えるか
- Optional Modulesが実際に役立つか
- ゲームや映画など別媒体への移植が起きるか
- 既存サービスが採用したくなるほど明確な型になっているか

### 12.3 長期指標

- SaPPが特定プラットフォームに依存しない形式として残るか
- 設定の由来と派生が文化として記録されるか
- 創作以外の領域にも自然に応用されるか
- 誰かがより良い実装を作れる状態になっているか

---

## 13. 周辺調査と競合整理

### 13.1 pixiv

pixivは、創作投稿、タグ、ユーザー企画、シリーズ、ブックマーク、コメント、支援・販売系サービスとの接続など、創作文化の基盤をすでに持っている。

また、pixivにはAI生成作品に関する投稿時の設定や、検索・閲覧でAI生成作品を表示するかどうかのオプションがある。[^pixiv-ai-post][^pixiv-ai-display]

そのため、将来的にpixivのような既存プラットフォームが、SaPP的な機能を持つ可能性は十分にある。

ただし、SaPPの主眼は「作品投稿」ではなく、次の点にある。

- 設定カード
- 派生元リンク
- Core Rules / Variablesの区別
- 派生カード
- 派生マップ
- Commons Agreement

つまり、pixivが場所として強いなら、SaPPはその上に載せられる作法である。

### 13.2 GitHub

GitHubは、README、Issues、Discussions、Pull Request、LICENSEなどを持ち、プロジェクトの目的説明、アイデア管理、議論、貢献、利用条件の明示に向いている。[^github-readme][^github-issues][^github-discussions][^github-license]

SaPP初期では、GitHubを次のように使う。

- README：企画の概要
- MANIFESTO：思想
- templates：SaPP Coreや派生カード
- modules：Optional Modules
- examples：葉桜環界譚などのサンプル
- maps：派生マップ
- Issues：改善案や派生案
- Discussions：名称、思想、使い方の議論

ただし、GitHubは創作一般の入口としては硬い。
そのため、GitHubは「原本置き場」であり、入口はnoteやSNSにする。

### 13.3 プロンプト市場・モデル共有サービス

PromptBase、Civitai、PromptHero、Hugging Faceなどは、プロンプト、モデル、ワークフロー、作例、コミュニティの共有に強みを持つ。

これらは、AI生成に必要な素材や技術を流通させる場所である。

一方で、SaPPが扱いたいのは、プロンプトやモデル単体ではなく、次のような **設定の芯** である。

- どんな文脈で使うのか
- 何を守るとそれらしくなるのか
- どこを変えてよいのか
- 何から派生したのか
- 次の人がどう受け取れるのか

プロンプトやモデルはOptional Moduleの一部として扱える。
しかし、SaPP Coreはそれらより上位の文脈を扱う。

### 13.4 note / SNS / Discord

noteやSNSは、提言や軽量テンプレートの拡散に向いている。

Discordなどは、必要になったら共同制作や雑談に使える。

ただし、最初からコミュニティ運営を背負うと重くなる。

そのため、初期は次の方針にする。

- note：提言とストーリー
- SNS：軽量テンプレートと作例
- GitHub：原本と仕様
- Discord：必要になってから

---

## 14. リスクと対策

### 14.1 テンプレートが重くなる

リスク：項目が増えすぎて、誰も書けなくなる。

対策：

- SaPP Coreは7項目に絞る
- 詳細はOptional Modulesに逃がす
- すべての欄を埋めなくてよいと明記する
- SNS用の軽量版を用意する

### 14.2 創作のノリを潰す

リスク：設定を構造化しすぎて、創作が義務っぽくなる。

対策：

- SaPPは「仕様書」ではなく「旅券」と説明する
- 空欄OK、雑でOK、後から育ててOKとする
- 作例を軽く、楽しくする

### 14.3 すべて自由素材化と誤解される

リスク：設定カードを出したら、全部自由利用できると思われる。

対策：

- 公開範囲と非公開範囲を明示する
- ライセンスとCommons Agreementを分ける
- 葉桜環界譚はサンプル実装であり、全開放ではないと明記する

### 14.4 権利やクレジットのトラブル

リスク：派生元が消える、他人の設定が無断で使われる、商用利用で揉める。

対策：

- Credit Blockを標準化する
- 派生元リンクを推奨する
- 商用利用の可否を設定カードごとに書けるようにする
- 法的ライセンスを必ず確認する導線を置く

### 14.5 プラットフォーム運営化して重くなる

リスク：投稿管理、モデレーション、問い合わせ、規約整備で疲れる。

対策：

- 初期はプロトコル提言に徹する
- 投稿サイトを作らない
- GitHubは原本置き場にする
- どこかがうまく実装してくれることも歓迎する

---

## 15. 公開時のメッセージ案

### 15.1 note記事タイトル案

- Settings as Play Protocol：AI創作時代の「設定で遊ぶ文化」について
- 設定は売るより、蒔いた方が面白い
- PlatformではなくProtocol：設定が旅できる作法を作る
- 完成品ではなく、派生可能な「設定の芯」を共有する

### 15.2 冒頭文案

```md
AI画像生成で遊んでいると、完成した画像だけでなく、
その背後にある「設定そのもの」が楽しくなることがあります。

たとえば、朝は寝ぼけていて夜は活動的になる猫耳キャラ。
葉桜だけが舞い続ける境界の街。
雨の日だけ表情が変わるキャラクター。

こうした設定は、単なる補助情報ではありません。
次の人が遊び始めるための種です。

Settings as Play Protocolは、そうした設定の芯を、
共有し、派生し、由来を残すための小さなプロトコル提案です。
```

### 15.3 短い説明

> SaPPは、設定を完成資料として固定するのではなく、他の人が受け取り、変え、別の媒体へ移植できる「設定の芯」として共有するための形式です。

### 15.4 さらに短い説明

> 完成品ではなく、派生可能な設定の芯を共有する。

### 15.5 コピー

> Platformではなく、Protocol。
> 設定を囲い込む場所ではなく、設定が旅できる作法を作る。

---

## 16. マニフェスト草案

```md
# Settings as Play Protocol Manifesto

私たちは、設定をただの所有物だとは考えません。
設定は、誰かが次に遊び始めるための種です。

キャラクター、世界観、プロンプト、遊び方。
それらは閉じて守ることで価値を持つこともあります。
けれど、ときには開かれ、受け渡され、変化することで、もっと大きな価値を持ちます。

私たちは、設定の派生を歓迎します。
コピー、改変、再解釈、別世界線、別媒体化。
それらは盗用ではなく、敬意ある変奏になりえます。

ただし、由来は消さない。
元の作者を神格化する必要はありません。
でも、どこから来た遊びなのかを残すことで、次の人がまた遊びに参加できます。

SaPPは、完成品ではなく、派生可能な「設定の芯」を共有するための小さなプロトコルです。
プラットフォームを独占するのではなく、どこでも使える作法を作ります。

設定は売り切るものではなく、蒔いて育てるもの。
私たちは、設定で遊ぶ文化をつくります。
```

---

## 17. まとめ

v0.4での結論は、次の通りである。

> SaPPは、AI創作・画像生成・キャラクター・世界観づくりから始める。
> しかし、その芯は「設定・文脈・由来・派生をどう持つか」という情報構造である。

そのため、SaPPは次のように設計する。

- 表の入口は創作・エンタメ
- 中心はSaPP Core
- 詳細はOptional Modules
- 応用は`Settings as X Protocol`として派生可能
- GitHubは原本置き場
- note / SNSは参加入口
- プラットフォーム化は長期の可能性
- 初期は提言、テンプレート、葉桜環界譚のサンプル実装に集中する

最初に作るべきものは、場所ではない。
誰かが場所を作りたくなるくらい、面白い型である。

---

## 18. 参考リンク

[^pixiv-ai-post]: pixivヘルプセンター「投稿作品のAI生成作品設定とはなんですか？」 https://www.pixiv.help/hc/ja/articles/11866194231577-%E6%8A%95%E7%A8%BF%E4%BD%9C%E5%93%81%E3%81%AEAI%E7%94%9F%E6%88%90%E4%BD%9C%E5%93%81%E8%A8%AD%E5%AE%9A%E3%81%A8%E3%81%AF%E3%81%AA%E3%82%93%E3%81%A7%E3%81%99%E3%81%8B

[^pixiv-ai-display]: pixivヘルプセンター「AI生成作品の表示オプションとはなんですか？」 https://www.pixiv.help/hc/ja/articles/11866167926809-AI%E7%94%9F%E6%88%90%E4%BD%9C%E5%93%81%E3%81%AE%E8%A1%A8%E7%A4%BA%E3%82%AA%E3%83%97%E3%82%B7%E3%83%A7%E3%83%B3%E3%81%A8%E3%81%AF%E3%81%AA%E3%82%93%E3%81%A7%E3%81%99%E3%81%8B

[^github-readme]: GitHub Docs, “About the repository README file.” https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes

[^github-issues]: GitHub Docs, “Tracking your work with issues.” https://docs.github.com/en/issues/tracking-your-work-with-issues

[^github-discussions]: GitHub Docs, “Collaborating with your community using discussions.” https://docs.github.com/en/discussions/collaborating-with-your-community-using-discussions

[^github-license]: GitHub Docs, “Adding a license to a repository.” https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository

[^cc-license]: Creative Commons Japan「クリエイティブ・コモンズ・ライセンスとは」 https://creativecommons.jp/licenses/

[^cc-by]: Creative Commons, “Attribution 4.0 International.” https://creativecommons.org/licenses/by/4.0/deed.en
