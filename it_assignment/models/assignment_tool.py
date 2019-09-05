from odoo import models, fields,api



class AssignmentTool(models.Model):

    _name = 'assignment.tool'  # database name
    _description = 'It assignment tool'

    obj_id = fields.Integer(string = "Object ID")
    user_name= fields.Many2one('res.users', 'Employee', default=lambda self: self.env.user.id, readonly=True)
    obj_type=fields.Selection([
        ('computer',"Computer"),
        ('screen', "Screen"),
        ('keyboard_mouse', "Keyboard and Mouse"),
        ('network_computer', "Network Computer"),
        ('telephone', "Telephone"),
        ('printer', "Printer")

    ], string='Object Type')
    date = fields.Date(string='Validation Date')
    assign_status = fields.Selection([
        ('valid', "Valid"),
        ('invalid', "Invalid")
    ], string='Assignment Status', default="invalid" )

    description = fields.Text(string='Assignment Details')

    @api.multi
    def approve_assignment(self):
        '''
        This function opens a window to compose an email, with the edi purchase template message loaded by default
        '''
        self.ensure_one()
        current_employee = self.env['hr.employee'].search([('user_id', '=', self.env.uid)], limit=1)
        for i in self:
            i.write({'assign_status': 'valid', 'second_approver_id': current_employee.id})
        #	Eğer şu anki state validate1 ise state'i refuse olarak değiştirilir.

        return True

    @api.onchange('obj_type')
    @api.multi
    def onchangefunc(self):
        ass_env=self.env['assignment.tool'].search([])
        real_value = 0
        obje_turu = self.obj_type

        for i in ass_env:
            value = i.obj_id
            if value > real_value:
                real_value = value


        if  obje_turu == False:
            self.obj_id = 0
        else:
            self.obj_id = real_value + 1








# -------------------------------------------------
