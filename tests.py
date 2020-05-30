# tests.py

def capital_case(x):
    return x.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

def increment(x):
    return x+1

def test_increment():
    assert increment(15) == 16

def decrement(x):
    return x+1

# This will fail!
def test_decrement():
    assert decrement(15) == 14


# def expected_result():
#     return [
    
    
import NewDijkstra as nd

def new_dijkstra():
    return nd.main()

def test_new_dijkstra():
    assert new_dijkstra() == ['Seattle', 'Minneapolis', 'Chicago', 'Boston'] 
