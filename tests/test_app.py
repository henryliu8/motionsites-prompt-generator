"""Check the actual Streamlit controls and generated prompt wiring."""

import re
import unittest
from pathlib import Path

from streamlit.testing.v1 import AppTest


APP = Path(__file__).resolve().parents[1] / "app.py"


class AppTests(unittest.TestCase):
    def test_english_controls_and_template_display_names(self):
        app = AppTest.from_file(str(APP)).run()
        self.assertFalse(app.exception)
        template_picker = app.selectbox[0]
        self.assertEqual(len(template_picker.options), 32)
        self.assertEqual(len(set(template_picker.options)), 32)
        self.assertIn("Video - Split City", template_picker.options)
        self.assertIn("Motion - SVG Flow Network", template_picker.options)
        self.assertIn("Layout - SaaS Multi-Section", template_picker.options)
        self.assertEqual(template_picker.options, sorted(template_picker.options))
        app.radio[1].set_value("split_two_column").run()
        for kind in ("selectbox", "radio", "text_input", "text_area", "color_picker", "slider"):
            for widget in app.get(kind):
                self.assertIsNone(re.search(r"[\u4e00-\u9fff]", widget.label))
                for option in getattr(widget, "options", []):
                    self.assertIsNone(re.search(r"[\u4e00-\u9fff]", str(option)))

    def test_display_names_still_load_the_correct_files(self):
        app = AppTest.from_file(str(APP)).run()
        filenames = sorted((APP.parent / "templates").glob("*.md.j2"))
        for path in filenames:
            with self.subTest(template=path.name):
                app.selectbox[0].set_value(path.name).run()
                self.assertFalse(app.exception)
                self.assertFalse(app.error)
                self.assertIn(f"templates/{path.name}", app.caption[-1].value)
                self.assertIn("OUTPUT MODE — RENDER THE PAGE DIRECTLY", app.code[0].value)
        app.selectbox[0].set_value("video_split_city.md.j2")
        app.selectbox[3].set_value("Full Width")
        app.radio[0].set_value("saas_multi_section")
        app.radio[1].set_value("split_two_column")
        next(widget for widget in app.text_input if widget.label == "Menu labels (comma-separated)").set_value("Products, Plans, Learn")
        app.run()
        self.assertFalse(app.exception)
        prompt = app.code[0].value
        self.assertIn("Nav Style: Full Width", prompt)
        self.assertIn('  - "Products"', prompt)
        self.assertIn('  - "Plans"', prompt)
        self.assertIn("Multi-section composition", prompt)


if __name__ == "__main__":
    unittest.main()
