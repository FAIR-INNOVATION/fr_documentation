# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '法奥协作机器人用户手册'
copyright = '2022-2026, 法奥（苏州）机器人技术股份有限公司'
author = '法奥（苏州）机器人技术股份有限公司'
release = '3.9.6'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['recommonmark']

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'
locale_dirs = ['locale/']  # 设置本地化数据目录

# 注：在生成html的时候这句话要注释
# latex_engine = 'xelatex'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ["custom.css"]
html_logo = '_static/logo.svg'
html_theme_options = {
    'logo_only': True,
    # 'display_version': False,
}

# highlight_language = "c,c++,python"

# def setup(app):
#     app.add_css_file('_static/custom.css')

# rst_epilog = '\n.. include:: .custom-style.rst\n'

latex_elements = {
    # 1. 启用图片“草稿模式”，这是节省内存最有效的一步
    'preamble': r'\PassOptionsToPackage{draft}{graphicx}',
    
    # 2. 增加列表深度限制，防止复杂列表导致内存飙升
    'maxlistdepth': '10',
    
    # 3. 其他优化
    'pointsize': '10pt',      # 使用较小的默认字体
    'releasename': '',        # 简化一些标题
}