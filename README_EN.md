# Module `view_hook`
## Odoo: `18`

## Purpose

The `view_hook` module aims to facilitate the dynamic creation of inherited views (`inherit`) in Odoo when updating modules. This is especially useful when modifying or extending existing views automatically, without manually defining inherited views during each update.

## Functionality

The module uses a model called `ir.ui.view.hook` that defines two main fields:

- `template_name`: The name of the template used as the base to generate the inherited view.
- `inherit_key`: The key of the view to be inherited.

The main function of the module is `post_update_hook`, which runs when a module is updated. This function performs the following steps:

1. Searches for records in the `ir.ui.view.hook` model that match the provided module name.
2. For each record found:
   - Retrieves the original view (`inherit_key`) and the base template (`template_name`).
   - Extracts the content of the base template and uses it to create a new inherited view.
   - If an inherited view with the generated name already exists, updates its content; otherwise, creates a new view.
   - Propagates translations from the base template to the new inherited view.

## Usage Example

Below is an example of how to configure the module to dynamically generate inherited views:

```xml
<record id="galileo_webiste_product_share_buttons_view_hook" model="ir.ui.view.hook">
    <field name="template_name">galileo_website.galileo_webiste_product_share_buttons_1</field>
    <field name="inherit_key">theme_clarico_vega.product_share_buttons_ept</field>
</record>

<template id="galileo_webiste_product_share_buttons_1">
    <xpath expr="//div[hasclass('s_share')]" position="replace"/>
</template>

<function model="ir.ui.view.hook" name="post_update_hook">
    <value>galileo_website</value>
</function>
```

### Example Explanation

1. **Hook Definition (`ir.ui.view.hook`)**:
   - Specifies `template_name` as `galileo_website.galileo_webiste_product_share_buttons_1`, which is the base template.
   - Defines `inherit_key` as `theme_clarico_vega.product_share_buttons_ept`, which is the original view to be inherited.

2. **Base Template**:
   - The template `galileo_webiste_product_share_buttons_1` contains the modifications to be applied to the inherited view.

3. **Function Execution**:
   - The `post_update_hook` function is executed with the parameter `galileo_website`, indicating the module name. This triggers the dynamic generation of inherited views.

## Requirements

- The module name (`module_name`) must be passed as a parameter when executing the `post_update_hook` function.
- Base templates must be correctly defined and associated with original views through the `ir.ui.view.hook` model.

## Benefits

- Automation in creating inherited views.
- Reduction of manual errors when updating modules.
- Automatic propagation of translations between templates and inherited views.
