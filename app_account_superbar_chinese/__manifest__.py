# -*- coding: utf-8 -*-

# Created on 2018-08-15
# author: 广州尚鹏，http://www.sunpop.cn
# email: 300883@qq.com
# resource of Sunpop
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo在线中文用户手册（长期更新）
# http://www.sunpop.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# http://www.sunpop.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# http://www.sunpop.cn/odoo10_developer_document_offline/
# description:

{
    'name': "App account superbar navigator for chinese account.",
    'version': '12.0.11.15',
    'author': 'Sunpop.cn',
    'category': 'Base',
    'website': 'http://www.sunpop.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """
    Browse journal by account chart... Use for parent children tree list kanban navigator. 
    ztree widget.Hierarchy Tree.Parent Children relation tree.
    """,
    'description': """
    树状结构会计科目表导航。
    Superbar, zTree widget. 
    Advance search with real parent children tree, ListView or KanbanView. parent tree, children tree,
    eg: Product category tree ,Department tree, stock location tree.
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'l10n_cn_standard_lastest',
        'app_account_superbar',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'views/account_views.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'css': [
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'js': [
    ],
    'post_load': None,
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': True,
    'auto_install': True,
}
