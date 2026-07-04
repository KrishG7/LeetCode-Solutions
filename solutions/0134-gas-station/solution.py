class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Rule 1: If overall gas is less than overall cost, it's impossible
        if sum(gas) < sum(cost):
            return -1
            
        current_tank = 0
        start_index = 0
        
        for i in range(len(gas)):
            # Add whatever gas we gain, and subtract what it costs to move forward
            current_tank += gas[i] - cost[i]
            
            # Rule 2: If our tank goes negative, we failed to reach station i + 1.
            if current_tank < 0:
                # The next possible valid starting point is the station AFTER the failure
                start_index = i + 1
                # Reset our tank for the new journey
                current_tank = 0
                
        # Because we already checked Rule 1, if we made it here, 
        # start_index is guaranteed to be the one unique solution.
        return start_index
