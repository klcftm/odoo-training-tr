from odoo import models, fields, api



class EmployeeInfo(models.Model):

    _name = 'employee.info'  # database name
    _description = 'Employee Info'

    name = fields.Many2one("hr.employee")
    identification_number = fields.Char()
    type = fields.Selection([
        ('passport_id', 'Passport'),
        ('card_id', 'Id Card'),
        ('driving_license', 'Driving License')
    ])
