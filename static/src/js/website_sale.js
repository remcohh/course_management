/** @odoo-module alias=course_management.js**/

import { WebsiteSale } from '@website_sale/js/website_sale';

WebsiteSale.include({
    events: Object.assign({}, WebsiteSale.prototype.events, {
        'click #add_product_waitinglist': '_onClickAddProductWaitinglist',
    }),

    _onClickAddProductWaitinglist: function (ev) {

      const partnerEmail = document.querySelector('#wsale_user_email').value;
      const email = partnerEmail;
      this._rpc({
        route: "/shop/add/stock_notification",
        params: {
            product_id: productId,
            email,
        },
    }).then((data) => {
        const message = stockNotificationEl.querySelector('#stock_notification_success_message');

        message.classList.remove('d-none');
        formEl.classList.add('d-none');
    }).catch((error) => {
        this._displayEmailIncorrectMessage(stockNotificationEl);
    });
      
    }
});

export default WebsiteSale;
