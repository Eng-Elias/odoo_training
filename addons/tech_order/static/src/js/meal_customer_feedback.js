odoo.define('client_act.meal_customer_feedback', function (require) {
   'use strict';
   var AbstractAction = require('web.AbstractAction');
   var core = require('web.core');
   var rpc = require('web.rpc');
   var QWeb = core.qweb;
   var MealCustomerFeedback = AbstractAction.extend({
   template: 'MealCustomerFeedbackTemplate',
       events: {
       },
       init: function(parent, action) {
           this._super(parent, action);
       },
       start: function() {
           var self = this;
           self.load_data();
       },
       load_data: function () {
           var self = this;
                   //var self = this;
                   self._rpc({
                       model: 'customer.feedback',
                       method: 'get_meal_customer_feedback_data',
                       args: [],
                   }).then(function(data) {
                       self.$('.table_view').html(QWeb.render('FeedBackTable', {
                                  report_lines : data,
                       }));
                   });
           },
   });
   core.action_registry.add("meal_customer_feedback", MealCustomerFeedback);
   return SaleCustom;
});
