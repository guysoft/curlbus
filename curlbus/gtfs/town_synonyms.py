"gtfs/town_synonyms.py: catch synonym of town names"
# Copyright (C) 2018 Elad Alfassa <elad@fedoraproject.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import re
# This dictionary is key'd on the official town name translation
# and the values are compiled regex objects to match variations of the town name
towns = {"Tel Aviv Yafo": re.compile("Tel[- ]Aviv([- ]Yafo)?", re.I),
         "Modi'in-Makabim-Re'ut": re.compile("Modi'in([- ]Ma[kc]abim[- ]Re'ut)?")}
