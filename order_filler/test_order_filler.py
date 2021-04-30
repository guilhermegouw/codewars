from.order_filler import fillable


stock = {
    'football': 4,
    'boardgame': 10,
    'leggos': 1,
    'doll': 5,
}

def test_exiting_item_right_amount():
    output = fillable(stock, 'football', 3)
    assert output == True
    
def test_exiting_item_greater_amount():
    output = fillable(stock, 'leggos', 3)
    assert output == False

def test_not_existing_item():
    output = fillable(stock, 'bike', 3)
    assert output == False
