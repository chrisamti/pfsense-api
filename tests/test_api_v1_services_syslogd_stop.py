# Copyright 2023 Jared Hendrickson
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
"""Script used to test the /api/v1/services/syslogd/stop endpoint."""
import e2e_test_framework


class APIE2ETestServicesSyslogdStop(e2e_test_framework.APIE2ETest):
    """Class used to test the /api/v1/services/syslogd/stop endpoint."""
    uri = "/api/v1/services/syslogd/stop"
    post_privileges = ["page-all", "page-status-services"]
    post_tests = [{"name": "Stop the syslogd service"}]


APIE2ETestServicesSyslogdStop()
