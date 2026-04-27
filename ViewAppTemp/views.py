from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from .utils import get_current_timestamp

branches_data = {
    "London": "Філія у Лондоні: Головний офіс у Великій Британії, заснований у 2010 році.",
    "Paris": "Філія у Парижі: Європейський центр дизайну та маркетингу.",
    "Kyiv": "Філія у Києві: Центр розробки програмного забезпечення.",
    "Odessa": "Філія у Одесі: Найкраща філія у світі блін бомба",
    "Japan": "Філія у Японії: Топ 2 філія",
    "India": "Філія у Індії: топ крішна філія, одобрено партією Калі",
    "China": "Філія у Китаї: одобрено партією + миска рису",
    "Italy": "одобрено персиком із Call me by your name",
    "Chornogoria": "одобрено моїм старшим братом",
    "Roblox": "удаліла мама поздно"

}
history_data = {
    1885: "Франція 1885 страшно",
    1914: "Франція 1914 дуже страшно",
}
class Product:
    id: int
    slug: str
    name: str
    description: str

    def __init__(self, id, slug, name, description):
        self.id = id
        self.slug = slug
        self.name = name
        self.description = description

    def __str__(self):
        return f"""
            <a href=#> {self.slug}</a>
            <h1>{self.name}</h1>
            <h3>{self.description}
        """

class ProductSerializer(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, Product):
            print(o.__dict__)
            result = {}
            result["id"] =o.id
            result["slug"] = o.slug
            result["name"] = o.name
            result["description"] = o.description
            return result
        return super().default(o)

products = [
        Product(get_current_timestamp(), "first-product", "First product", "Very good product"),
        Product(get_current_timestamp(), "second-product", "Second product", "Very good product"),
        Product(get_current_timestamp(), "third-product", "Third product", "Very good product")
]

class ProductView(View):
    @csrf_exempt
    def post(self, request: HttpRequest):
        return JsonResponse({"message": "You called POST method"})

    def get(self, request: HttpRequest):
        param_id = request.GET.get("id", None)
        param_slug = request.GET.get("slug", None)
        if param_id == None and param_slug == None:
            if len(products) > 0:
                return JsonResponse(products, ProductSerializer, safe = False)

            else:
                r = JsonResponse({"errors_data" : "Products not found"})
                r.status_code = 404
                r.reason_phrase = "Not Found"
                return r

        if param_id is not None:
            try:
                id = int(param_id)
            except ValueError:
                r = JsonResponse({"errors_data" : "'Id' parameter must be number"})
                r.status_code = 400
                r.reason_phrase = "Bad Request"
                return r
            result = list(filter(lambda x: x.id == id, products))
            if len(result) < 1:
                r = JsonResponse({"errors_data" : "Products not found"})
                r.status_code = 400
                r.reason_phrase = "Not Found"
                return r
            else:
                return JsonResponse(result[0], ProductSerializer, safe = False)

        elif param_slug is not None:
            result = list(filter(lambda x: x.slug == param_slug, products))
            if len(result) < 1:
                r = JsonResponse({"errors_data" : "Products not found"})
                r.status_code = 400
                r.reason_phrase = "Not Found"
                return r
            else:
                return JsonResponse(result[0], ProductSerializer, safe = False)

class HomeView(View):
    def get(self, request: HttpRequest):
        return HttpResponse("<h1>Головна сторінка</h1>")

class NewsView(View):
    def get(self, request: HttpRequest):
        return HttpResponse("<h1>Новини компанії</h1>")

class ManagementView(View):
    def get(self, request: HttpRequest):
        return HttpResponse("<h1>Керівництво компанії</h1>")

class AboutView(View):
    def get(self, request: HttpRequest):
        return HttpResponse("<h1>Про компанію</h1>")
class ContactsView(View):
    def get(self, request: HttpRequest):
        return HttpResponse("<h1>Контакти</h1>")

def exept_view(request):
    return ValueError("Failed!")

def index(request):
    return HttpResponse("<h1>Start Page</h1>")

def json_response(request):
    return JsonResponse({
        "status_code" : 404,
        "reason_phrase" : "Not Found",
        "data" : "Hello"
    })

def get_all_products(request):
    return JsonResponse(products, ProductSerializer, safe=False)

def get_product_by_id(request, id):
    r = JsonResponse({})
    result = list(filter(lambda x: x.id == id, products))
    if len(result) < 1:
        r.status_code = 404
        r.content = {"status_code" : 404, "reason_phrase" : "Product not found", "data": None}

    return JsonResponse(result[0], ProductSerializer, safe=False)


def all_branches(request):
    branches_list = "</li><li>".join(branches_data.keys())
    return HttpResponse(f"<h1>Наші філії:</h1><ul><li>{branches_list}</li></ul>")

def branch_detail(request, city):
    info = branches_data.get(city, "Інформація про філію у цьому місті відсутня.")
    return HttpResponse(f"<h1>{city}</h1><p>{info}</p>")

def all_history(request):
    history_list = "</li><li>".join(branches_data.keys())
    return HttpResponse(f"<h1>Перша історія:</h1><ul><li>{history_list}</li></ul>")

def history_detail(request, data):
    info = branches_data.get(data, "Інформація про історі")
    return HttpResponse(f"<h1>{data}</h1><p>{info}</p>")