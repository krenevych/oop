class GeneralStaff():
    def __init__(self, generals, secretPaper):
        self.generals = generals
        self.secretPaper = secretPaper

    def __str__(self):
        res = """GeneralStaff: У генеральному штабі є %d геренералів та %d секретних паперів """ % \
              (self.generals, self.secretPaper)
        return res


class MilitaryBase():
    def __init__(self, officers, soldiers, jeeps, tanks):
        self.officers = officers
        self.soldiers = soldiers
        self.jeeps = jeeps
        self.tanks = tanks

    def __str__(self):
        res = """MilitaryBase: На військовій базі є %d офіцерів, %d солдатів, %d джипів та %d танків.  """ % \
              (self.officers, self.soldiers, self.jeeps, self.tanks)
        return res


if __name__ == '__main__':

    generalStaff = GeneralStaff(20, 100)
    print(generalStaff)

    militaryBase = MilitaryBase(10, 1000, 300, 20)
    print(militaryBase)

