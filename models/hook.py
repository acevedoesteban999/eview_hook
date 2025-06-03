# -*- coding: utf-8 -*-

from odoo import models, fields, api,Command
from lxml import etree

class PostUpdateHook(models.Model):
    _name='ir.ui.view.hook'
    _description = "Hook"
    
    template_name = fields.Char(string="Name", required=True)
    inherit_key = fields.Char(string="Key", required=True)

    @api.model
    def post_update_hook(self,module_name:str=None):
        if not module_name:
            return
        templates = self.search([('template_name','=like',f'{module_name}.%')]).read(['inherit_key', 'template_name'])
        for template in templates:
            _temp = template.get('template_name')
            _view = template.get('inherit_key')
            try:
                view = self.env['ir.ui.view'].search([('key','=',_view)])
                templ = self.env['ir.ui.view'].search([('key','=',_temp)])
                root = etree.fromstring(templ.arch_db)
                new_arch_base = ""
                if root.tag == 't' and root.attrib.get('t-name') == _temp:
                    content = list(root)
                    if content:
                        new_arch_base = etree.tostring(content[0], encoding="unicode", pretty_print=True)
                if view:
                    templ_hook = self.env['ir.ui.view'].search([('name','=',f"{_temp}_hook")])
                    if templ_hook:
                        templ_hook.arch_base = new_arch_base
                    else:
                        templ_hook = self.env['ir.ui.view'].create({
                            'name': f"{_temp}_hook",
                            'arch': new_arch_base,
                            'type': 'qweb',
                        })
                        view.inherit_children_ids = [Command.link(templ_hook.id)]
                    
                    templ_translations , _ = templ.get_field_translations('arch_db',[lang for lang,_ in self.env['res.lang'].get_installed()])
                    if templ_translations:
                        templ_hook_translations = {}
                        for item in templ_translations:
                            lang = item['lang']
                            if lang not in templ_hook_translations:
                                templ_hook_translations[lang] = {}
                            templ_hook_translations[lang][item['source']] = item['value']
                        templ_hook._update_field_translations('arch_db',templ_hook_translations)
                           
            except Exception as e:
                pass