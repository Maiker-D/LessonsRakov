calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()
    list_to_search = [item.lower() for item in list_to_search]
    return string in list_to_search


print(string_info('Capybara'))
print(string_info('Armagedon'))
print(is_contains('urban', ['ban', 'BaNan', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycle', 'ceclic']))  # No matches
print(calls)
