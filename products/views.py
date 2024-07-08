from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse
from .models import Product, Category, Favorite, Review, ProductRecommendation
from .forms import ProductForm, ReviewForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    print("all products", products)
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

            if not products.exists():
                messages.error(request, "No products found matching your search criteria.")
                return redirect(reverse('products'))

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details and handle reviews """
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product)
    is_favorite = False
    recommended_products = (
        Product.objects
        .filter(category=product.category)
        .exclude(id=product_id)
        [:4]
    )

    if request.user.is_authenticated:
        is_favorite = (
            Favorite.objects
            .filter(user=request.user, product=product)
            .exists()
        )

        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.product = product
                review.user = request.user
                review.save()
                messages.success(request, 'Your review has been submitted!')
                return redirect('product_detail', product_id=product.id)
            else:
                messages.error(request, 'There was an error with your review.')
        else:
            form = ReviewForm()
    else:
        form = None

    context = {
        'product': product,
        'reviews': reviews,
        'is_favorite': is_favorite,
        'review_form': form,
        'recommended_products': recommended_products,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


def add_to_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.user.is_authenticated:
        favorite, created = Favorite.objects.get_or_create(
            user=request.user,
            product=product
        )
        if created:
            messages.success(
                request,
                'Product added to favorites successfully.'
            )
        else:
            favorite.delete()
            messages.success(request, 'Product removed from favorites.')

        return redirect(reverse('product_detail', args=[product_id]))

    else:
        messages.warning(request, 'Please login to add to favorites.')
        return redirect(reverse('product_detail', args=[product_id]))


def remove_from_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.user.is_authenticated:
        try:
            favorite = Favorite.objects.get(user=request.user, product=product)
            favorite.delete()
            messages.success(
                request,
                'Product removed from favorites successfully.'
            )
        except Favorite.DoesNotExist:
            messages.error(request, 'Product is not in your favorites.')
        except Exception as e:
            messages.error(
                request,
                f'Error removing product from favorites: {str(e)}'
            )

        return redirect(reverse('favorite_list'))

    else:
        messages.warning(request, 'Please login to remove from favorites.')
        return redirect(reverse('product_detail', args=[product_id]))


@login_required
def favorite_list(request):
    favorites = Favorite.objects.filter(user=request.user)
    context = {
        'favorites': favorites,
        'on_favorite_page': True,
    }
    return render(request, 'products/favorites.html', context)
