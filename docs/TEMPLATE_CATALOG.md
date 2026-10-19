# 模板目录与使用说明

当前共 32 个可选模板：原始 Hero、完善后的 SaaS 多区块，以及新增的 10 个版式、10 个代码动画、10 个视频 Hero。模板输出仍为英文提示词，保持原项目的 HTML5 / Tailwind CSS / React 技术约定。

## 使用方式

刷新 Streamlit 页面，配置界面现已使用英文；在侧栏模板选择器中按英文分类名选择：`Layout -` 为版式、`Motion -` 为代码动画、`Video -` 为视频素材，名称自动从文件名生成，实际文件名与加载路径不变。现有应用自动发现文件，无需注册或新增依赖。

- 模板名称决定结构；“居中单栏 / 左右分栏”控制新模板中文案区域的居中或左对齐，不会覆盖其标志性布局。原始 `motionsites_hero` 的行为保持不变。
- 多 Section 模式生成 Hero 和模板指定的后续区块。SaaS 模板在该模式生成完整十段页面。
- 单屏模式仅生成首屏，优先缩减装饰。短屏、大字号或 200% 缩放下允许必要的纵向滚动，以免裁切正文和按钮。
- 所有新模板使用现有颜色、字体、品牌、文案、导航及 CTA 参数；次按钮为空时会完整省略。
- 动画模板描述的是浏览器代码动画，不是视频生成。按模板安装所需库的是后续生成的 React 项目，当前 Python 项目无需增加这些依赖。
- 这里交付的是提示词模板，并非 30 个已实现的 React 页面；模板中的视觉、交互和性能要求需要在生成页面后验证。

## 原有模板

| 文件 | 说明 |
| --- | --- |
| [motionsites_hero.md.j2](../templates/motionsites_hero.md.j2) | 原始居中 / 双栏 Hero |
| [saas_multi_section.md.j2](../templates/saas_multi_section.md.j2) | Hero、客户标识、功能、演示、流程、评价、定价、FAQ、收尾 CTA、Footer；支持单屏降级 |

## 10 个版式模板

| 文件 | 名称 | 设计方向 |
| --- | --- | --- |
| [layout_editorial_typographic.md.j2](../templates/layout_editorial_typographic.md.j2) | 编辑式大字 | Editorial Typographic Hero |
| [layout_asymmetric_split.md.j2](../templates/layout_asymmetric_split.md.j2) | 非对称双栏 | Asymmetric Split Hero |
| [layout_bento_product_grid.md.j2](../templates/layout_bento_product_grid.md.j2) | Bento 产品矩阵 | Bento Product Matrix |
| [layout_browser_product_stage.md.j2](../templates/layout_browser_product_stage.md.j2) | 浏览器产品舞台 | Browser Product Stage |
| [layout_developer_terminal.md.j2](../templates/layout_developer_terminal.md.j2) | 终端开发者 | Developer Terminal Hero |
| [layout_metrics_dashboard.md.j2](../templates/layout_metrics_dashboard.md.j2) | 数据指标仪表盘 | Metrics Dashboard Hero |
| [layout_magazine_cover.md.j2](../templates/layout_magazine_cover.md.j2) | 杂志封面 | Magazine Cover Hero |
| [layout_vertical_timeline.md.j2](../templates/layout_vertical_timeline.md.j2) | 纵向时间线 | Vertical Process Timeline Hero |
| [layout_layered_product_cards.md.j2](../templates/layout_layered_product_cards.md.j2) | 层叠产品卡片 | Layered Product Cards Hero |
| [layout_minimal_whitespace.md.j2](../templates/layout_minimal_whitespace.md.j2) | 极简留白 | Minimal Whitespace Hero |

## 10 个代码动画 Hero

| 文件 | 名称 | 设计方向 |
| --- | --- | --- |
| [motion_aurora_gradient.md.j2](../templates/motion_aurora_gradient.md.j2) | 渐变极光 | Aurora Gradient Hero |
| [motion_orbital_system.md.j2](../templates/motion_orbital_system.md.j2) | 轨道系统 | Orbital System Hero |
| [motion_particle_constellation.md.j2](../templates/motion_particle_constellation.md.j2) | 粒子星场 | Particle Constellation Hero |
| [motion_interactive_grid.md.j2](../templates/motion_interactive_grid.md.j2) | 交互透视网格 | Interactive Perspective Grid Hero |
| [motion_kinetic_type_reveal.md.j2](../templates/motion_kinetic_type_reveal.md.j2) | 文字逐行揭示 | Kinetic Type Reveal Hero |
| [motion_perspective_card_tilt.md.j2](../templates/motion_perspective_card_tilt.md.j2) | 透视卡片 | Perspective Card Tilt Hero |
| [motion_svg_flow_network.md.j2](../templates/motion_svg_flow_network.md.j2) | SVG 流线网络 | SVG Flow Network Hero |
| [motion_three_wireframe_globe.md.j2](../templates/motion_three_wireframe_globe.md.j2) | Three.js 线框球 | Three.js Wireframe Globe Hero |
| [motion_cursor_spotlight.md.j2](../templates/motion_cursor_spotlight.md.j2) | 鼠标聚光灯 | Cursor Spotlight Hero |
| [motion_spring_card_deck.md.j2](../templates/motion_spring_card_deck.md.j2) | 弹簧卡片堆叠 | Spring Card Deck Hero |

