# Copyright 2014-2015 Grupo ESOC <www.grupoesoc.es>
# Copyright 2017-Apertoso N.V. (<http://www.apertoso.be>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "It Assignment",
    "summary": "Define certification for different purposes",
    'version': '12.0.1.0.0',
    "category":"Management",
    "website": "https://github.com/klcftm",
    "author": "Fatma Kılıç,Selehattin Mücahit Keskin,Selim Has",
    "license": "AGPL-3",
    "depends": [
        'base','hr'
    ],
    "data": [
              'security/ir.model.access.csv',
              'views/assignment_tool_view.xml',
              'views/user_view.xml',




    ],
   
    'development_status':'Beta',
    'maintainers':['ceeficent'],
    'installable': True,
    'application': True,
}
