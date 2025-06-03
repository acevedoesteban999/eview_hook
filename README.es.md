# Módulo`view_hook`

## `Odoo`:`18`

## Traducción de lectura

-   [Inglés](README.md)
-   [Español](README.es.md)
-   [portugués](README.pt.md)
-   [Francés](README.fr.md)

## Objetivo

El`view_hook`El módulo tiene como objetivo facilitar la creación dinámica de vistas hereditarias (`inherit`) en Odoo al actualizar los módulos. Esto es especialmente útil cuando necesita modificar o extender las vistas existentes automáticamente usando solo la plantilla`key`, sin definir manualmente las vistas hereditarias para cada actualización.

## Funcionalidad

El módulo usa un modelo llamado`ir.ui.view.hook`que define dos campos principales:

-   `template_name`: El nombre de la plantilla que se utilizará como base para generar la vista hereditaria.
-   `inherit_key`: La clave de la vista a ser heredada.

La función principal del módulo es`post_update_hook`, que se ejecuta cuando se actualiza un módulo. Esta función realiza los siguientes pasos:

1.  Búsqueda de registros en el`ir.ui.view.hook`modelo que coincida con el nombre del módulo proporcionado.
2.  Para cada registro encontrado:
    -   Recupera la vista original (`inherit_key`) y la plantilla base (`template_name`).
    -   Extrae el contenido de la plantilla base y la usa para crear una nueva vista hereditaria.
    -   Si ya existe una vista hereditaria con el nombre generado, actualiza su contenido; De lo contrario, crea una nueva vista.
    -   Propagar las traducciones de la plantilla base a la nueva vista hereditaria.

## Ejemplo de uso

A continuación se muestra un ejemplo de cómo configurar el módulo para generar dinámicamente vistas heredadas:

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

### Explicación de ejemplo

1.  **Definición de gancho (`ir.ui.view.hook`)**:
    -   Especifica el`template_name`, que es la plantilla base.
    -   Define el`inherit_key`, que es la clave de la vista original a ser heredada.

2.  **Plantilla base**:
    -   La plantilla contiene las modificaciones que se aplicarán a la vista hereditaria.

3.  **Ejecución de la función**:
    -   El`post_update_hook`la función se ejecuta con el`module_name`Parámetro, que indica el nombre del módulo. Esto activa el proceso de generación dinámica de las vistas hereditarias solo para este módulo.

## Requisitos

-   El nombre del módulo (`module_name`) debe pasarse como parámetro al ejecutar el`post_update_hook`función.
-   Las plantillas base deben definirse correctamente y asociarse con las vistas originales a través del`ir.ui.view.hook`modelo.

## Beneficios

-   Automatización en la creación de vistas hereditarias.
-   Reducción de errores manuales al actualizar módulos.
-   Propagación automática de traducciones entre plantillas y vistas hereditarias.
