# НЕ МОЖЕ ДА СЕ ПРОМЕНЯ име на КЛЮЧ,
# МОЖЕ ДА СЕ ИЗТРИЕ ДВОЙКА КЕУ VALUE И ПОСЛЕ ДА СЕ ДОБАВИ НОВ ключ
# и стойност със запазената value
test_dictionary = {"a":"A","b":"B"}
print(test_dictionary)
value = test_dictionary["b"]
test_dictionary.pop("b")
print(test_dictionary)
test_dictionary["c"] = value
print(test_dictionary)