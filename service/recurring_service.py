"""
  Copyright (C) 2020 Seerbit

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """
from interface.app_interface import IClientConstants
from interface.service_interface import IRecurringService
from service.service import Service


class RecurringService(Service, IRecurringService, IClientConstants):

    def create_subscription(self, subscription):
        pass

    def get_customer_subscriptions(self, public_key, customer_id):
        pass

    def update_subscription(self, subscription):
        pass

    def get_merchant_subscriptions(self, public_key):
        pass

    def recurring_debit(self, recurring_debit):
        pass
