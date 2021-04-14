from django.urls import path
from api.views import companiesList, companiesDetail, companiesVacancies,vacanciesList, vacanciesDetail, vacanciesTopTen

urlpatterns = [
    path('companies/', companiesList),
    path('companies/<int:companyId>/', companiesDetail),
    path('companies/<int:companyId>/vacancies', companiesVacancies),
    path('vacancies/', vacanciesList),
    path('vacancies/<int:vacancyId>/', vacanciesDetail),
    path('vacancies/top_ten', vacanciesTopTen)
]