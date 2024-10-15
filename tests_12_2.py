import runner2, unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.usein = runner2.Runner('Усейн', 10)
        self.andrei = runner2.Runner('Андрей', 9)
        self.nik = runner2.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        cls.all_results = list(reversed(cls.all_results))
        for result in cls.all_results:
            formatted_result = '{' + ', '.join(f'{place}: {runner}' for place, runner in result.items()) + '}'
            print(formatted_result)


    def test_usein_nik(self):
        tour = runner2.Tournament(90, self.usein, self.nik)
        result = tour.start()
        self.all_results.append(result)
        last = result[max(result.keys())]
        self.assertTrue(last == "Ник")

    def test_andrei_nik(self):
        tour = runner2.Tournament(90, self.andrei, self.nik)
        result = tour.start()
        self.all_results.append(result)
        last = result[max(result.keys())]
        self.assertTrue(last == "Ник")

    def test_all(self):
        tour = runner2.Tournament(90, self.andrei, self.usein, self.nik)
        result = tour.start()
        self.all_results.append(result)
        last = result[max(result.keys())]
        self.assertTrue(last == "Ник")

    def test_short_distance(self):
        tour = runner2.Tournament(3, self.andrei, self.usein, self.nik)
        result = tour.start()
        self.all_results.append(result)
        last = result[max(result.keys())]
        self.assertTrue(last == "Ник")


        
        