import os
import streamlit as st
from jinja2 import Environment, FileSystemLoader

# ==========================================
# 1. 页面基本设置与 Jinja2 环境初始化
# ==========================================
st.set_page_config(
    page_title="Motionsites Prompt Generator",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")

# 如果 templates 文件夹不存在，自动创建
if not os.path.exists(TEMPLATES_DIR):
    os.makedirs(TEMPLATES_DIR)

# 初始化 Jinja2 环境
jinja_env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

st.title("⚡ Hellosite Precision Prompt Generator")
st.caption("Configure your design and copy, then generate a detailed prompt for your AI website builder.")

# ==========================================
# 2. 动态读取模板列表
# ==========================================
def get_available_templates():
    if not os.path.exists(TEMPLATES_DIR):
        return []
    # 筛选以 .j2 或 .md 结尾的文件
    return [
        f for f in os.listdir(TEMPLATES_DIR) 
        if f.endswith(".j2") or f.endswith(".md") or f.endswith(".markdown")
    ]

def get_template_display_name(filename):
    name = filename
    for suffix in (".j2", ".markdown", ".md"):
        if name.endswith(suffix):
            name = name[:-len(suffix)]
    special_names = {
        "motionsites_hero": "Layout - Motionsites Hero",
        "saas_multi_section": "Layout - SaaS Multi-Section",
    }
    if name in special_names:
        return special_names[name]
    prefix, separator, title = name.partition("_")
    acronyms = {"svg": "SVG", "three": "3D", "ui": "UI", "saas": "SaaS"}
    words = (title if separator and prefix in ("layout", "motion", "video") else name).split("_")
    label = " ".join(acronyms.get(word, word.capitalize()) for word in words)
    return f"{prefix.capitalize()} - {label}" if separator and prefix in ("layout", "motion", "video") else label


available_templates = sorted(get_available_templates(), key=get_template_display_name)

# ==========================================
# 3. 侧边栏配置项 (Form Controls)
# ==========================================
with st.sidebar:
    st.header("🎛️ Page Configuration")
    
    # 📁 模板选择器
    st.subheader("0. Prompt Template")
    if available_templates:
        selected_template_file = st.selectbox(
            "Choose a template",
            options=available_templates,
            format_func=get_template_display_name,
            index=0,
            help="Add or edit template files in the templates/ directory."
        )
    else:
        st.error("⚠️ No templates found. Add a template to the templates/ directory.")
        st.stop()
        
    st.divider()
    
    st.subheader("1. Page & Layout")
    page_mode = st.radio(
        "Viewport mode",
        options=["fixed_single_screen", "saas_multi_section"],
        format_func=lambda x: "Single screen (no scrolling)" if x == "fixed_single_screen" else "Multiple sections (scrollable)",
        help="Single-screen mode fits navigation and Hero into one viewport; essential content may scroll on short screens or at high zoom."
    )
    
    layout_type = st.radio(
        "Hero layout",
        options=["center_stack", "split_two_column"],
        format_func=lambda x: "Centered stack" if x == "center_stack" else "Split columns",
    )
    
    st.divider()
    st.subheader("2. Theme & Design Tokens")
    font_family = st.selectbox(
        "Font family",
        options=["Suisse Intl", "Sora", "Poppins", "Inter", "Kanit"],
        index=0
    )
    
    col1, col2 = st.columns(2)
    with col1:
        bg_color = st.color_picker("Background color", "#080A19")
        accent_color = st.color_picker("Accent color", "#35AEC7")
    with col2:
        text_primary = st.color_picker("Primary text color", "#FFFFFF")
        text_secondary = st.color_picker("Secondary text color", "#B3B3B3")

    button_radius = st.selectbox("Button corners", ["999px (Pill)", "12px (Rounded)", "6px (Subtle)"], index=0)
    glass_blur = st.slider("Backdrop blur", min_value=0, max_value=40, value=20, step=2, format="%dpx")
    
    st.divider()
    st.subheader("3. Navigation")
    nav_style = st.selectbox("Navigation style", ["Glass Pill", "Full Width"])
    brand_name = st.text_input("Brand / project name", "Hellosite")
    nav_links_raw = st.text_input("Menu labels (comma-separated)", "Platform, Pricing, Resources, Blog")
    nav_cta = st.text_input("Navigation CTA label", "Book a demo")

# ==========================================
# 4. 主区域配置 (文案输入与展示)
# ==========================================
col_left, col_right = st.columns([1, 1], gap="medium")

with col_left:
    st.subheader("📝 Copy & Content")
    
    h1_text = st.text_area("Headline (H1)", "Elevate your essential data to new heights", height=70)
    subhead_text = st.text_area("Subheadline", "Advanced reasoning systems and predictive models built for the unknown.", height=80)
    
    c1, c2 = st.columns(2)
    with c1:
        primary_cta = st.text_input("Primary CTA label", "Get Started")
    with c2:
        secondary_cta = st.text_input("Secondary CTA label (optional)", "Talk to team")
        
    right_column_type = "Glassmorphic Stats Card with Chart"
    if layout_type == "split_two_column":
        right_column_type = st.selectbox(
            "Product showcase",
            ["Glassmorphic Stats Card", "Browser Mockup", "3D Hologram Frame"]
        )

# ==========================================
# 5. 读取所选模板并渲染 Prompt
# ==========================================
try:
    template = jinja_env.get_template(selected_template_file)
    radius_value = button_radius.split(" ")[0]

    rendered_prompt = template.render(
        brand_name=brand_name,
        page_mode=page_mode,
        layout_type=layout_type,
        bg_color=bg_color,
        accent_color=accent_color,
        text_primary=text_primary,
        text_secondary=text_secondary,
        font_family=font_family,
        button_radius=radius_value,
        glass_blur=f"{glass_blur}px",
        h1_text=h1_text,
        subhead_text=subhead_text,
        primary_cta=primary_cta,
        secondary_cta=secondary_cta if secondary_cta.strip() != "" else None,
        right_column_type=right_column_type,
        nav_style=nav_style,
        nav_links=nav_links_raw,
        nav_cta=nav_cta
    )
except Exception as e:
    st.error(f"Could not render template: {str(e)}")
    st.stop()

# 在右侧展示导出的 Markdown Prompt
with col_right:
    st.subheader("🚀 Generated Prompt")
    st.caption(f"Template source: `templates/{selected_template_file}`")
    st.info("Copy the full prompt using the copy button, then paste it into an AI builder with live preview support.")
    st.code(rendered_prompt, language="markdown")
