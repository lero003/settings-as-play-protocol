# Settings as Play Protocol

**Settings as Play Protocol（SaPP）** は、AI と人間が創作設定を共有・検証・再利用するための AI-first な仕様書フォーマットです。

Settings as Play Protocol, or SaPP, is an AI-first specification format for creative settings.

It is designed for humans and AI assistants to share, validate, transform, and extend creative settings through structured Markdown documents.

It is not a platform, marketplace, or legal license. It is a small format for keeping what should stay, what may change, and where a setting came from.

The canonical specification is defined as AI-readable Skill Documents. Human-facing templates, examples, and guides are provided as supporting materials.

> Platformではなく、Protocol。
>
> 完成品ではなく、派生可能な「設定の芯」を共有する。

## ステータス

- Latest GitHub Release: [v0.4.1-docs-polish](https://github.com/lero003/settings-as-play-protocol/releases/tag/v0.4.1-docs-polish)
- Latest public draft tag: [v0.5-ai-first-public-draft](https://github.com/lero003/settings-as-play-protocol/tree/v0.5-ai-first-public-draft)
- Current main: post-v0.5 development
- Next target: v0.5.x feedback polish or v0.6
- Scope: AI-readable Skill Documents、テンプレート、小さな作例
- Stability: 名称、項目、モジュール、運用形式は変更される可能性があります
- License: [CC BY 4.0](LICENSE.md)
- 注意: SaPP Commons Agreement は法的ライセンスではありません。法的な許諾は CC BY 4.0、文化的な作法は Commons Agreement として分けています。

## 3分で始める

1. [SaPP Core](templates/sapp-core.md) をコピーします。
2. まず Name、One-liner、Core Rules、Variables だけ埋めます。
3. 下書きでは Credit はあとから足せます。
4. 公開・派生・再配布する前に、Derivation & Credit を確認します。

SaPP は完成資料ではなく、育てられる設定メモから始められます。

SaPP の正本仕様を確認したい場合は、[SaPP Skill Documents](spec/skills/README.md) を読んでください。

## どこから読むか

### 自分の設定をSaPP化したい人

1. [SaPP Core Template](templates/sapp-core.md)
2. [Example: Minimal SaPP Core](examples/minimal/one-screen-setting.md)
3. [Credit Block Template](templates/credit-block.md)

### AI assistant や実装者に SaPP を読ませたい人

1. [SaPP Skill Documents](spec/skills/README.md)
2. [SaPP Core Skill](spec/skills/sapp-core.skill.md)
3. [SaPP Validator Skill](spec/skills/sapp-validator.skill.md)

### 既存設定から派生を作りたい人

1. [Derivation Card Template](templates/derivation-card.md)
2. [Derivation Map](docs/derivation-map.md)
3. [Commons Agreement](COMMONS_AGREEMENT.md)

### 画像生成・キャラ設定で使いたい人

1. [Image Generation Module](modules/image-generation.md)
2. [Character Module](modules/character.md)
3. [Example: Image-generation poster brief](examples/image-generation-focused/hazakura-poster-brief.md)

### SaPP自体に貢献したい人

1. [Contributing](CONTRIBUTING.md)
2. [Roadmap](docs/roadmap.md)
3. [Related Work](docs/related-work.md)

## Why SaPP? / なぜ SaPP か

AIによって、キャラクター、世界観、画像、短い物語をすぐに試作できる場面は増えています。

でも、創作の面白さは完成物だけにあるわけではありません。どんな設定で遊ぶのか。何を守ればその設定らしいのか。どこを変えれば、別の誰かの遊びになるのか。

SaPP は、そうした「設定の芯」を、許諾された範囲で受け渡し、由来を残しながら派生しやすくするための小さな形式です。

もちろん、SaPP は権利処理やプラットフォーム規約の代替ではありません。無断利用や権利侵害を正当化するものでもありません。

SaPP が目指すのは、共有してよいもの、派生を歓迎するもの、公開しないものの境界を明らかにしながら、設定を気持ちよく受け渡せる文化です。

設定を囲い込むだけでなく、受け渡し、育て合い、細くつながっていくために。

## これは何か

- 設定・文脈・遊び方を共有するための提言
- AI-readable / human-auditable な仕様書フォーマット
- SaPP Core という軽量な正本仕様
- 派生元、クレジット、公開範囲を残す作法
- GitHub、note、SNS、Wiki、ローカル文書などに載せられる形式
- AI画像生成、キャラクター設定、世界観づくりから試せる入口

## これは何ではないか

- 新しい投稿サイト
- プロンプト販売マーケット
- すべての設定を自由素材化するルール
- 著作権、ライセンス、契約、プラットフォーム規約の代替
- 医療・法務・金融など高リスク領域の判断仕様

## 使い方

1. [SaPP Core](templates/sapp-core.md) をコピーします。
2. 必要な項目だけ埋めます。初期案では空欄があっても構いません。
3. 追加情報が必要なときだけ Optional Module を足します。
4. 派生設定を作る場合は [Derivation Card](templates/derivation-card.md) を使います。
5. 可能な範囲で、元設定名・作者・リンクを残します。

SaPP を使うこと自体は、特定のライセンスを強制しません。このリポジトリの公開物は CC BY 4.0 ですが、あなた自身の設定カードでは、公開範囲と法的ライセンスを別途選べます。

## SaPP Core

SaPP Core の正本仕様は [SaPP Core Skill](spec/skills/sapp-core.skill.md) です。

人間向けテンプレートとして [SaPP Core Template](templates/sapp-core.md) も用意しています。

SaPP Core は7項目です。

1. **Name**: 設定名。Required
2. **One-liner**: 一言でいうと。Required
3. **Intent**: この設定で何を起こしたいか。Recommended
4. **Context**: 前提、世界、状況、関係性。Recommended
5. **Core Rules**: 変えないことで同一性を保つもの。Required
6. **Variables**: 変えることで派生を生むもの。Required
7. **Derivation & Credit**: 派生元、作者、リンク、公開範囲、利用条件。Required when sharing publicly or deriving from others

最も重要なのは、Core Rules と Variables を分けることです。

- **Core Rules** は設定らしさを守ります。
- **Variables** は派生の余白を作ります。

## Minimum SaPP Card

SaPPとして最低限共有できるカードは、次の4項目だけでも構いません。

- Name
- One-liner
- Core Rules
- Variables

ただし、公開・派生・再配布を想定する場合は、Derivation & Credit を必ず確認してください。公開範囲、非公開範囲、法的な許諾、文化的な作法を混ぜないことが、SaPPの安全弁です。

## Optional Modules

SaPP Core を太らせず、用途別の詳細は必要な分だけ足します。

モジュールの正本仕様は [Skill Documents](spec/skills/README.md) に置き、人間向けの書き始め用資料を `modules/` に置きます。

- [Character Module](modules/character.md)
- [Worldbuilding Module](modules/worldbuilding.md)
- [Image Generation Module](modules/image-generation.md)
- [Story / Film Module](modules/story-film.md)
- [Game Module](modules/game.md)

学習、ワークショップ、研究、プロジェクト設計などのモジュールは、SaPP Core を広げずに後から追加できます。

## 公開用ドキュメント

- [SaPP Skill Documents](spec/skills/README.md)
- [SaPP Core Skill](spec/skills/sapp-core.skill.md)
- [SaPP Validator Skill](spec/skills/sapp-validator.skill.md)
- [SaPP Derivation Skill](spec/skills/sapp-derivation.skill.md)
- [Manifesto](MANIFESTO.md)
- [Commons Agreement](COMMONS_AGREEMENT.md)
- [License](LICENSE.md)
- [Contributing](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)
- [Proposal v0.4](docs/proposal-v0.4.md) historical proposal
- [Roadmap](docs/roadmap.md)
- [Derivation Map](docs/derivation-map.md)
- [License / Permission Guide](docs/license-permission-guide.md)
- [Optional Front Matter](docs/front-matter.md)
- [Glossary](docs/glossary.md)
- [Publication Checklist](docs/publication-checklist.md)
- [Related Work](docs/related-work.md)
- [SaPP Core Template](templates/sapp-core.md)
- [SaPP Mini Template](templates/sapp-core-short.md)
- [Derivation Card Template](templates/derivation-card.md)
- [Credit Block Template](templates/credit-block.md)
- [Example: Minimal SaPP Core](examples/minimal/one-screen-setting.md)
- [Example: Tiny SaPP Cards](examples/tiny/README.md)
- [Example: Character-focused card](examples/character-focused/morning-night-nekomimi-character.md)
- [Example: Image-generation poster brief](examples/image-generation-focused/hazakura-poster-brief.md)
- [Example: Morning / Night Nekomimi](examples/morning-night-nekomimi.md)
- [Example: 葉桜環界譚](examples/hazakura-kankaitan/README.md)
- [Example: Core Rules vs Variables](examples/core-rules-vs-variables.md)

## Commons Agreement

SaPP は、敬意ある派生・改変・再解釈を歓迎します。同時に、由来を消さないことを大切にします。

[Commons Agreement](COMMONS_AGREEMENT.md) は文化的な合意文であり、法的ライセンスではありません。このリポジトリの公開物は、特記がない限り [CC BY 4.0](LICENSE.md) で提供します。

SaPP は、設定カードのライセンスを一律に強制するものではありません。公開範囲、非公開範囲、法的ライセンス、文化的な作法を分けて書くための形式です。

## Attribution

- Canonical author name: Hazakura Lab / 葉桜ラボ
- Website: [hazakura.dev](https://hazakura.dev)
- Project name: Settings as Play Protocol
- Short credit: SaPP by Hazakura Lab

## 参加のしかた

初期の参加は小さくて構いません。

- SaPP Core を1枚書いてみる
- SaPP Mini を1枚書いてみる
- 既存設定から派生カードを作る
- わかりにくいテンプレート項目を直す
- note、SNS、Wiki、GitHub などで作例を共有する
- 可能な範囲で元設定へのリンクを残す

このリポジトリが公開された後は、Issue や Pull Request での改善提案も歓迎します。ただし、SaPP を使うために GitHub 参加は必須ではありません。

## 現在の焦点

SaPP は、まず AI創作・画像生成・キャラクター設定・世界観づくりから始めます。具体的で、試しやすく、参加しやすいからです。

長期的には、設定・文脈・派生・クレジットを、媒体やコミュニティをまたいで受け渡せる形式に育てます。
