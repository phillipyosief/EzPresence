from dearpygui.core import *
from dearpygui.simple import *

from src.ui.UI import *


class Donate:
    @staticmethod
    def close():
        close_popup('Donate philliphqs')

    @staticmethod
    def close_hqs():
        close_popup('Donate hqsartworks')

    @staticmethod
    def show():
        """
        Shows the "Donate" popup with all GUI content

        @return:
        """
        add_text('DonateTitle', default_value='Thank you for your donation!')
        add_separator()
        add_text('PayWith', default_value='Pay with...')
        Buttons.create('DonatePayPalButton', 'MEDIUM', 'PayPal', None)
        Buttons.create('DonateCreditcardButton', 'MEDIUM', 'Creditcard', None)
        Buttons.create('DonatePaysafecardButton', 'MEDIUM', 'paysafecard', None)
        Buttons.create('DonateiDEALButton', 'MEDIUM', 'iDEAL', None)
        Buttons.create('DonateKlarnaButton', 'MEDIUM', 'Klarna', None)

        add_text('DonateGermany', default_value='Germany')
        Buttons.create('DonateGiropayButton', 'MEDIUM', 'Giropay', None)

        add_text('DonateMostEurope', default_value='Some europe countries')
        set_item_tip('DonateMostEurope', 'Belgia, Germany, Italia, Netherlands, Austria, Poland, Swiss, Spain, UK')
        Buttons.create('DonateSOFORTButton', 'MEDIUM', 'Pay now', None)

        add_separator()

        Buttons.create('DonateCloseButton', 'MEDIUM', 'Close', Donate.close)

    @staticmethod
    def show_hqs():
        """
        Shows the "Donate" popup with all GUI content

        @return:
        """
        add_text('DonateHQSTitle', default_value='Thank you for your donation!')
        add_separator()
        add_text('HQSPayWith', default_value='Pay with...')
        Buttons.create('DonateHQSPayPalButton', 'MEDIUM', 'PayPal', None)
        Buttons.create('DonateHQSCreditcardButton', 'MEDIUM', 'Creditcard', None)
        Buttons.create('DonateHQSPaysafecardButton', 'MEDIUM', 'paysafecard', None)
        Buttons.create('DonateHQSiDEALButton', 'MEDIUM', 'iDEAL', None)
        Buttons.create('DonateHQSKlarnaButton', 'MEDIUM', 'Klarna', None)

        add_text('DonateHQSGermany', default_value='Germany')
        Buttons.create('DonateHQSGiropayButton', 'MEDIUM', 'Giropay', None)

        add_text('DonateHQSMostEurope', default_value='Some europe countries')
        set_item_tip('DonateHQSMostEurope', 'Belgia, Germany, Italia, Netherlands, Austria, Poland, Swiss, Spain, UK')
        Buttons.create('DonateHQSSOFORTButton', 'MEDIUM', 'Pay now', None)

        add_separator()

        Buttons.create('DonateHQSCloseButton', 'MEDIUM', 'Close', Donate.close_hqs)
