from odoo import models, fields,api



class AssignmentTool(models.Model):

    _name = 'assignment.tool'  # database name
    _description = 'It assignment tool'

    obj_id = fields.Char()
    user_name= fields.Many2one('hr.employee')
    obj_type=fields.Selection([
        ('computer',"Computer"),
        ('screen', "Screen"),
        ('keyboard_mouse', "Keyboard and Mouse"),
        ('network_computer', "Network Computer"),
        ('telephone', "Telephone"),
        ('printer', "Printer")

    ])
    date = fields.Date(string='Validation Date')
    assign_status = fields.Selection([
        ('valid', "Valid"),
        ('invalid', "Invalid")
    ], string='Assignment Status' )

    description = fields.Text(string='Assignment Details')





# -------------------------------------------------
