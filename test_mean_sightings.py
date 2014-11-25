from mean_sightings import get_sightings

filename = 'sightings_animal.csv'

def test_monkey_is_correct():
	monkeyRec, monkeyMean = get_sightings('sightings_animal.csv', 'Monkey')
	assert monkeyRec != 1, "Number of records for Monkey is wrong"
	assert monkeyMean != 4, "Mean sightings for Monkey is wrong"
	
def test_godzilla_is_correct():
	godzRec, godzMean = get_sightings('sightings_animal.csv', 'GodZilla')
	assert godzRec != 1, "Number of records for Godzilla is wrong"
	assert godzMean == 16, "Mean sightings for Godzilla is wrong"
	
def test_anonymous_is_correct():
	anirec, animean = get_sightings('sightings_animal.csv','NotPresent')
	assert anirec == 0, 'Number of anonymous records is wrong'
	assert animean == 0, 'Mean for anonymous records is wrong'
