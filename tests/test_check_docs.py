import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check-docs.py"
SPEC = importlib.util.spec_from_file_location("check_docs", SCRIPT)
check_docs = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(check_docs)
CARD = check_docs.ROOT / "sample.md"


class MetadataChecks(unittest.TestCase):
    def errors_for(self, yaml_text, *, okf=False):
        errors = []
        metadata = check_docs.read_front_matter(CARD, f"---\n{yaml_text}\n---\n# Sample\n", errors)
        if metadata is not None:
            check_docs.check_metadata(CARD, metadata, errors, okf=okf)
        return errors

    def test_plain_card_and_absent_optional_metadata_pass(self):
        errors = []
        self.assertIsNone(check_docs.read_front_matter(CARD, "# Plain card\n", errors))
        self.assertEqual([], errors)
        self.assertEqual([], self.errors_for('sapp_version: "0.6"'))
        self.assertEqual([], self.errors_for('type: "SaPP Core"', okf=True))

    def test_legacy_plain_status_passes(self):
        self.assertEqual([], self.errors_for('sapp_version: "0.5"\nstatus: public-draft'))

    def test_legacy_and_new_plain_status_must_agree(self):
        self.assertEqual([], self.errors_for('status: released\nsapp_status: released'))
        self.assertTrue(any("must agree" in error for error in self.errors_for(
            'status: draft\nsapp_status: released'
        )))
        self.assertEqual([], self.errors_for(
            'type: SaPP Core\nstatus: stable\nsapp_status: archived', okf=True
        ))

    def test_malformed_yaml_is_rejected(self):
        self.assertTrue(any("invalid YAML" in error for error in self.errors_for("card_id: [unfinished")))
        self.assertTrue(any("invalid YAML" in error for error in self.errors_for("custom: 2026-99-99")))

    def test_duplicate_keys_are_rejected_at_any_level(self):
        for yaml_text in ("card_id: first\ncard_id: second", "custom: {key: first, key: second}"):
            with self.subTest(yaml_text=yaml_text):
                self.assertTrue(any("duplicate key" in error for error in self.errors_for(yaml_text)))

    def test_front_matter_requires_a_mapping_and_string_keys(self):
        for yaml_text in ("- a list", "1: numeric key", ""):
            with self.subTest(yaml_text=yaml_text):
                self.assertTrue(any("mapping with string keys" in error for error in self.errors_for(yaml_text)))

    def test_unknown_keys_are_preserved(self):
        errors = []
        metadata = check_docs.read_front_matter(
            CARD, "---\ntype: SaPP Core\ncustom: {nested: [one, two]}\n---\n", errors
        )
        check_docs.check_metadata(CARD, metadata, errors, okf=True)
        self.assertEqual([], errors)
        self.assertEqual({"nested": ["one", "two"]}, metadata["custom"])

    def test_revision_requires_nonempty_strings(self):
        for value in ("0.6", "2026-10-13", "null", '" "'):
            with self.subTest(value=value):
                errors = self.errors_for(f'card_id: "setting-one"\ncard_revision: {value}')
                self.assertTrue(any("card_revision must be a non-empty string" in error for error in errors))

    def test_revision_dependencies_are_required(self):
        self.assertTrue(any("card_revision requires card_id" in error for error in self.errors_for('card_revision: "r2"')))
        self.assertTrue(any("derived_from_revision requires derived_from" in error for error in self.errors_for('derived_from_revision: "r1"')))
        self.assertEqual([], self.errors_for(
            'card_id: "setting-one"\ncard_revision: "r2"\n'
            'derived_from: "../original.md"\nderived_from_revision: "r1"'
        ))

    def test_status_axes_are_independent_and_have_distinct_values(self):
        self.assertEqual([], self.errors_for('type: SaPP Core\nstatus: stable\nsapp_status: released', okf=True))
        self.assertTrue(any("status must be" in error for error in self.errors_for('type: SaPP Core\nstatus: public-draft', okf=True)))
        self.assertTrue(any("sapp_status must be" in error for error in self.errors_for("sapp_status: [draft]")))

    def test_okf_type_is_required(self):
        self.assertTrue(any("type must be" in error for error in self.errors_for("status: draft", okf=True)))

    def test_optional_okf_shapes_are_checked_only_when_present(self):
        for yaml_text in ("tags: sapp", "sources: [{title: Missing resource}]", "generated: [agent]", "verified: {by: human:author}"):
            with self.subTest(yaml_text=yaml_text):
                self.assertTrue(self.errors_for(f"type: SaPP Core\n{yaml_text}", okf=True))

    def test_verified_mapping_list_and_offset_timestamps_pass(self):
        for verified in (
            '{by: "human:author", at: 2026-10-13T09:00:00+09:00}',
            '[{by: "human:author", at: "2026-10-13T00:00:00Z"}]',
        ):
            with self.subTest(verified=verified):
                self.assertEqual([], self.errors_for(
                    f'type: SaPP Core\ngenerated: {{by: "human:author"}}\nverified: {verified}', okf=True
                ))
        self.assertTrue(self.errors_for('type: SaPP Core\nstale_after: "2026-10-13T00:00:00"', okf=True))

    def test_unsafe_yaml_tags_are_rejected(self):
        self.assertTrue(any("invalid YAML" in error for error in self.errors_for('custom: !!python/object:builtins.object {}')))

    def test_closing_delimiter_may_be_at_end_of_file(self):
        errors = []
        metadata = check_docs.read_front_matter(CARD, '---\ncard_id: "one"\n---', errors)
        self.assertEqual({"card_id": "one"}, metadata)
        self.assertEqual([], errors)


if __name__ == "__main__":
    unittest.main()
