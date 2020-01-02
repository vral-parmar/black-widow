"""
*********************************************************************************
*                                                                               *
* abstract_sniffing_view.py -- Django Abstract Sniffing view.                   *
*                                                                               *
********************** IMPORTANT BLACK-WIDOW LICENSE TERMS **********************
*                                                                               *
* This file is part of black-widow.                                             *
*                                                                               *
* black-widow is free software: you can redistribute it and/or modify           *
* it under the terms of the GNU General Public License as published by          *
* the Free Software Foundation, either version 3 of the License, or             *
* (at your option) any later version.                                           *
*                                                                               *
* black-widow is distributed in the hope that it will be useful,                *
* but WITHOUT ANY WARRANTY; without even the implied warranty of                *
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                 *
* GNU General Public License for more details.                                  *
*                                                                               *
* You should have received a copy of the GNU General Public License             *
* along with black-widow.  If not, see <http://www.gnu.org/licenses/>.          *
*                                                                               *
*********************************************************************************
"""

import os

from app.env import APP_STORAGE_OUT
from app.helper import storage

from app.gui.web.black_widow.view.abstract_view import AbstractView


class AbstractSniffingView(AbstractView):
    """
    Abstract Sniffing View
    """
    storage_out_dir = os.path.join(APP_STORAGE_OUT, 'sniffing')
    storage.check_folder(storage_out_dir)
    if not os.access(storage_out_dir, os.X_OK):
        os.chmod(storage_out_dir, 0o0755)
