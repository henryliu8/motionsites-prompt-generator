"""Validate the prompt library with the same input contract as app.py."""

import itertools
import json
from pathlib import Path
import unittest

from jinja2 import Environment, FileSystemLoader, StrictUndefined, meta


ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
CONTEXT = {
    "brand_name": "Example Brand",
    "page_mode": "fixed_single_screen",
    "layout_type": "center_stack",
    "bg_color": "#080A19",
    "accent_color": "#35AEC7",
    "text_primary": "#FFFFFF",
    "text_secondary": "#B3B3B3",
    "font_family": "Inter",
    "button_radius": "12px",
    "glass_blur": "20px",
    "h1_text": "A long supplied headline for a responsive product experience",
    "subhead_text": "The supplied subhead must survive every template branch.",
    "primary_cta": "Start exploring",
    "secondary_cta": "Contact team",
    "right_column_type": "Browser Mockup",
    "nav_style": "Glass Pill",
    "nav_links": "Platform, Pricing, Resources, Blog",
    "nav_cta": "Book a demo",
}


class TemplateLibraryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.env = Environment(
            loader=FileSystemLoader(TEMPLATES), undefined=StrictUndefined
        )
        cls.names = sorted(path.name for path in TEMPLATES.glob("*.md.j2"))

    def test_library_inventory(self):
        self.assertEqual(len(self.names), 32)
        for prefix in ("layout_", "motion_", "video_"):
            self.assertEqual(sum(name.startswith(prefix) for name in self.names), 10)
        self.assertIn("motionsites_hero.md.j2", self.names)
        self.assertIn("saas_multi_section.md.j2", self.names)

    def test_every_template_renders_all_control_branches(self):
        branches = itertools.product(
            ("fixed_single_screen", "saas_multi_section"),
            ("center_stack", "split_two_column"),
            (None, "Contact team"),
            ("Glass Pill", "Full Width"),
        )
        for page_mode, layout, secondary, nav_style in branches:
            context = dict(
                CONTEXT, page_mode=page_mode, layout_type=layout,
                secondary_cta=secondary, nav_style=nav_style,
            )
            for name in self.names:
                with self.subTest(template=name, page=page_mode, layout=layout,
                                  secondary=secondary, nav=nav_style):
                    rendered = self.env.get_template(name).render(**context)
                    self.assertIn(CONTEXT["h1_text"], rendered)
                    self.assertIn(CONTEXT["subhead_text"], rendered)
                    self.assertIn(CONTEXT["primary_cta"], rendered)
                    self.assertIn(CONTEXT["brand_name"], rendered)
                    self.assertNotRegex(rendered, r"\{[%{]|__[A-Z_]+__")
                    if name != "motionsites_hero.md.j2":
                        self.assertEqual("Contact team" in rendered, bool(secondary))
                        for index in range(1, 7):
                            self.assertRegex(rendered, rf"(?m)^## {index}\. ")

    def test_templates_only_use_existing_app_parameters(self):
        for name in self.names:
            with self.subTest(template=name):
                source = (TEMPLATES / name).read_text()
                used = meta.find_undeclared_variables(self.env.parse(source))
                self.assertFalse(used - CONTEXT.keys(), used - CONTEXT.keys())

    def test_all_templates_preserve_menu_labels_and_preview_contract(self):
        for name in self.names:
            with self.subTest(template=name):
                rendered = self.env.get_template(name).render(
                    **dict(CONTEXT, nav_links=" Product , , Plans, Learn , Journal ")
                )
                labels = ['  - "Product"', '  - "Plans"', '  - "Learn"', '  - "Journal"']
                positions = [rendered.index(label) for label in labels]
                self.assertEqual(positions, sorted(positions))
                self.assertIn("OUTPUT MODE — RENDER THE PAGE DIRECTLY", rendered)
                self.assertIn("inline SVG fallback", rendered)
                self.assertIn("Apply alpha to the background color", rendered)
                self.assertIn("Industry-Aware Color Direction", rendered)

    def test_video_backgrounds_loop_without_controls(self):
        for name in self.names:
            if not name.startswith("video_"):
                continue
            with self.subTest(template=name):
                rendered = self.env.get_template(name).render(**CONTEXT)
                self.assertIn('<video muted loop playsinline', rendered)
                self.assertIn('No visible playback controls', rendered)
                self.assertIn('shared by Header and Hero', rendered)
                self.assertIn('inset: 0; width: 100%; height: 100%; object-fit: cover', rendered)
                self.assertNotIn('working Play button', rendered)
                self.assertNotIn('Reserve the specified aspect ratio', rendered)

    def test_saas_full_journey_only_appears_in_scrolling_mode(self):
        template = self.env.get_template("saas_multi_section.md.j2")
        fixed = template.render(**CONTEXT)
        scrolling = template.render(**dict(CONTEXT, page_mode="saas_multi_section"))
        self.assertNotIn("Full page section order", fixed)
        self.assertIn("render only navigation", fixed)
        for target in ("#customers", "#features", "#product", "#workflow",
                       "#stories", "#pricing", "#faq", "#contact"):
            self.assertIn(target, scrolling)

    def test_motion_and_video_groups_have_distinct_media_contracts(self):
        for name in self.names:
            text = self.env.get_template(name).render(**CONTEXT)
            if name.startswith("motion_"):
                self.assertIn("CODE-DRIVEN MOTION CONTRACT", text)
                self.assertIn("prefers-reduced-motion", text)
                self.assertNotRegex(text, r"https://\S+\.mp4")
            elif name.startswith("video_"):
                self.assertIn("VIDEO ASSET & PLAYBACK CONTRACT", text)
                self.assertIn('preload="none"', text)
                self.assertIn("Pause/Play", text)
                self.assertIn("prefers-reduced-motion", text)

    def test_video_manifest_matches_standalone_prompts(self):
        sources = json.loads((ROOT / "docs/video_sources.json").read_text())
        video_names = {name for name in self.names if name.startswith("video_")}
        self.assertEqual({item["template"] for item in sources}, video_names)
        self.assertEqual(len({item["mp4"] for item in sources}), 10)
        for item in sources:
            with self.subTest(template=item["template"]):
                rendered = self.env.get_template(item["template"]).render(**CONTEXT)
                for field in ("mp4", "low_bandwidth_mp4", "poster", "source_page"):
                    self.assertIn(item[field], rendered)
                    self.assertTrue(item[field].startswith("https://"))
                self.assertRegex(item["mp4"], r"/videos/\d+/\d+-720\.mp4$")
                self.assertEqual(item["license"], "Mixkit Stock Video Free License")


if __name__ == "__main__":
    unittest.main()
