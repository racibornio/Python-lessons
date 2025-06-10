# Klasa Club.

class Club():

    def __init__(self, clubName, maxMembers):
        self.clubName = clubName
        self.maxMembers = maxMembers
        self.membersList = []

    def addMember(self, name):
        # Należy się upewnić, że jest miejsce dla nowego członka klubu.
        if len(self.membersList) < self.maxMembers:
            self.membersList.append(name)
            print('OK.', name, 'został(a) dołączony(a) do klubu', self.clubName, 'club')
        else:
            print('Przepraszamy. W tym momencie nie możemy dołączyć', name, 'do klubu', self.clubName, '.')
            print('Do klubu należy maksymalna liczba członków:', self.maxMembers, '.')

    def report(self):
        print()
        print('Oto', len(self.membersList), 'członków', self.clubName, 'klubu:')
        for name in self.membersList:
            print('   ' + name)
        print()

