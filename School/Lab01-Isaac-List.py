# Isaac List  - CS150, 09-07-2018
#
# This program finds the area of a circle given
# an arbitrary radius.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# Want a floating point number
radius = float(input("Radius"))

# Does python have a pi definition somewhere?
pi = 3.14159

# A=pi*r^2
area = pi*(radius**2)

# Finding the volume of a sphere
volume = (4/3)*pi*(radius**3)

# Print the result
print("The area is:", area)
print("The volume is:", volume)
