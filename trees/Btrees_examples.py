# -*- coding: utf-8 -*-
"""
Examples of B-trees 
"""

from algopy import btree

# first in tutorial, degree = 3
s0 = '(<40>(<7,20,35>(<2,5,6>)(<13,14,15,16>)(<22,27,29,30>)(<36,39>))(<72,83>(<42,51>)(<79,81>)(<87,91,93,96,99>)))'
B0 = btree.fromlist(s0, 3)



# second in tutorial, ex 1.4 q1 degree = 2
s2 = "(<22>(<15>(<8,12>)(<18,19,20>))(<27,41>(<24,25>)(<30,35,38>)(<45,48>)))"
B2 = btree.fromlist(s2, 2)

# ex 1.4 q2, degree = 2
s1 = "(<13,32,44>(<3>)(<18,25>)(<35,40>)(<46,49,50>))"
B1 = btree.fromlist(s1, 2)

# another degree = 3
ex = "(<20>(<8,15>(<1,2,3,4,5>)(<9,13>)(<16,17,18,19>))(<26,42,53>(<21,25>)(<27,34,35,41>)(<43,48,51,52>)(<62,65,77>)))"
B3 = btree.fromlist(ex, 3)

#ex for split
exSplit = "(<20>(<8,15>(<1,2,3,4,5>)(<9,13>)(<16,17,18,19>))(<26,34,42,48,53>(<21,25>)(<27,31>)(<35,41>)(<43,47>)(<51,52>)(<62,65,77>)))"
Bsplit = btree.fromlist(exSplit, 3)
