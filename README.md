# language-scripts
Set of scripts for language analysis

## f0.py
This script extracts the fundamental frequency (f0) values of specific labeled intervals (vowels or 'ん') from a given TextGrid file and audio (WAV) file. The extracted data is then written to a CSV file with details about each interval's start time, end time, and corresponding average f0 value.

## f0_10ms.py
This script extracts the fundamental frequency (f0) values of specific labeled intervals (vowels or 'ん') from a given TextGrid file and audio (WAV) file. The extracted data is then written to a CSV file with details about each interval's start time, end time, and corresponding f0 value of each interval every 10 ms.

## number_word.py
This script provides a utility to modify a given Praat TextGrid file. Specifically, it iterates through the intervals in the 'token' tier and appends an index number to repeated tokens to differentiate them.

## check_textgrids_word.py
This script processes TextGrid files, which are commonly used in phonetics and linguistics to annotate speech. The main purpose of this script is to extract and print tokens that do not have exactly two occurrences in a specified tier.


Copyright (c) 2023 K.I.

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
