class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        from collections import deque

        dires = deque()
        radiants = deque()

        for idx in range(len(senate)):
            if senate[idx] == 'R':
                radiants.append(idx)
            else:
                dires.append(idx)

        new_idx = len(senate)
        while dires and radiants:
            dire = dires.popleft()
            radiant = radiants.popleft()

            if dire < radiant:
                dires.append(new_idx)
            else:
                radiants.append(new_idx)
            new_idx += 1

        return "Radiant" if radiants else "Dire"