import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from ads.models import Ads, Categories
from avito import settings
from users.models import Users


class Index(View):
    def get(self, request):
        return JsonResponse({'status': 'ok'}, status=200)


class CategoriesView(ListView):
    model = Categories

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        res = []
        for category in self.object_list:
            res.append(
                {'id': category.id,
                 'name': category.name}
            )
        return JsonResponse(res, safe=False)


class CategoryView(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs):
        category = self.get_object()
        return JsonResponse({'id': category.id, 'name': category.name})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryCreateView(CreateView):
    model = Categories
    fields = ['name']

    def post(self, request, *args, **kwargs):
        category_data = json.loads(request.body)
        new_category = Categories.objects.create(name=category_data.get('name'))
        return JsonResponse({'pk': new_category.id, 'name': new_category.name}, status=201)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Categories
    fields = ['name']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        category_data = json.loads(request.body)
        self.object.name = category_data['name']

        self.object.save()
        return JsonResponse({'pk': self.object.id,
                             'name': self.object.name}, status=201)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Categories
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok. deleted"}, status=200)


class AdsView(ListView):
    model = Ads

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.select_related('author')
        paginator = Paginator(self.object_list, settings.ON_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        res = []
        for ad in page_obj:
            res.append(
                {'id': ad.id,
                 'name': ad.name,
                 'author': ad.author.first_name,
                 'price': ad.price,
                 'description': ad.description,
                 'is_published': ad.is_published,
                 'image': ad.image.url if ad.image else 'no image'
                 }
            )

        return JsonResponse({'ads': res,
                             'pages': page_obj.number,
                             'total': page_obj.paginator.count},
                            safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ads
    fields = ["name", "author", "price", "description", "is_published", "category"]

    def post(self, request, *args, **kwargs):
        req_data = json.loads(request.body)
        author = get_object_or_404(Users, req_data["author_id"])
        category = get_object_or_404(Categories, req_data["category_id"])

        ad = Ads.objects.create(
            name=req_data["name"],
            author=author,
            price=req_data["price"],
            description=req_data["description"],
            is_published=req_data["is_published"],
            category=category,
        )

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author_id": ad.author_id,
            "author": ad.author.first_name,
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "category_id": ad.category_id,
            "image": ad.image.url if ad.image else 'no image',
        })


class AdView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse(
            {
                'id': ad.id,
                'name': ad.name,
                'author': ad.author,
                'price': ad.price,
                'description': ad.description,
                'address': ad.address,
                'is_published': ad.is_published
            }
                            )


@method_decorator(csrf_exempt, name='dispatch')
class AdUploadImageView(UpdateView):
    model = Ads
    fields = ['image']

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.image = request.FILES.get("image")
        self.object.save()

        return JsonResponse(
            {
                'id': self.object.id,
                'name': self.object.name,
                'author': self.object.author.username,
                'price': self.object.price,
                'description': self.object.description,
                'is_published': self.object.is_published,
                'image': self.object.image.url if self.object.image else 'No image'
            }
        )


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ads
    fields = ["name", "author", "price", "description", "is_published", "category"]

    def post(self, request, *args, **kwargs):
        req_data = json.loads(request.body)
        author = get_object_or_404(Users, req_data["author_id"])
        category = get_object_or_404(Categories, req_data["category_id"])

        ad = Ads.objects.create(
            name=req_data["name"],
            author=author,
            price=req_data["price"],
            description=req_data["description"],
            is_published=req_data["is_published"],
            category=category,
        )

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author_id": ad.author_id,
            "author": ad.author.first_name,
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "category_id": ad.category_id,
            "image": ad.image.url if ad.image else 'no image',
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
    model = Ads
    fields = ["name", "author", "price", "description", "category"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        req_data = json.loads(request.body)
        self.object.name = req_data["name"]
        self.object.price = req_data["price"]
        self.object.description = req_data["description"]

        self.object.author = get_object_or_404(Users, req_data["author_id"])
        self.object.category = get_object_or_404(Categories, req_data["category_id"])

        self.object.save()
        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author_id": self.object.author_id,
            "author": self.object.author.first_name,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "category_id": self.object.category_id,
            "image": self.object.image.url if self.object.image else None,
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    model = Ads
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok. deleted"}, status=200)
