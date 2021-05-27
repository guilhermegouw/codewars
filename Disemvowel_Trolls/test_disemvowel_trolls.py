from Disemvowel_Trolls.disemvowel_trolls import disem_vowel
from .disemvowel_trolls import disem_vowel


def test_disem_vowel():
    output = disem_vowel("This website is for losers LOL!")
    assert output == "Ths wbst s fr lsrs LL!"
