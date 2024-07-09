from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'


    work_address_id = fields.Many2one('res.partner', string='Work Address')
    tz = fields.Selection(related='resource_id.tz', string='Timezone', readonly=False)
    pension_fund_tax = fields.Boolean(string='Pension Fund Tax')


    department_id = fields.Many2one('hr.department', string='Department', groups="base.group_user", invisible=True)
    job_id = fields.Many2one('hr.job', string='Job Position', groups="base.group_user", invisible=True)
    parent_id = fields.Many2one('hr.employee', string='Manager', groups="base.group_user", invisible=True)
    coach_id = fields.Many2one('hr.employee', string='Coach', groups="base.group_user", invisible=True)

    position_ids = fields.One2many('employee.position', 'employee_id', string='Positions')

    vacation_days_total = fields.Integer(string='Total Vacation, days', readonly=True)
    vacation_days_used = fields.Integer(string='Used Vacation, days', readonly=True)
    vacation_days_rest = fields.Integer(string='Rest of Vacation, days', readonly=True)
    note = fields.Text(string='Note')

   
    child_ids = fields.One2many('hr.employee', 'parent_id', string='Direct Subordinates')







# from odoo import models, fields, api

# class HrEmployee(models.Model):
#     _inherit = 'hr.employee'

#     position_ids = fields.One2many('hr.employee.position', 'employee_id', string="Positions")

    
#     work_address = fields.Char(string="Work Address")
#     tz = fields.Selection(string="Timezone")
#     pension_fund_tax = fields.Boolean(string="Pension Fund Tax")

# class HrEmployeePosition(models.Model):
#     _name = 'hr.employee.position'
#     _description = 'Employee Position'

#     employee_id = fields.Many2one('hr.employee', string="Employee")
#     date_start = fields.Date(string="Start Date")
#     date_end = fields.Date(string="End Date")
#     job_id = fields.Many2one('hr.job', string="Job Position")
#     department_id = fields.Many2one('hr.department', string="Department")
#     manager_id = fields.Many2one('hr.employee', string="Manager")
#     coach_id = fields.Many2one('hr.employee', string="Coach")
#     employee_type = fields.Selection([
#         ('employee', 'Employee'),
#         ('student', 'Student'),
#         ('trainee', 'Trainee'),
#         ('contractor', 'Contractor'),
#         ('freelance', 'Freelancer')
#     ], string='Employee Type', default='employee')
#     current_contract_id = fields.Many2one('hr.contract', string="Current Contract")
#     work_location = fields.Char(string="Work Location")
#     working_hours = fields.Float(string="Working Hours")
#     vacation_direct_supervisor_id = fields.Many2one('hr.employee', string="Vacation Direct Supervisor")
#     vacation_hr_manager_id = fields.Many2one('hr.employee', string="Vacation HR Manager")
#     expenses_id = fields.Many2one('hr.expense', string="Expenses")
#     pension_scheme = fields.Char(string="Pension Scheme")
#     taxes = fields.Char(string="Taxes")
#     insurance_company = fields.Char(string="Insurance Company")
#     insurance_fee = fields.Float(string="Insurance Fee")
#     other_benefits = fields.Text(string="Other Benefits")
#     total_vacation_days = fields.Float(string="Total Vacation Days")
#     used_vacation_days = fields.Float(string="Used Vacation Days")
#     rest_vacation_days = fields.Float(string="Remaining Vacation Days")
#     note = fields.Text(string="Note")