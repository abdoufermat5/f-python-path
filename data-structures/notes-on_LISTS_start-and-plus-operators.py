# Be careful with the star operator when initializing lists
import dis

list_of_3_length_lists = [[]] * 3
# This is a list of three references to the same list object, so if you change one, you change them all

list_of_3_length_lists_ = [[] for _ in range(3)]
# This is a list of three separate lists, so if you change one, you don't change the others

# Be careful again, a tempting but wrong shortcut would be
list_of_3_length_lists__ = [[]*3] * 3
# This is a list of three references to the same list object, so if you change one, you change them all

# Weird fact about inplace assignment
t = (1, 2, [30, 40])
t[2] += [50, 60]
# This will raise an exception because t[2] is a list and += is an inplace operation
# But the list in the tuple will be changed anyway
# This because the t[2] is first pushed on the stack, then the += operation is performed, then the result is
# assigned to t[2] which fails
dis.dis("t[2] += [50, 60]")
# Output:
#  1           0 LOAD_NAME                0 (t)
#              2 LOAD_CONST               0 (2)
#              4 DUP_TOP_TWO        <--- t[2] is pushed on the stack
#              6 BINARY_SUBSCR
#              8 LOAD_CONST               1 (50)
#             10 LOAD_CONST               2 (60)
#             12 BUILD_LIST               2
#             14 INPLACE_ADD       <--- += operation
#             16 ROT_THREE
#             18 STORE_SUBSCR     <--- assignment
#             20 LOAD_CONST               3 (None)        <--- assignment fails
#             22 RETURN_VALUE
# So the list is changed but the assignment fails
# So we should avoid using mutable objects in immutable objects
