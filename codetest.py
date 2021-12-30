

def blackjack_hand_greater_than(hand_1,hand_2):
    
    hand_1_total_count = 0
    hand_2_total_count = 0
    
    
    for i in hand_1:
        if i == 'K' or i == 'J' or i == 'Q':
            hand_1_total_count = hand_1_total_count + 10
        elif i >= '10' and i != 'A':
            number1 = int(i)
            hand_1_total_count = hand_1_total_count + number1
        elif i == 'A':
            if hand_1_total_count > 11:
                hand_1_total_count = hand_1_total_count + 1
            else:
                hand_1_total_count = hand_1_total_count + 11
                
    if hand_1_total_count > 21 and hand_1.count('A') >= 1:
        hand_1_total_count = hand_1_total_count - (hand_1.count('A') * 11) + hand_1.count('A')
                
    for i in hand_2:
        if i == 'K' or i == 'J' or i == 'Q':
            hand_2_total_count = hand_2_total_count + 10
        elif i >= '10' and i != 'A':
            number2 = int(i)
            hand_2_total_count = hand_2_total_count + number2
        elif i == 'A':
            if hand_2_total_count > 11:
                hand_2_total_count = hand_2_total_count + 1
            else:
                hand_2_total_count = hand_2_total_count + 11
                
    if hand_2_total_count > 21 and hand_2.count('A') >= 1:
        hand_2_total_count = hand_2_total_count - (hand_2.count('A') * 11) + hand_2.count('A')
    
    if hand_1_total_count > 21:
        return False
    elif hand_1_total_count <= 21 and hand_1_total_count > hand_2_total_count or hand_2_total_count > 21:
        return True
    else:
        return False
    
    

x = blackjack_hand_greater_than(['2','8','3'], ['A', '4', '4', '7'])
print(x)