from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from webapp.forms import ReviewForm
from webapp.models import Review, Product


class ReviewListView(PermissionRequiredMixin, ListView):
    model = Review
    template_name = "reviews/review_list.html"
    context_object_name = 'reviews'
    permission_required = 'webapp.can_look_review_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(moderated=False)
        return queryset.order_by('-updated_at')


class ReviewAddView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/create.html"

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        review = form.save(commit=False)
        review.author = self.request.user
        review.product = product
        review.save()
        return redirect('webapp:product_view', pk=product.pk)


class ReviewUpdateView(PermissionRequiredMixin, UpdateView):
    model = Review
    template_name = 'reviews/update.html'
    form_class = ReviewForm
    permission_required = 'webapp.change_review'

    def form_valid(self, form):
        response = super().form_valid(form)
        review = form.save(commit=False)
        review.moderated = False
        review.save()
        return response

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse("webapp:product_view", kwargs={"pk": self.object.product.pk})


class ReviewDeleteView(PermissionRequiredMixin, DeleteView):
    model = Review
    permission_required = 'webapp.delete_review'

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse("webapp:product_view", kwargs={"pk": self.object.product.pk})