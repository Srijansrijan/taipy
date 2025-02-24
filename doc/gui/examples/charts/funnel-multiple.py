# Copyright 2021-2024 Avaiga Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
# -----------------------------------------------------------------------------------------
# To execute this script, make sure that the taipy-gui package is installed in your
# Python environment and run:
#     python <script>
# -----------------------------------------------------------------------------------------
from taipy.gui import Gui

if __name__ == "__main__":
    data = {
        "Types": ["Website visit", "Downloads", "Prospects", "Invoice sent", "Closed"],
        "Visits_us": [13873, 10533, 5443, 2703, 908],
        "Visits_eu": [7063, 4533, 3443, 1003, 1208],
        "Visits_ap": [6873, 2533, 3443, 1703, 508],
    }

    # Columns for each trace
    x = ["Visits_us", "Visits_eu", "Visits_ap"]

    # Legend text for each trace
    names = ["US", "EU", "AP"]

    page = """
# Funnel - Multiple traces

<|{data}|chart|type=funnel|x={x}|y=Types|name={names}|>
    """

    Gui(page).run()
