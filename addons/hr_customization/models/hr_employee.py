from odoo import models, fields, api

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    # Moving fields
    work_address = fields.Char(string="Work Address")
    tz = fields.Selection(string="Timezone")

    # New field
    pension_fund_tax = fields.Boolean(string="Pension Fund Tax")

    # Hiding standard fields
    # department_id = fields.Many2one('hr.department', string='Department', invisible=True)
    # job_id = fields.Many2one('hr.job', string='Job Position', invisible=True)
    # parent_id = fields.Many2one('hr.employee', string='Manager', invisible=True)
    # coach_id = fields.Many2one('hr.employee', string='Coach', invisible=True)





#   readonly=True


