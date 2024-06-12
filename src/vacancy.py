class Vacancy:
    def __init__(self, name, url, salary_from, city, employment):
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.city = city
        self.employment = employment
        #self.validate()

    def validate(self):
        if self.salary_from == None:
            self.salary_from = 0
        if self.employment == None:
            self.employment = "Не указано"

    @classmethod
    def create_vacancies(self, data):
        instances = []
        for vac_info in data:
            name = vac_info.get('name')
            instances.append(name)
            url = vac_info.get('alternate_url')
            instances.append(url)
            salary_from = vac_info.get('salary')
            f = salary_from['from']
            print(f)
            instances.append(f)
            salary_to = vac_info.get('salary')
            instances.append(salary_to)
            city = vac_info.get('city')
            instances.append(city)
            employment = vac_info.get("employment""name")
            instances.append(employment)
        return instances

    def __lt__(self, other):
        return self.salary_from < other.salary_from

    def to_json(self):
        "формирует словарь для вакансии"
        return {
            'name': self.name,
            'url': self.url,
            'salary_from': self.salary_from,
            'salary_to': self.salary_to,
            'city': self.city,
            'employment': self.employment
        }


