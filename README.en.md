# Module`view_hook`

## While:`18`

## Purpose

The`view_hook`module aims to facilitate the dynamic creation of inherited views (`inherit`) in Odoo when updating modules. This is especially useful when you need to modify or extend existing views automatically using only the template`key`, without manually defining inherited views for each update.

## Functionality

The module uses a model called`ir.ui.view.hook`that defines two main fields:

-   `template_name`: The name of the template to be used as the base for generating the inherited view.
-   `inherit_key`: The key of the view to be inherited.

The main function of the module is`post_update_hook`, which is executed when a module is updated. This function performs the following steps:

1.  Searches for records in the`ir.ui.view.hook`model that match the provided module name.
2.  For each record found:
    -   Retrieves the original view (`inherit_key`) and the base template (`template_name`).
    -   Extracts the content of the base template and uses it to create a new inherited view.
    -   If an inherited view with the generated name already exists, updates its content; otherwise, creates a new view.
    -   Propagates translations from the base template to the new inherited view.

## Usage Example

Below is an example of how to configure the module to dynamically generate inherited views:

```xml
<record id="module_name__template_name__view_hook" model="ir.ui.view.hook">
    <field name="template_name">module_name.template_name</field>
    <field name="inherit_key">inherit_module_name.inherit_tamplate_key</field>
</record>

<template id="module_name.template_name">
    <xpath expr="//div[@id='div_id']" position="replace"/>
</template>

<function model="ir.ui.view.hook" name="post_update_hook">
    <value>module_name</value>
</function>
```

### Example Explanation

1.  **Hook Definition (`ir.ui.view.hook`)**:
    -   Specifies the`template_name`, which is the base template.
    -   Defines the`inherit_key`, which is the key of the original view to be inherited.

2.  **Base Template**:
    -   The template contains the modifications to be applied to the inherited view.

3.  **Function Execution**:
    -   The`post_update_hook`function is executed with the`module_name`parameter, which indicates the module name. This activates the dynamic generation process of inherited views only for this module.

## Requirements

-   The module name (`module_name`) must be passed as a parameter when executing the`post_update_hook`function.
-   Base templates must be correctly defined and associated with the original views through the`ir.ui.view.hook`model.

## Benefits

-   Automation in the creation of inherited views.
-   Reduction of manual errors when updating modules.
-   Automatic propagation of translations between templates and inherited views.
