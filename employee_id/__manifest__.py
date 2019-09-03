# Copyright 2014-2015 Grupo ESOC <www.grupoesoc.es>
# Copyright 2017-Apertoso N.V. (<http://www.apertoso.be>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "EmployeeInfo",
    "summary": "Define certification for different purposes",
    'version': '12.0.1.0.0',
    "category":"Certification  Management",
    "website": "https://github.com/klcftm",
    "author": "Fatma Kılıç, İlknur Unal",
    "license": "AGPL-3",
    "depends": [
        'base','hr'
    ],
    "data": [ 'security/ir.model.access.csv',
              'views/employee_info_view.xml',


    ],
    'development_status':'Beta',
    'maintainers':['ceeficent'],
}
