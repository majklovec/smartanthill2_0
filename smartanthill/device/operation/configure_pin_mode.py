# Copyright (C) 2015 OLogN Technologies AG
#
# This source file is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License version 2
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from smartanthill.api.handler import APIPermission
from smartanthill.device.api import APIDeviceHandlerBase
from smartanthill.device.arg import PinArg, PinModeArg
from smartanthill.device.operation.base import OperationBase, OperationType


class APIHandler(APIDeviceHandlerBase):

    PERMISSION = APIPermission.UPDATE
    KEY = "device.pinmode"
    REQUIRED_PARAMS = ("devid", "pin[]")

    def handle(self, data):
        return self.launch_operation(data['devid'],
                                     OperationType.CONFIGURE_PIN_MODE, data)


class Operation(OperationBase):

    TYPE = OperationType.CONFIGURE_PIN_MODE

    def process_data(self, data):
        args = []
        for _key, _value in data.items():
            if "pin[" not in _key:
                continue
            pinarg = PinArg(*self.board.get_pinarg_params())
            pinmodearg = PinModeArg(*self.board.get_pinmodearg_params())
            pinarg.set_value(_key[4:-1])
            pinmodearg.set_value(_value)
            args += [pinarg, pinmodearg]
        return [a.get_value() for a in args]
