# Módulo `view_hook`
## Odoo: `18`

## Propósito

El módulo `view_hook` tiene como objetivo facilitar la creación dinámica de vistas heredadas (`inherit`) en Odoo al actualizar los módulos. Esto es especialmente útil cuando se necesita modificar o extender vistas existentes de manera automatizada, sin necesidad de definir manualmente las vistas heredadas en cada actualización.

## Funcionamiento

El módulo utiliza un modelo llamado `ir.ui.view.hook` que define dos campos principales:

- `template_name`: El nombre del template que se utilizará como base para generar la vista heredada.
- `inherit_key`: La clave de la vista que será heredada.

La función principal del módulo es `post_update_hook`, que se ejecuta al actualizar un módulo. Esta función realiza los siguientes pasos:

1. Busca los registros en el modelo `ir.ui.view.hook` que coincidan con el nombre del módulo proporcionado.
2. Para cada registro encontrado:
   - Obtiene la vista original (`inherit_key`) y el template base (`template_name`).
   - Extrae el contenido del template base y lo utiliza para crear una nueva vista heredada.
   - Si ya existe una vista heredada con el nombre generado, actualiza su contenido; de lo contrario, crea una nueva vista.
   - Propaga las traducciones del template base a la nueva vista heredada.

## Ejemplo de Uso

A continuación, se muestra un ejemplo de cómo configurar el módulo para generar vistas heredadas dinámicamente:

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

### Explicación del Ejemplo

1. **Definición del Hook (`ir.ui.view.hook`)**:
   - Se especifica el `template_name` como `galileo_website.galileo_webiste_product_share_buttons_1`, que es el template base.
   - Se define el `inherit_key` como `theme_clarico_vega.product_share_buttons_ept`, que es la vista original que será heredada.

2. **Template Base**:
   - El template `galileo_webiste_product_share_buttons_1` contiene las modificaciones que se aplicarán a la vista heredada.

3. **Ejecución de la Función**:
   - La función `post_update_hook` se ejecuta con el parámetro `galileo_website`, que indica el nombre del módulo. Esto activa el proceso de generación dinámica de vistas heredadas.

## Requisitos

- Es necesario que el nombre del módulo (`module_name`) se pase como parámetro al ejecutar la función `post_update_hook`.
- Los templates base deben estar correctamente definidos y asociados a las vistas originales mediante el modelo `ir.ui.view.hook`.

## Beneficios

- Automatización en la creación de vistas heredadas.
- Reducción de errores manuales al actualizar módulos.
- Propagación automática de traducciones entre templates y vistas heredadas.

