# Derivation Map

Derivation Map is a lightweight way to show how settings branch from one another.

It is not required to use SaPP.

## Minimal Example

```text
Original Setting
├─ Derivative A: changed season and setting
├─ Derivative B: changed medium from image prompt to short story
└─ Derivative C: kept core rules, changed character role
```

## What To Track

- Source setting
- Derivative setting
- What changed
- What stayed
- Credit link

## Mermaid Example

```mermaid
graph TD
  A["朝夜で変わる猫耳ちゃん / SaPP Core"]
  B["Character-focused Sample"]
  C["Image Prompt Variant"]
  D["Short Story Variant"]

  A --> B
  A --> C
  A --> D
```

## Hazakura Kankaitan Sample Map

```mermaid
graph TD
  A["葉桜環界譚 / 忘却の市街 SaPP Core"]
  B["Worldbuilding Module"]
  C["Image Generation Module"]
  D["Character Module: 猫守白羽"]
  E["Poster Visual Reference"]

  A --> B
  A --> C
  A --> D
  B --> E
  C --> E
  D --> E
```

This map uses only the public sample cards in [examples/hazakura-kankaitan](../examples/hazakura-kankaitan/README.md). It does not imply that unpublished source material is available for reuse.

For an actual derivative, keep the map small and pair it with a [Derivation Card](../templates/derivation-card.md).
