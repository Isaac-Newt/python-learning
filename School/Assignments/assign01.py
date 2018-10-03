#
# Isaac List - CS150 09-12-2018
#
# Furlongs per Fortnight
# This program converts a given in Furlongs/Fortnight to Knots
#
# Comments explain each step taken
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

def conversion(value):
    # fortnight = 14 days
    furlongsPerDay = value / 14
    # furlong = 1/8mi
    milesPerDay = furlongsPerDay / 8
    # mile = 5280ft
    feetPerDay = milesPerDay * 5280
    # ft = 12in
    inchesPerDay = feetPerDay * 12
    # in  = 2.54cm
    cmPerDay = inchesPerDay * 2.54
    # m = 100cm
    metersPerDay = cmPerDay / 100
    # nm = 1852m
    nmPerDay = metersPerDay / 1852
    # knots = nm/hr
    knots = nmPerDay / 24

    return knots

fpfInupt = float(input("Enter a speed in Furlongs per Fortnight: "))

knots = conversion(fpfInput)

print(fpfInput, "Furlongs per Fortnight = ", knots, "Knots")
