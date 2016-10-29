'''
There are three doors, behind one of which there is a pize. 
- You choose a door
- A door that you have not chosen is revealed to be an empty one.
- There are two doors left: the one that you have chosen initially and another.
- Do you switch doors in order to increase your chances of winning?
'''

from random import randint

def main():
    doors =  ['A', 'B', 'C']

    def set_winner_door():
        '''
        Decide which door hides the prize. Return name of door.
        '''
        winner = doors[randint(0,len(doors)-1)]
        return winner

    def get_chosen_door():
        '''
        Decide which door the player picks. Return name of door.
        '''
        chosen = doors[randint(0,len(doors)-1)]
        return chosen

    def check_result():
        '''
        Check if player has chosen the winner door. Return True or False
        '''
        winner = set_winner_door()
        chosen = get_chosen_door()
        return winner == chosen

    def get_statistics(n):
        '''
        Check the number of wins in n trials, assuming the player hasn't switched doors.
        '''
        won = 0
        for i in range(n):
            if check_result():
                won += 1
        return won/n

    def reveal_door():
        '''
        Reveal a door that is not the winner. Copies the original list and makes a new one 
        with the string 'revealed' in the place of a non-winner door.
        '''
        local_doors = doors.copy()
        chosen = get_chosen_door()
        winner = set_winner_door()
        for index in range(len(local_doors)):
            if local_doors[index] != chosen and local_doors[index] != winner:
                local_doors[index] = 'revealed'
                break
        return local_doors, chosen, winner
    
    def switch_door():
        '''
        Modify the choice of the player.
        Return choice and winner.
        '''
        revealed_doors, chosen, winner = reveal_door()
        for door in revealed_doors:
            if door != 'revealed' and door != chosen:
                chosen = door
                break
        return chosen, winner
            
    
    def check_switched_result():
        '''
        Check if the chosen door is the winner. Return True or False.
        '''
        chosen, winner = switch_door()
        return chosen == winner
        
    def get_statistics_for_switched(n):
        '''
        Check the number of wins in n trials, assuming the player has switched doors.
        '''
        won = 0
        for i in range(n):
            check = check_switched_result()
            if check:
                won += 1
        return won / n
        
    
    print('If you do not switch doors, you have a ', get_statistics(100000) *100, '% chance of winning')
    print('If you do switch doors, you have a     ', get_statistics_for_switched(100000)*100, '% chance of winning')

    
        
    
# def get_probability_of_winning():
