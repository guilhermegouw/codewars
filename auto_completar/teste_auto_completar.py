from auto_completar import auto_completar
import unittest


class TestAutoCompletar(unittest.TestCase):
    def setUp(self):
        self.lista = [
            "Avião",
            "avental",
            "cola",
            "avante",
            "alarme",
            "abelha",
            "abutre",
        ]

    def test_av(self):
        self.assertEqual(
            auto_completar(self.lista, "av"), ["Avião", "avental", "avante"]
        )

    def test_ab(self):
        self.assertEqual(auto_completar(self.lista, "ab"), ["abelha", "abutre"])

    def test_a(self):
        self.assertEqual(
            auto_completar(self.lista, "a"),
            ["Avião", "avental", "avante", "alarme", "abelha"],
        )

    def test_b(self):
        self.assertEqual(auto_completar(self.lista, "b"), [])


if __name__ == "__main__":
    unittest.main()