## 10 个视频 Hero

| 文件 | 名称 | 设计方向 |
| --- | --- | --- |
| [video_cinematic_full_bleed.md.j2](../templates/video_cinematic_full_bleed.md.j2) | 全屏电影感 | Cinematic Full-Bleed Video Hero |
| [video_split_city.md.j2](../templates/video_split_city.md.j2) | 城市左右分屏 | Split City Video Hero |
| [video_rounded_sky_window.md.j2](../templates/video_rounded_sky_window.md.j2) | 圆角天空视频窗口 | Rounded Sky Window Video Hero |
| [video_creek_bento.md.j2](../templates/video_creek_bento.md.j2) | 溪流视频 Bento | Creek Video Bento Hero |
| [video_ink_typographic_mask.md.j2](../templates/video_ink_typographic_mask.md.j2) | 文字遮罩视频 | Ink Typographic Mask Video Hero |
| [video_portrait_coast.md.j2](../templates/video_portrait_coast.md.j2) | 竖屏海岸展示 | Portrait Coast Video Hero |
| [video_aurora_filmstrip.md.j2](../templates/video_aurora_filmstrip.md.j2) | 极光横向胶片带 | Aurora Filmstrip Video Hero |
| [video_floating_bokeh_card.md.j2](../templates/video_floating_bokeh_card.md.j2) | 悬浮视频卡片 | Floating Bokeh Video Card Hero |
| [video_architectural_space.md.j2](../templates/video_architectural_space.md.j2) | 建筑空间 | Architectural Space Video Hero |
| [video_forest_atmosphere.md.j2](../templates/video_forest_atmosphere.md.j2) | 自然氛围 | Forest Atmosphere Video Hero |

## 视频来源与文件

10 个视频模板分别内嵌真实 MP4（720/360 两档）、封面、素材页和授权链接。未将二进制视频打包进本仓库；生成页面时可以直接引用，正式部署建议下载所选文件并自行托管。文件 URL 由素材页提取，不依赖猜测 CDN 命名。

