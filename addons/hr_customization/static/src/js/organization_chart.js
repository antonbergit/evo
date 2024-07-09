odoo.define('employee_position.organization_chart', function(require) {
    'use strict';

    const FormController = require('web.FormController');
    const viewRegistry = require('web.view_registry');
    const FormView = require('web.FormView');

    const OrganizationChartController = FormController.extend({
        pass
    });

    const OrganizationChartView = FormView.extend({
        config: _.extend({}, FormView.prototype.config, {
            Controller: OrganizationChartController,
        }),
    });

    viewRegistry.add('organization_chart', OrganizationChartView);
});
