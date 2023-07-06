#!/usr/bin/env python3
# ----------------------------------------------------------------------------
#
# Copyright 2018 EMVA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# ----------------------------------------------------------------------------


# Related third party imports
from PyQt5.QtCore import QRegExp
from PyQt5.QtWidgets import QAbstractSpinBox, QLineEdit
from PyQt5.QtGui import QRegExpValidator


class BigIntSpinBox(QAbstractSpinBox):

    def __init__(self, parent=None):
        super(BigIntSpinBox, self).__init__(parent)

        self._singleStep = 1
        self._minimum = -18446744073709551616
        self._maximum = 18446744073709551615

        self.lineEdit = QLineEdit(self)
        self.setLineEdit(self.lineEdit)

    def value(self):
        try:
            return int(self.lineEdit.text())
        except:
            raise
            return 0

    def setValue(self, value):
        if self._valueInRange(value):
            strValue = str(value)
            self.lineEdit.setText(strValue)

    def stepBy(self, steps):
        self.setValue(self.value() + steps*self.singleStep())

    def stepEnabled(self):
        return self.StepUpEnabled | self.StepDownEnabled

    def setSingleStep(self, singleStep):
        assert isinstance(singleStep, int)
        # don't use negative values
        self._singleStep = abs(singleStep)

    def singleStep(self):
        return self._singleStep

    def minimum(self):
        return self._minimum

    def setMinimum(self, minimum):
        assert isinstance(minimum, int) or isinstance(minimum, long)
        self._minimum = minimum

    def maximum(self):
        return self._maximum

    def setMaximum(self, maximum):
        assert isinstance(maximum, int) or isinstance(maximum, long)
        self._maximum = maximum

    def setRange(self, minimum, maximum):
        self.setMinimum(minimum)
        self.setMaximum(maximum)

    def _valueInRange(self, value):
        if value >= self.minimum() and value <= self.maximum():
            return True
        else:
            return False
