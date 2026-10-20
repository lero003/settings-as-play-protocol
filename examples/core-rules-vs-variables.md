# Core Rules vs Variables Example

This example shows a weak SaPP card fragment, a clearer version, and the questions that separate the two.

## Weak Example

Core Rules:

- かわいい
- いい感じ
- 世界観を守る

Variables:

- なんでも自由

Why it fails:

- "かわいい" and "いい感じ" are moods, not testable constraints.
- "世界観を守る" is circular; it does not say what to preserve.
- "なんでも自由" gives no recognizable boundary, so a derivative cannot tell what still makes this the same setting.

## Improved Example

Core Rules:

- 朝は眠そう、夜は活動的
- 同じキャラクターだと分かる耳、尻尾、目元を残す
- 時間変化が表情、服装、背景に出る

Variables:

- 季節
- 天気
- 服装
- 口調
- 背景

Why it works:

- Each Core Rule can be checked against an output.
- The rules describe a recognizable identity, not a mood.
- The Variables give a real space to play without contradicting the Core Rules.

## Four Questions

Use these when the split is not obvious:

1. **Change test**: Does changing it produce a different setting for the intended use?
2. **Recognition test**: Can a reader or AI still recognize the setting after the change?
3. **Promise test**: Does the change break the tone, safety boundary, or identity the card promises?
4. **Scope test**: Is it a constraint for the whole setting, or detail for one medium or scene?

The answers can conflict. Record which one took priority. A card can be intentionally closed or intentionally open, but it should say so.

## Overcorrected Example

Core Rules:

- 朝は眠そう
- 夜は活動的
- 耳は猫
- 尻尾は黒
- 目は金色
- 口調は敬語
- 背景は海辺
- 服装は制服
- 季節は夏
- カメラは正面

Variables:

- なし

This is not wrong if the author wants a closed setting. But it should be labeled as such: almost everything is a Core Rule, so compatible derivation is intentionally narrow. Without that label, a derivative author may mistake a preference for a universal rule.

## Related

- [SaPP の哲学](../docs/philosophy.md)
- [SaPP Core Skill](../spec/skills/sapp-core.skill.md#choosing-core-rules-and-variables)