完整机器可读清单见 [video_sources.json](video_sources.json)。核实日期：2026-10-18；素材页均标注 Mixkit Stock Video Free License，排除了仅限个人使用的 Restricted 素材。保留素材记录，遵守 [Mixkit 授权条款](https://mixkit.co/license/#videoFree)，不要将视频作为独立素材转售或分发。

| 模板 | 素材页 | MP4 | 封面 |
| --- | --- | --- | --- |
| 全屏电影感 | [Sunset on a beach with a palm tree](https://mixkit.co/free-stock-video/sunset-on-a-beach-with-a-palm-tree-44499/) | [720](https://assets.mixkit.co/videos/44499/44499-720.mp4) / [360](https://assets.mixkit.co/videos/44499/44499-360.mp4) | [JPG](https://assets.mixkit.co/videos/44499/44499-thumb-720-0.jpg) |
| 城市左右分屏 | [Corporate and business buildings in the city.](https://mixkit.co/free-stock-video/corporate-and-business-buildings-in-the-city-4170/) | [720](https://assets.mixkit.co/videos/4170/4170-720.mp4) / [360](https://assets.mixkit.co/videos/4170/4170-360.mp4) | [JPG](https://assets.mixkit.co/videos/4170/4170-thumb-720-0.jpg) |
| 圆角天空视频窗口 | [White clouds moving across a clear blue sky quickly](https://mixkit.co/free-stock-video/white-clouds-moving-across-a-clear-blue-sky-quickly-51105/) | [720](https://assets.mixkit.co/videos/51105/51105-720.mp4) / [360](https://assets.mixkit.co/videos/51105/51105-360.mp4) | [JPG](https://assets.mixkit.co/videos/51105/51105-thumb-720-0.jpg) |
| 溪流视频 Bento | [Flying over a relaxing creek full of rock on the countryside](https://mixkit.co/free-stock-video/flying-over-a-relaxing-creek-full-of-rock-on-the-51585/) | [720](https://assets.mixkit.co/videos/51585/51585-720.mp4) / [360](https://assets.mixkit.co/videos/51585/51585-360.mp4) | [JPG](https://assets.mixkit.co/videos/51585/51585-thumb-720-0.jpg) |
| 文字遮罩视频 | [Abstract video of a liquid with dark ink flowing](https://mixkit.co/free-stock-video/abstract-video-of-a-liquid-with-dark-ink-flowing-44818/) | [720](https://assets.mixkit.co/videos/44818/44818-720.mp4) / [360](https://assets.mixkit.co/videos/44818/44818-360.mp4) | [JPG](https://assets.mixkit.co/videos/44818/44818-thumb-720-0.jpg) |
| 竖屏海岸展示 | [Overhead view of a rocky coast and waves crashing](https://mixkit.co/free-stock-video/overhead-view-of-a-rocky-coast-and-waves-crashing-51502/) | [720](https://assets.mixkit.co/videos/51502/51502-720.mp4) / [360](https://assets.mixkit.co/videos/51502/51502-360.mp4) | [JPG](https://assets.mixkit.co/videos/51502/51502-thumb-720-0.jpg) |
| 极光横向胶片带 | [Yellow northern lights in Norway](https://mixkit.co/free-stock-video/yellow-northern-lights-in-norway-4036/) | [720](https://assets.mixkit.co/videos/4036/4036-720.mp4) / [360](https://assets.mixkit.co/videos/4036/4036-360.mp4) | [JPG](https://assets.mixkit.co/videos/4036/4036-thumb-720-0.jpg) |
| 悬浮视频卡片 | [Blurred abstract cars lights at night with bokeh effect](https://mixkit.co/free-stock-video/blurred-abstract-cars-lights-at-night-with-bokeh-effect-30/) | [720](https://assets.mixkit.co/videos/30/30-720.mp4) / [360](https://assets.mixkit.co/videos/30/30-360.mp4) | [JPG](https://assets.mixkit.co/videos/30/30-thumb-720-2.jpg) |
| 建筑空间 | [Luxury hotel room panning shot](https://mixkit.co/free-stock-video/luxury-hotel-room-panning-shot-4196/) | [720](https://assets.mixkit.co/videos/4196/4196-720.mp4) / [360](https://assets.mixkit.co/videos/4196/4196-360.mp4) | [JPG](https://assets.mixkit.co/videos/4196/4196-thumb-720-0.jpg) |
| 自然氛围 | [Gloomy forest full of trees during a rainy afternoon](https://mixkit.co/free-stock-video/gloomy-forest-full-of-trees-during-a-rainy-afternoon-22729/) | [720](https://assets.mixkit.co/videos/22729/22729-720.mp4) / [360](https://assets.mixkit.co/videos/22729/22729-360.mp4) | [JPG](https://assets.mixkit.co/videos/22729/22729-thumb-720-0.jpg) |

外部链接可能变化。播放被浏览器拦截、网络失败、移动端、减少动态效果或省流偏好下，模板要求回退到真实封面；必须保留可操作的播放/暂停按钮及始终可读的 HTML 正文。

## 本地检查

运行 `venv/bin/python -m unittest discover -s tests -v`，检查模板数量、参数分支、严格渲染及视频清单一致性。Streamlit 的真实选择器切换可用 AppTest 验证；该检查不等同于对未来生成的 React 页面的视觉验收。


## 统一交付与视觉规则
此提示词经过提炼而成，适合在网站开发初期进行配色和landing page的整体样式浏览，通过选择不同的模版类型，找到符合需求的样式，后期可对提示词就行自定义修改，也可以创建自己的模版，放到模版目录中，刷新页面就可以显示在模版列表中。

全部模板要求在支持网页预览的大模型中直接打开交互页面，不在对话中输出代码。导航保留配置菜单的原文和顺序，显示品牌 Logo（缺省使用原创 SVG），使用独立中性色半透明背景，并与正文保留间距；行业配色建议在内部应用，不显示到网页上。

视频模板现均使用覆盖 Header + Hero 的全屏背景，保留各自素材和前景设计元素，旧名称中的 Window、Card、Filmstrip、Mask 等不再表示视频播放窗口。桌面静音循环播放，不显示素材详情或播放控件；手机、减少动态效果及省流量模式显示全屏封面。背景类代码动画覆盖 Header + Hero，卡片和产品交互保留在前景组件内。

This prompt has been refined to assist with color scheme selection and the overall styling of landing pages during the early stages of web development. Users can explore various template types to find a style that meets their requirements. The prompt can be customized further, and users can even create their own templates—simply add them to the template directory and refresh the page to see them appear in the selection list.

All templates are designed to render as interactive, previewable web pages directly within the AI ​​model’s interface, rather than outputting raw code in the chat. The navigation bar must retain the original configuration menu items and their sequence; it should display a brand logo (defaulting to an original SVG), feature a semi-transparent, neutral-toned background, and maintain proper spacing from the main content. Industry-specific color palettes are intended for internal reference only and should not be displayed on the rendered web page.

Video-based templates now utilize a full-screen background that spans both the Header and Hero sections, while preserving their respective assets and foreground design elements. Terms such as "Window," "Card," "Filmstrip," or "Mask"—previously used in template names—no longer denote specific video playback windows. On desktop, videos play in a muted, looped format without displaying asset details or playback controls. On mobile devices—or when "reduced motion" or "data-saver" modes are active—the templates will display a full-screen static cover image instead. Background-based programmatic animations cover the Header and Hero areas, while interactive elements like cards and product components remain contained within the foreground layer.