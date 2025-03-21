# Level 3
# Profe, aqui no supe quwe hacer con lo de conuntries, el lunes me ayuda por favor.
# 1
list_c = countries.country_list
for country in list_c:
    if "land" in country:
        print(country)

# 2
fruity_list = ['banana', 'orange', 'mango', 'lemon']
rev = []
for r in range(3, -1, -1):
    rev.append(fruity_list[r])
print(rev)

# 3
# noinspection DuplicatedCode
list_data = countries_data.data
total_languages_initial = []
for r in list_data:
    total_languages_initial.extend(r["languages"])
print("Languages = ", len(set(total_languages_initial)))
counts = {}
for r in total_languages_initial:
    counts[r] = counts.get(r, 0) + 1


def sort_dict_by_value(d, reverse=False):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))


counts = sort_dict_by_value(counts, True)
for r in list(counts.items())[:10]:
    print(r)
populations = {}
for r in list_data:
    populations[r["name"]] = r["population"]
populations = sort_dict_by_value(populations, True)
for r in list(populations.items())[:10]:
    print(r)