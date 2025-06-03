# Módulo`view_hook`

## Enquanto:`18`

## Propósito

O`view_hook`O módulo pretende facilitar a criação dinâmica de visões herdadas (`inherit`) no Odoo ao atualizar os módulos. Isso é especialmente útil quando você precisa modificar ou estender as visualizações existentes automaticamente usando apenas o modelo`key`, sem definir manualmente as visualizações herdadas para cada atualização.

## Functionality

O módulo usa um modelo chamado`ir.ui.view.hook`que define dois campos principais:

-   `template_name`: O nome do modelo a ser usado como base para gerar a visualização herdada.
-   `inherit_key`: A chave da visão a ser herdada.

A principal função do módulo é`post_update_hook`, que é executado quando um módulo é atualizado. Esta função executa as seguintes etapas:

1.  Procura registros no`ir.ui.view.hook`modelo que corresponde ao nome do módulo fornecido.
2.  Para cada registro encontrado:
    -   Recupera a visão original (`inherit_key`) e o modelo base (`template_name`).
    -   Extrai o conteúdo do modelo base e o usa para criar uma nova visualização herdada.
    -   Se já existir uma visão herdada com o nome gerado, atualiza seu conteúdo; Caso contrário, cria uma nova visão.
    -   Propaga as traduções do modelo base para a nova visualização herdada.

## Exemplo de uso

Abaixo está um exemplo de como configurar o módulo para gerar dinamicamente visões herdadas:

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

### Exemplo de explicação

1.  **Definição de gancho (`ir.ui.view.hook`)**:
    -   Especifica o`template_name`, que é o modelo base.
    -   Define o`inherit_key`, que é a chave da visão original a ser herdada.

2.  **Modelo base**:
    -   O modelo contém as modificações a serem aplicadas à visão herdada.

3.  **Execução da função**:
    -   O`post_update_hook`A função é executada com o`module_name`parâmetro, que indica o nome do módulo. Isso ativa o processo de geração dinâmica de visualizações herdadas apenas para este módulo.

## Requisitos

-   O nome do módulo (`module_name`) deve ser passado como um parâmetro ao executar o`post_update_hook`função.
-   Os modelos básicos devem ser definidos corretamente e associados às visualizações originais através do`ir.ui.view.hook`modelo.

## Benefícios

-   Automação na criação de visões herdadas.
-   Redução de erros manuais ao atualizar os módulos.
-   Propagação automática de traduções entre modelos e visões herdadas.
