# Copyright 2021 Google LLC
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


from unittest import result


def show_results(input_values):
    # New York, California, Georgia, Washington, South Dakota 
    score_key = {'New York': 'Albany', 'California': 'Sacramento','Georgia': 'Atlanta', 'Washington': 'Seatle','South Dakota': 'Pierre'}
    result = {}
    for state, capital in input_values:
        if(score_key[state] != capital):
            result[state] = f'{capital} is not the capital of {state}. ❌ '
        else:
            result[state] = f'{capital} is the capital of {state}. ✅'
    return result
