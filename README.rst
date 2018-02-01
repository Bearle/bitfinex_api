============
Bitfinex API
============


.. image:: https://img.shields.io/pypi/v/bitfinex_api.svg
    :target: https://pypi.python.org/pypi/bitfinex_api

.. image:: https://img.shields.io/travis/delneg/bitfinex_api.svg
    :target: https://travis-ci.org/delneg/bitfinex_api

.. image:: https://readthedocs.org/projects/bitfinex-api/badge/?version=latest
    :target: https://bitfinex-api.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/delneg/bitfinex_api/shield.svg
    :target: https://pyup.io/repos/github/delneg/bitfinex_api/
     :alt: Updates


    AModern Python wrapper for Bitfinex api v1 & v2


    * Free software: MIT license
    * Documentation: https://bitfinex-api.readthedocs.io.


Features
--------

* TODO

Methods
--------------------------
**Bold** means that it's implemented, regular - it is not implemented.
Format is 'Docs method name - function_name'

v1
^^

1. General
    1.1 Account info
    1.2 Account fees
    1.3 Summary
    1.4 Deposit
    1.5 Key Permissions
    1.6 Margin Information
    1.7 Wallet Balances
    1.8 Transfer Between Wallets
    1.9 Withdrawal
2. Orders
    2.1 **New order - place_order**
    2.2 Multiple new orders
    2.3 **Cancel order - delete_order**
    2.4 Cancel multiple orders
    2.5 **Cancel all orders - delete_all_orders**
    2.6 Replace order
    2.7 **Order status - status_order**
    2.8 **Active orders - active_orders**
    2.9 Orders history
3. Positions
    3.1 **Active positions - active_positions**
    3.2 **Claim position - claim_position**
4. Historical data
    4.1 **Balance history - history**
    4.2 **Deposit-Withdrawal history - history_movements**
    4.3 **Past trade - past_trades**
5. Margin funding
    5.1 **New offer - place_offer**
    5.2 **Cancel offer - cancel_offer**
    5.3 **Offer status - status_offer**
    5.4 Active credits
    5.5 **Offers - active_offers**
    5.6 Offers history
    5.7 Past funding trades
    5.8 Active Funding Used in a margin position
    5.9 Active Funding Not Used in a margin position
    5.10 Total taken funds
    5.11 Total taken funds
    5.12 Close margin funding
    5.13 Basket manage
    5.14 Close position

v2
^^

None yet


TODO
----

* Implement rest of the methods for v1
* Start v2
* Throw special exception on permissions mismatch
Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

