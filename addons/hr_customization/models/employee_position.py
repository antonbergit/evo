from odoo import models, fields, api

class EmployeePosition(models.Model):
    _name = 'employee.position'
    _description = 'Employee Position'

    employee_id = fields.Many2one('hr.employee', string='Employee')
    date_start = fields.Date(string='Date Start')
    date_end = fields.Date(string='Date End')
    job_id = fields.Many2one('hr.job', string='Job Position', domain="[('department_id', '=', department_id)]")
    department_id = fields.Many2one('hr.department', string='Department')


    manager_id = fields.Many2one('hr.employee', string='Manager')
    coach_id = fields.Many2one('hr.employee', string='Coach')
    employee_type = fields.Selection([('permanent', 'Permanent'), ('contract', 'Contract'), ('intern', 'Intern')], string='Employee Type')
    current_contract_id = fields.Many2one('hr.contract', string='Current Contract', domain="[('employee_id', '=', employee_id), ('job_id', '=', job_id)]")
    work_location_id = fields.Many2one('hr.work.location', string='Work Location')
    working_hours = fields.Float(string='Working Hours', compute='_compute_working_hours')

    @api.depends('job_id')
    def _compute_working_hours(self):
        for record in self:
            record.working_hours = record.job_id.working_hours_per_week

  
    vacation_supervisor_id = fields.Many2one('res.users', string='Vacation (Direct Supervisor)', domain="[('time_off_manager', '=', 'Administrator')]")
    vacation_hr_manager_id = fields.Many2one('res.users', string='Vacation (HR manager)', domain="[('time_off_manager', '=', 'Administrator')]")
    expenses_manager_id = fields.Many2one('res.users', string='Expenses')
