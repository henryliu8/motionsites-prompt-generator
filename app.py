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

st.title("⚡ Motionsites 风格高精度 Prompt 生成器")
st.caption("选择基础参数与排版策略，一键生成可用于 LLM / Code Generator 的超级 Prompt 规范文档。")

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

available_templates = get_available_templates()

# ==========================================
# 3. 侧边栏配置项 (Form Controls)
# ==========================================
with st.sidebar:
    st.header("🎛️ 页面配置参数")
    
    # 📁 模板选择器
    st.subheader("0. 选定提示词模板")
    if available_templates:
        selected_template_file = st.selectbox(
            "选择提示词模板 (templates/ 目录下)",
            options=available_templates,
            index=0,
            help="你可以随时在 templates/ 文件夹中新增或修改 .j2 模板文件"
        )
    else:
        st.error("⚠️ 未在 templates/ 文件夹中找到任何模板文件！请创建模板后再试。")
        st.stop()
        
    st.divider()
    
    st.subheader("1. 页面类型与布局")
    page_mode = st.radio(
        "页面滚动模式 (Viewport)",
        options=["fixed_single_screen", "saas_multi_section"],
        format_func=lambda x: "单屏锁定 (100vh 无滚动)" if x == "fixed_single_screen" else "多 Section (可往下滚动)",
        help="单屏模式强制 overflow-hidden 且占据 100vh"
    )
    
    layout_type = st.radio(
        "Hero 核心排版风格",
        options=["center_stack", "split_two_column"],
        format_func=lambda x: "居中单栏 (Center Stack)" if x == "center_stack" else "左右分栏 (Split Column)",
    )
    
    st.divider()
    st.subheader("2. 视觉 Token 与主题")
    font_family = st.selectbox(
        "主字体 (Font Family)",
        options=["Suisse Intl", "Sora", "Poppins", "Inter", "Kanit"],
        index=0
    )
    
    col1, col2 = st.columns(2)
    with col1:
        bg_color = st.color_picker("背景底色", "#080A19")
        accent_color = st.color_picker("主强调色", "#35AEC7")
    with col2:
        text_primary = st.color_picker("主文字颜色", "#FFFFFF")
        text_secondary = st.color_picker("副文字颜色", "#B3B3B3")

    button_radius = st.selectbox("按钮圆角", ["999px (全胶囊)", "12px (圆角矩形)", "6px (硬朗微圆角)"], index=0)
    glass_blur = st.slider("玻璃模糊度 (Backdrop Blur)", min_value=0, max_value=40, value=20, step=2, format="%dpx")
    
    st.divider()
    st.subheader("3. 导航栏 (Nav) 配置")
    nav_style = st.selectbox("导航栏样式", ["Glass Pill (悬浮玻璃胶囊)", "Full Width (全宽固定)"])
    brand_name = st.text_input("品牌/项目名称", "Apogee")
    nav_links_raw = st.text_input("导航菜单项 (逗号分隔)", "Platform, Pricing, Resources, Blog")
    nav_cta = st.text_input("导航栏右侧按钮", "Book a demo")

# ==========================================
# 4. 主区域配置 (文案输入与展示)
# ==========================================
col_left, col_right = st.columns([1, 1], gap="medium")

with col_left:
    st.subheader("📝 文案与核心内容配置")
    
    h1_text = st.text_area("H1 主标题文案", "Elevate your essential data to new heights", height=70)
    subhead_text = st.text_area("Subhead 副标题文案", "Advanced reasoning systems and predictive models built for the unknown.", height=80)
    
    c1, c2 = st.columns(2)
    with c1:
        primary_cta = st.text_input("主按钮文案", "Get Started")
    with c2:
        secondary_cta = st.text_input("副按钮文案 (可选，留空则不显示)", "Talk to team")
        
    right_column_type = "Glassmorphic Stats Card with Chart"
    if layout_type == "split_two_column":
        right_column_type = st.selectbox(
            "右侧展示组件类型",
            ["Glassmorphic Stats Card (数据图表卡片)", "Browser Mockup (浏览器预览框)", "3D Hologram Frame (3D 展示框)"]
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
    st.error(f"渲染模板出错: {str(e)}")
    st.stop()

# 在右侧展示导出的 Markdown Prompt
with col_right:
    st.subheader("🚀 生成的高精度 Prompt 结果")
    st.caption(f"当前使用的模板文件：`templates/{selected_template_file}`")
    st.info("可以直接点击右上角复制按钮，全文粘贴至 ChatGPT / Claude / Cursor 中使用。")
    st.code(rendered_prompt, language="markdown")
