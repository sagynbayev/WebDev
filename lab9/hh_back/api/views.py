from django.http.response import JsonResponse
from api.models import Company
from api.models import Vacancy

def companiesList(request):
    companies = Company.objects.all()
    companies_json = [company.to_json() for company in companies]
    print(companies_json)
    return JsonResponse(companies_json, safe=False)

def companiesDetail(request, companyId):
    try:
        company = Company.objects.get(id = companyId)
    except Company.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse(company.to_json())

def companiesVacancies(request, companyId):
    try:
        vacancies = Vacancy.objects.filter(company=companyId)
    except Company.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)
    # vacancies = Vacancy.objects.filter(company_id=companyId)
    # vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    # return JsonResponse(vacancies_json, safe=False)

def vacanciesList(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    print(vacancies_json)
    return JsonResponse(vacancies_json, safe=False)

def vacanciesDetail(request, vacancyId):
    try:
        vacancy = Vacancy.objects.get(id = vacancyId)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse(vacancy.to_json())

def vacanciesTopTen(request):
    vacancies = Vacancy.objects.order_by("-salary")[0:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    print(vacancies_json)
    return JsonResponse(vacancies_json, safe=False)