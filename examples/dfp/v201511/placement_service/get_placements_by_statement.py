#!/usr/bin/python
#
# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This code example gets all active placements by using a statement.

To create a placement, run create_placements.py.
"""


# Import appropriate modules from the client library.
from googleads import dfp


def main(client):
  # Initialize appropriate service.
  placement_service = client.GetService('PlacementService', version='v201511')

  # Create a statement to only select active placements.
  values = [{
      'key': 'status',
      'value': {
          'xsi_type': 'TextValue',
          'value': 'ACTIVE'
      }
  }]
  query = 'WHERE status = :status'
  statement = dfp.FilterStatement(query, values)

   # Get placements by statement.
  while True:
    response = placement_service.getPlacementsByStatement(
        statement.ToStatement())
    if 'results' in response:
      # Display results.
      for placement in response['results']:
        print ('Placement with id \'%s\' and name \'%s\' was found.'
               % (placement['id'], placement['name']))
      statement.offset += dfp.SUGGESTED_PAGE_LIMIT
    else:
      break

  print '\nNumber of results found: %s' % response['totalResultSetSize']

if __name__ == '__main__':
  # Initialize client object.
  dfp_client = dfp.DfpClient.LoadFromStorage()
  main(dfp_client)
