
import proj05
from cards import Card

############################################
#use these to test the different hand categories
##################################################

# Test flush
H1 = [Card(2,4),Card(5,4),Card(8,3),Card(11,3),Card(13,3),Card(1,3),Card(10,3)]
H2 = [Card(2,4),Card(5,4),Card(8,4),Card(11,3),Card(13,3),Card(1,3),Card(10,3)]
flush_list_H1 = [Card(1,3), Card(8,3), Card(10,3), Card(11,3),Card(13,3)]
print(proj05.is_flush(H1),"Expected:{}".format(flush_list_H1), proj05.is_flush(H1)==flush_list_H1) #1
#Test straight
H1 = [Card(10,4),Card(5,4),Card(1,3),Card(2,2),Card(3,1),Card(4,3),Card(6,3)]
H2 = [Card(2,4),Card(3,4),Card(4,4),Card(5,3),Card(13,3),Card(11,3),Card(10,3)]
straight_list_H1= [Card(1,3),Card(2,2),Card(3,1),Card(4,3),Card(5,4)]
print(proj05.is_straight(H1),"Expected:{}".format(straight_list_H1), proj05.is_straight(H1)==straight_list_H1) #2
# Test straight flush
H1 = [Card(10,4),Card(5,3),Card(1,3),Card(2,3),Card(3,3),Card(4,3),Card(6,3)]
H2 = [Card(2,4),Card(3,4),Card(4,4),Card(5,3),Card(13,3),Card(11,3),Card(10,3)]
straight_flush_H1 = [Card(1,3),Card(2,3),Card(3,3),Card(4,3),Card(5,3)]
print(proj05.is_straight_flush(H1),"Expected:{}".format(straight_flush_H1) , proj05.is_straight_flush(H1)==straight_flush_H1) #3
# Test four a kind
H1 = [Card(10,4),Card(2,1),Card(2,4),Card(2,2),Card(2,3),Card(4,3),Card(6,3)]
H2 = [Card(2,4),Card(3,4),Card(3,1),Card(3,3),Card(13,3),Card(11,3),Card(10,3)]
four_kind_list_H1 = [Card(2,1),Card(2,2),Card(2,3),Card(2,4)]
print(proj05.is_four_of_a_kind(H1),"Expected:{}".format(four_kind_list_H1),proj05.is_four_of_a_kind(H1)==four_kind_list_H1) #4
# Test full house
H1 = [Card(7,4),Card(5,1),Card(11,4),Card(3,2),Card(11,3),Card(7,2),Card(7,3)]
H2 = [Card(2,4),Card(5,4),Card(2,1),Card(3,3),Card(13,3),Card(11,3),Card(10,3)]
full_house_list_H1 = [Card(7,2),Card(7,3),Card(7,4), Card(11,3),Card(11,4)]
print(proj05.is_full_house(H1),"Expected:{}".format(full_house_list_H1), proj05.is_full_house(H1)==full_house_list_H1)  #5
# Test three of a kind
H1 = [Card(10,4),Card(3,1),Card(4,4),Card(3,2),Card(3,3),Card(4,3),Card(6,3)]
H2 = [Card(2,4),Card(3,4),Card(3,1),Card(2,3),Card(13,3),Card(11,3),Card(10,3)]
three_kind_list_H1 = [Card(3,1),Card(3,2),Card(3,3)]
print(proj05.is_three_of_a_kind(H1),"Expected:{}".format(three_kind_list_H1),proj05.is_three_of_a_kind(H1)==three_kind_list_H1) #6
# Test two pair
H1 = [Card(10,4),Card(3,1),Card(4,4),Card(3,2),Card(4,3),Card(5,2),Card(6,3)]
H2 = [Card(2,4),Card(3,4),Card(3,1),Card(3,3),Card(13,3),Card(11,3),Card(10,3)]
two_pair_list_H1 = [Card(3,1),Card(3,2),Card(4,3),Card(4,4)]
print(proj05.is_two_pair(H1),"Expected:{}".format(two_pair_list_H1),proj05.is_two_pair(H1)==two_pair_list_H1) #7
# Test one pair
H1 = [Card(10,4),Card(3,1),Card(11,4),Card(7,2),Card(11,3),Card(5,2),Card(6,3)]
H2 = [Card(2,4),Card(5,4),Card(7,1),Card(3,3),Card(13,3),Card(11,3),Card(10,3)]
one_pair_test_H1= [Card(11,3),Card(11,4)]
print(proj05.is_one_pair(H1),"Expected:{}".format(one_pair_test_H1),proj05.is_one_pair(H1)==one_pair_test_H1) #8


