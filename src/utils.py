from api_hh import HHApi
from vacancy import Vacancy
from fileworker import JSONWorker


HH = HHApi()
hh_vacancies = HH.get_vacancy("моряк")
print(hh_vacancies)

vac = JSONWorker.write_file(hh_vacancies)
print(vac)

