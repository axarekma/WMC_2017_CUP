from .game import Game

class Cup_16:
    def __init__(self,rank,data,lanes):
        self.data = data
        self.lanes = lanes

        self.games = dict()
        self.games['G1'] = self.game(rank[1],rank[16],'F4')
        self.games['G2'] = self.game(rank[8],rank[9],'F7')
        self.games['G3'] = self.game(rank[5],rank[12],'F8')
        self.games['G4'] = self.game(rank[4],rank[13],'F12')
        self.games['G5'] = self.game(rank[3],rank[14],'F13')
        self.games['G6'] = self.game(rank[6],rank[11],'F15')
        self.games['G7'] = self.game(rank[7],rank[10],'F17')
        self.games['G8'] = self.game(rank[2],rank[15],'F18')
        #bo8
        self.games['G9'] = self.game(self.games['G1'].winner ,
                                self.games['G2'].winner,'F2')
        self.games['G10'] = self.game(self.games['G3'].winner ,
                                 self.games['G4'].winner,'F7')
        self.games['G11'] = self.game(self.games['G5'].winner ,
                                 self.games['G6'].winner,'F12')
        self.games['G12'] = self.game(self.games['G7'].winner ,
                                 self.games['G8'].winner,'F15')
        #bo4
        self.games['S1'] = self.game(self.games['G9'].winner ,
                                self.games['G10'].winner,'E1')
        self.games['S2'] = self.game(self.games['G11'].winner ,
                                self.games['G12'].winner,'E1')
        #bronze
        self.games['Bronze'] = self.game(self.games['S1'].loser ,
                                    self.games['S2'].loser,'E1')
        #bronze
        self.games['Final'] = self.game(self.games['S1'].winner ,
                                    self.games['S2'].winner,'E1')
        
    @property
    def winner(self):
        return self.games['Final'].winner
                
    @property
    def medals(self):
        return (self.games['Final'].winner,
               self.games['Final'].loser,
               self.games['Bronze'].winner)
    def game(self,p1,p2,k,MC = True):
        return Game(p1,p2,k,self.data,self.lanes,MC)

class Cup_32:
    def __init__(self,rank,data,lanes):
        self.data = data
        self.lanes = lanes

        self.games = dict()
        self.games['G1'] = self.game(rank[1],rank[32],'F4')
        self.games['G2'] = self.game(rank[16],rank[17],'F7')
        self.games['G3'] = self.game(rank[9],rank[24],'F8')
        self.games['G4'] = self.game(rank[8],rank[25],'F12')
        self.games['G5'] = self.game(rank[5],rank[28],'F13')
        self.games['G6'] = self.game(rank[12],rank[21],'F15')
        self.games['G7'] = self.game(rank[13],rank[20],'F17')
        self.games['G8'] = self.game(rank[4],rank[29],'F18')

        self.games['G9'] = self.game(rank[3],rank[30],'E1')
        self.games['G10'] = self.game(rank[14],rank[19],'E3')
        self.games['G11'] = self.game(rank[11],rank[22],'E4')
        self.games['G12'] = self.game(rank[6],rank[27],'E5')
        self.games['G13'] = self.game(rank[7],rank[26],'E12')
        self.games['G14'] = self.game(rank[10],rank[23],'E13')
        self.games['G15'] = self.game(rank[15],rank[18],'E14')
        self.games['G16'] = self.game(rank[2],rank[31],'E16')
        #bo8
        self.games['G17'] = self.game(self.games['G1'].winner ,
                                 self.games['G2'].winner,'E1')
        self.games['G18'] = self.game(self.games['G3'].winner ,
                                 self.games['G4'].winner,'E3')
        self.games['G19'] = self.game(self.games['G5'].winner ,
                                 self.games['G6'].winner,'E4')
        self.games['G20'] = self.game(self.games['G7'].winner ,
                                 self.games['G8'].winner,'E5')
        self.games['G21'] = self.game(self.games['G9'].winner ,
                                 self.games['G10'].winner,'E12')
        self.games['G22'] = self.game(self.games['G11'].winner ,
                                 self.games['G12'].winner,'E13')
        self.games['G23'] = self.game(self.games['G13'].winner ,
                                 self.games['G14'].winner,'E14')
        self.games['G24'] = self.game(self.games['G15'].winner ,
                                 self.games['G16'].winner,'E16')
        #bo8
        self.games['G25'] = self.game(self.games['G17'].winner ,
                                 self.games['G18'].winner,'E1')
        self.games['G26'] = self.game(self.games['G19'].winner ,
                                 self.games['G20'].winner,'E4')
        self.games['G27'] = self.game(self.games['G21'].winner ,
                                 self.games['G22'].winner,'E12')
        self.games['G28'] = self.game(self.games['G23'].winner ,
                                 self.games['G24'].winner,'E14')
        
        #bo4
        self.games['S1'] = self.game(self.games['G25'].winner ,
                                self.games['G26'].winner,'E1')
        self.games['S2'] = self.game(self.games['G27'].winner ,
                                self.games['G28'].winner,'E1')
        #bronze
        self.games['Bronze'] = self.game(self.games['S1'].loser ,
                                    self.games['S2'].loser,'E1')
        #bronze
        self.games['Final'] = self.game(self.games['S1'].winner ,
                                    self.games['S2'].winner,'E1')
                
    @property
    def winner(self):
        return self.games['Final'].winner
        
    @property
    def medals(self):
        return (self.games['Final'].winner,
               self.games['Final'].loser,
               self.games['Bronze'].winner)

    def game(self,p1,p2,k,MC = True):
        return Game(p1,p2,k,self.data,self.lanes,MC)

    
def gen_Cup_16(ranks,data,lanes,n_max):
    for n in range(n_max):
        yield Cup_16(ranks,data,lanes)
        
def gen_Cup_32(ranks,data,lanes,n_max):
    for n in range(n_max):
        yield Cup_32(ranks,data,lanes)