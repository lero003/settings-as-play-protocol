# Settings as Play Protocol

**Settings as Play Protocol（SaPP）** は、AI創作時代のキャラクター設定・世界観・プロンプト・遊び方を、派生可能な「設定の芯」として共有するための小さなプロトコル提案です。

> Platformではなく、Protocol。
>
> 完成品ではなく、派生可能な「設定の芯」を共有する。

## ステータス

- Version: v0.4 public draft
- Scope: 提言、テンプレート、小さな作例
- Stability: 名称、項目、モジュール、運用形式は変更される可能性があります
- 注意: SaPP Commons Agreement は法的ライセンスではありません。権利関係を明確にする必要がある場合は、別途ライセンスや許諾条件を示してください。

## これは何か

- 設定・文脈・遊び方を共有するための提言
- SaPP Core という軽量テンプレート
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

## SaPP Core

SaPP Core は7項目です。

1. **Name**: 設定名
2. **One-liner**: 一言でいうと
3. **Intent**: この設定で何を起こしたいか
4. **Context**: 前提、世界、状況、関係性
5. **Core Rules**: 変えないことで同一性を保つもの
6. **Variables**: 変えることで派生を生むもの
7. **Derivation & Credit**: 派生元、作者、リンク、公開範囲、利用条件

最も重要なのは、Core Rules と Variables を分けることです。

- **Core Rules** は設定らしさを守ります。
- **Variables** は派生の余白を作ります。

## Optional Modules

SaPP Core を太らせず、用途別の詳細は必要な分だけ足します。

- [Character Module](modules/character.md)
- [Worldbuilding Module](modules/worldbuilding.md)
- [Image Generation Module](modules/image-generation.md)
- [Story / Film Module](modules/story-film.md)
- [Game Module](modules/game.md)

学習、ワークショップ、研究、プロジェクト設計などのモジュールは、SaPP Core を広げずに後から追加できます。

## 公開用ドキュメント

- [Manifesto](MANIFESTO.md)
- [Commons Agreement](COMMONS_AGREEMENT.md)
- [Proposal v0.4](docs/proposal-v0.4.md)
- [SaPP Core Template](templates/sapp-core.md)
- [Derivation Card Template](templates/derivation-card.md)
- [Credit Block Template](templates/credit-block.md)
- [Example: Morning / Night Nekomimi](examples/morning-night-nekomimi.md)

## Commons Agreement

SaPP は、敬意ある派生・改変・再解釈を歓迎します。同時に、由来を消さないことを大切にします。

[Commons Agreement](COMMONS_AGREEMENT.md) は文化的な合意文であり、法的ライセンスではありません。各設定カードには、必要に応じて公開範囲、非公開範囲、商用利用の扱い、ライセンスを明記してください。

## 参加のしかた

初期の参加は小さくて構いません。

- SaPP Core を1枚書いてみる
- 既存設定から派生カードを作る
- わかりにくいテンプレート項目を直す
- note、SNS、Wiki、GitHub などで作例を共有する
- 可能な範囲で元設定へのリンクを残す

このリポジトリが公開された後は、Issue や Pull Request での改善提案も歓迎します。ただし、SaPP を使うために GitHub 参加は必須ではありません。

## 現在の焦点

SaPP は、まず AI創作・画像生成・キャラクター設定・世界観づくりから始めます。具体的で、試しやすく、参加しやすいからです。

長期的には、設定・文脈・派生・クレジットを、媒体やコミュニティをまたいで受け渡せる形式に育てます。
