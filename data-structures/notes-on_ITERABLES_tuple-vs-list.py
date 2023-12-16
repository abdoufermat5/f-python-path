
##################################################################
# Execute the following code in a terminal with python installed #
##################################################################
from dis import dis

# tuple compile
dis(compile("(1,5,7,'ert')", "", "eval"))
# Output:
##################################################################
#   1             0 LOAD_CONST               0 ((1, 5, 7, 'ert'))
#                 2 RETURN_VALUE

# list compile
dis(compile("[1,5,7, 'ert']", "", "eval"))
# Output:
##################################################################
#   1           0 LOAD_CONST               0 (1)
#               2 LOAD_CONST               1 (5)
#               4 LOAD_CONST               2 (7)
#               6 LOAD_CONST               3 ('ert')
#               8 BUILD_LIST               4
#              10 RETURN_VALUE


"""
As we can see the tuple are more efficient compared to list as they are referenced only once while every 
element of a list considered apart.
"""



