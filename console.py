import pdb
from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository


city_repository.delete_all()
country_repository.delete_all()

country1 = Country("France", "Europe")
country_repository.save(country1)
country2 = Country("Germany", "Europe")
country_repository.save(country2)

# country_repository.select_all()

city_1 = City("Paris", country1, False)
city_repository.save(city_1)

city_2 = City("Berlin", country2, False)
city_repository.save(city_2)


pdb.set_trace()