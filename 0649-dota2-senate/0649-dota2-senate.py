class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        banned = [False] * len(senate)

        radiants_cnt_alive = senate.count("R")
        dires_cnt_alive = len(senate) - radiants_cnt_alive
        
        r_bans = 0
        d_bans = 0
        idx = 0
        while radiants_cnt_alive > 0 and dires_cnt_alive > 0:
            if idx >= len( senate) :
                idx = 0

            if banned[idx]:
                idx += 1
                continue

            if senate[idx] == "R":
                if d_bans > 0:
                    d_bans -= 1
                    banned[idx] = True
                    radiants_cnt_alive -= 1
                else:
                    r_bans += 1
            else:
                if r_bans > 0:
                    r_bans -= 1
                    banned[idx] = True
                    dires_cnt_alive -= 1
                else:
                    d_bans += 1
            idx += 1
        return "Radiant" if dires_cnt_alive == 0 else "Dire"