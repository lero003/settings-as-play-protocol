# Derivation Map

Derivation Map is a lightweight way to show how settings branch from one another. It may also show card composition when a sample is split into Core and Optional Modules, but derivative branches and composition links should be labeled differently.

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

When available, label each node with its own `card_id` / `card_revision` and each source edge with the source revision. Keep a derivative's source snapshot fixed when the source later changes. [The revision samples](../examples/versioned/lighthouse-derivative-r1.md) show a derivative of r1 alongside the same source card's r2. Revision tracking remains optional.

## Mermaid Example

```mermaid
graph TD
  A["朝夜で変わる猫耳ちゃん / SaPP Core"]
  B["Character-focused Sample"]
  C["Image Prompt Variant"]
  D["Short Story Variant"]

  A -->|derives| B
  A -->|derives| C
  A -->|derives| D
```

## Hazakura Kankaitan Sample Map

```mermaid
graph TD
  A["葉桜環界譚 / 忘却の市街 SaPP Core"]
  B["Worldbuilding Module"]
  C["Image Generation Module"]
  D["Character Module: 猫守白羽"]
  E["Poster Visual Reference"]

  A -->|extends| B
  A -->|extends| C
  A -->|extends| D
  B -->|informs| E
  C -->|informs| E
  D -->|informs| E
```

This map uses only the public sample cards in [examples/hazakura-kankaitan](../examples/hazakura-kankaitan/README.md). It does not imply that unpublished source material is available for reuse.

Use `derives` when a new setting or card changes a source. Use `extends` when an optional module adds detail to the same sample. Use `informs` when a card guides an asset, prompt, or reference.

For an actual derivative, keep the map small and pair it with a [Derivation Card](../templates/derivation-card.md).
