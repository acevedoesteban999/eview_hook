# Module`view_hook`

## `Odoo`:`18`

## Traduction de réadme

-   [Anglais](README.md)
-   [Espagnol](README.es.md)
-   [portugais](README.pt.md)
-   [Français](README.fr.md)

## But

Le`view_hook`Le module vise à faciliter la création dynamique de vues héritées (`inherit`) Dans Odoo lors de la mise à jour des modules. Ceci est particulièrement utile lorsque vous devez modifier ou étendre automatiquement les vues existantes en utilisant uniquement le modèle`key`, sans définir manuellement les vues héritées pour chaque mise à jour.

## Fonctionnalité

Le module utilise un modèle appelé`ir.ui.view.hook`qui définit deux champs principaux:

-   `template_name`: Le nom du modèle à utiliser comme base pour générer la vue héritée.
-   `inherit_key`: La clé de la vue à hériter.

La fonction principale du module est`post_update_hook`, qui est exécuté lorsqu'un module est mis à jour. Cette fonction effectue les étapes suivantes:

1.  Recherche d'enregistrements dans le`ir.ui.view.hook`modèle qui correspond au nom du module fourni.
2.  Pour chaque dossier trouvé:
    -   Récupère la vue originale (`inherit_key`) and the base template (`template_name`).
    -   Extrait le contenu du modèle de base et l'utilise pour créer une nouvelle vue héritée.
    -   Si une vue héritée avec le nom généré existe déjà, met à jour son contenu; Sinon, crée une nouvelle vue.
    -   Propage les traductions du modèle de base à la nouvelle vue héréditaire.

## Exemple d'utilisation

Vous trouverez ci-dessous un exemple de la façon de configurer le module pour générer dynamiquement les vues héritées:

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

### Exemple d'explication

1.  **Définition du crochet (`ir.ui.view.hook`)**:
    -   Spécifie le`template_name`, qui est le modèle de base.
    -   Définit le`inherit_key`, qui est la clé de la vue originale à hériter.

2.  **Modèle de base**:
    -   Le modèle contient les modifications à appliquer à la vue héritée.

3.  **Function Execution**:
    -   Le`post_update_hook`La fonction est exécutée avec le`module_name`Paramètre, qui indique le nom du module. Cela active le processus de génération dynamique des vues héréditaires uniquement pour ce module.

## Exigences

-   Le nom du module (`module_name`) must be passed as a parameter when executing the `post_update_hook`fonction.
-   Les modèles de base doivent être correctement définis et associés aux vues d'origine à travers le`ir.ui.view.hook`modèle.

## Avantages

-   Automatisation dans la création de vues héritées.
-   Réduction des erreurs manuelles lors de la mise à jour des modules.
-   Propagation automatique des traductions entre les modèles et les vues héritées.
